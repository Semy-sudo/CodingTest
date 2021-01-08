from collections import deque

#deque를 스택처럼-> append() pop()
#deque를 큐 처럼 -> append() popleft()

#BFS 메서드 정의
def bfs(graph,start,visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v,end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True






graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False]*9 

bfs(graph,1,visited) # 그래프, 시작노드, 방문여부