from collections import deque
n,m = map(int, input().split())
graph=[[] for _ in range(n+1)]
in_degree = [0] * (n+1)

for i in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

def topology_sort() :
    res = []
    queue = deque()
    for i in range(1, n+1) :
        if in_degree[i] == 0 :
            queue.append(i)
    
    while queue :
        cur = queue.popleft()
        res.append(cur)
        
        for i in graph[cur] :
            in_degree[i] -= 1
            if in_degree[i] == 0 :
                queue.append(i)
    
    for i in res :
        print(i, end=' ')

topology_sort()
