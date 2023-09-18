from collections import deque

# n개의 줄, m개의 열
n, m = map(int,input().split())

# 미로의 정보 입력받기
graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

# 방향 정보(상하좌우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 출발 노드
queue = deque()
deque.append((0,0))
# 혹은 deque([(0,0)])

while queue :
  # 큐에서 하나의 원소를 꺼내서 출력
  x, y = queue.popleft()

  # 꺼낸 원소와 인접노드 확인
  for i in range(len(dx)):
    nx = x+dx[i]
    ny = y+dy[i]

    # 범위를 벗어난 노드 무시
    if nx>n-1 or ny>m-1 or nx<0 or ny<0 :
      continue

    # 아직 방문하지 않은 노드라면
    # 처음 방문하는 경우가 바로 최단거리다
    if graph[nx][ny]==1:
      queue.append((nx,ny))
      graph[nx][ny] = graph[x][y]+1 # 직전 노드+1


print(graph[n-1][m-1])
