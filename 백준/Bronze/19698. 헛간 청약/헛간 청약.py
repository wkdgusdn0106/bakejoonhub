n,h,w,l = map(int,input().split())
print(min(n, (h//l)*(w//l)))