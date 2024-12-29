a= int(input())
b = sum(list(map(int,input().split())))
if b > 0:
    print('Right')
elif b <0 :
    print('Left')
else:
    print('Stay')