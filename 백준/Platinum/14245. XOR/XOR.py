import sys
input = sys.stdin.readline

def init(n):
    global tree,lazy
    tree = [0]*(4*n)
    lazy = [0]*(4*n)
def build(node,start,end, arr):
    if start == end:
        tree[node] = arr[start]
        return
    mid = (start+end) // 2
    build(node*2, start,mid, arr)
    build(node*2+1, mid+1, end, arr)
    tree[node] = tree[node*2] ^ tree[node*2+1]
    
def propagate(node, start, end):
    if lazy[node] != 0:
        if (end-start+1)%2:
            tree[node] ^= lazy[node]
        if start != end:
            lazy[node*2] ^= lazy[node]
            lazy[node*2+1] ^= lazy[node]
        lazy[node] = 0

def update_range(node, start, end, l, r, value):
    propagate(node,start,end)
    if start > r or end < l:
        return
    if l <= start and end <= r:
        lazy[node] ^= value
        propagate(node, start, end)
        return
    mid = (start + end) // 2
    update_range(node*2, start, mid, l, r, value)
    update_range(node*2+1, mid+1, end, l ,r, value)
    tree[node] = tree[node*2] ^ tree[node*2+1]

def query_range(node, start, end, l, r):
    propagate(node, start, end)
    if start > r or end < l:
        return 0
    if l <= start and end <= r:
        return tree[node]
    mid = (start + end) // 2
    return query_range(node*2, start, mid, l, r) ^ query_range(node*2+1, mid+1,end, l,  r)
n = int(input())
init(n)
arr = list(map(int,input().split()))
build(1, 0, n-1, arr)
m = int(input())
for i in range(m):
    a = list(map(int,input().split()))
    if a[0] == 1:
        update_range(1, 0, n - 1, a[1] , a[2] , a[3])
    else:
        print(query_range(1, 0, n - 1, a[1] , a[1] ))
