def find(x):
    if x == parent[x]:
      return x
    parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y :
        parent[y] = x
    else :
        parent[x] = y
        
N = int(input())
M = int(input())
arr = []
res = 0
parent =[i for i in range(N+1)]

for i in range(M) :
    a, b, c = map(int, input().split())
    arr.append((c, a, b))
    
arr.sort()

# 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
for i in arr :
    c, a, b = i
     # find 연산 후, 부모노드 다르면 사이클 발생 X으므로 union 연산 수행 -> 최소 신장 트리에 포함
    if find(a) != find(b) :
        union(a, b)
        res += c
