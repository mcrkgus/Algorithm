#DFS - Depth First Search
#깊이 우선 탐색 - 깊은 부분을 우선적으로 탐색
#스택 자료구조 사용

visited = [False] * 9

def DFS(graph, v, visited) :
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    
    for i in graph[v] :
        if not visited[i] :
            DFS(graph, i, visited)
            
#현재 노드와 연결된 다른 노드를 재귀적으로 방문
