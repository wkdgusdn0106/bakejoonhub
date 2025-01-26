n = int(input())
def calculate(li,st,en):
    left_idx=-1;right_idx=-1;left_cnt=0;right_cnt=0;count=0
    for i in range(st,en):
        if li[i] == '(':
            if left_idx==-1:
                left_idx=i
            left_cnt+=1
        else:
            right_idx=i
            right_cnt+=1
        if left_cnt == right_cnt and left_cnt != 0 and left_idx != -1 and right_idx != -1:
            if right_idx-left_idx==1:
                count+=1
            else:
                count+= 2*calculate(li,left_idx+1,right_idx)
            left_idx=-1;right_idx=-1;left_cnt=0;right_cnt=0;
    return count
for _ in range(n):
    fa = list(input())
    fb = list(input())
    A = calculate(fa,0,len(fa))
    B = calculate(fb,0,len(fb))
    if A == B:
        print('=')
    elif A < B:
        print('<')
    else:
        print('>')

