#BFS
#너비 우선 탐색 : 가까운 노드부터 탐색
#큐 자료구조 사용

from collections import deque

def BFS(graph, start, visited) :
    queue : deque([start])
    
    #현재 노드 방문 처리
    visited[start] = True
    
    #큐가 빌 때까지 반복
    while queue :
        #큐에서 하나의 원소를 뽑아 print
        v = queue.popleft()
        print(v, end = ' ')
        
        #아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
                
visited = [False] * 9

