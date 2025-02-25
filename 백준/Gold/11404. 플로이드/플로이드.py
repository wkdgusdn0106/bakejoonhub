INF = float('inf')

def floyd_warshall(n, graph):
    # 거리 행렬 초기화
    dist = [[INF] * (n+1) for _ in range(n+1)]
    
    # 자기 자신으로 가는 비용은 0
    for i in range(1,n+1):
        dist[i][i] = 0

    # 그래프 값 복사
    for u, v, w in graph:
        dist[u][v] = min(w,dist[u][v])  # 방향 그래프라면 이것만 사용
    # 플로이드 워셜 알고리즘 실행
    for k in range(1,n+1):  # 중간 노드
        for i in range(1,n+1):  # 출발 노드
            for j in range(1,n+1):  # 도착 노드
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] == INF:
                dist[i][j] = 0
    return dist

# 예제: (노드 개수, 간선 리스트)
n = int(input())
a = int(input())
graph = [list(map(int,input().split())) for i in range(a)]
result = floyd_warshall(n, graph)

# 출력
for row in result[1:]:
    print(*row[1:])
