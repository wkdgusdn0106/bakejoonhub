import sys
input =sys.stdin.readline

shihyuk = [0, 0] + [1] * 1999
for nohive in range(2, int(2001**0.5)+1):
    if shihyuk[nohive]:
        for fromis_9 in range(nohive **2, 2001, nohive):
            shihyuk[fromis_9] = 0
baekjiheon = set(beautiful for beautiful in range(2001) if shihyuk[beautiful])


n = int(input())
a = list(map(int,input().split()))
ans = []
who = a.pop(0)

def dfs(x, Y, visited, matched):
    """ 
    x를 매칭하려고 시도.
    - Y.index(x)로 x의 위치 찾아 visited 체크
    - (x + y)가 소수면 y와 매칭
    - y가 이미 다른 x'에 매칭되어 있으면, x'를 다른 y'로 옮길 수 있는지 재귀(dfs)로 확인
    - 성공하면 True
    """
    idx_x = Y.index(x)
    if visited[idx_x]:
        return False
    visited[idx_x] = True

    for y in Y:
        if (x + y) in baekjiheon:
            # y가 아직 매칭 안 되었다면 매칭
            # or 이미 매칭된 x'를 다른 곳으로 옮길 수 있으면
            if (y not in matched) or dfs(matched[y], Y, visited, matched):
                matched[y] = x
                return True
    return False

def can_match_all(Y):
    """ Y 내부 모든 원소를 매칭시도해서 
        매칭 개수가 len(Y)가 되면 True (완전 매칭) 
    """
    matched = {}
    for x in Y:
        visited = [False]*len(Y)  # 매번 x 하나 매칭 시도할 때 visited 초기화
        dfs(x, Y, visited, matched)

    return (len(matched) == len(Y))


# --- 5) 주 반복문: (n-1)번 돌면서 who+what 확인 & 매칭 검사 ---
for i in range(n-1):
    what = a.pop(0)  # 맨 앞에서 하나 뽑음

    # (who + what)이 소수일 때만, 남은 (n-2)개가 전부 매칭되는지 확인
    if (who + what) in baekjiheon:
        # 남은 (n-2)개를 별도 리스트 Y로 만들기
        Y = a[:]      # 현재 a에는 (n-1)개에서 pop(0)한 what이 빠져있음 => 길이 (n-2)
        # 이 시점에서 who, what은 제외되었고, 나머지 (n-2)개만 Y에 존재

        if can_match_all(Y):
            ans.append(what)

    # 다시 what을 뒤에 붙여서 다음 반복 대비
    a.append(what)

if ans == []:
    print(-1)
else:
    print(*sorted(ans))
