# Part2 Chapter05 DFS/BFS

# 1. 꼭 필요한 자료구조 기초

# 탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
# 자료구조 : 데이터를 표현하고 관리하고 처리하기 위한 구조

# 스택 ( stack )
# 박스 쌓기 ( 선입후출 또는 후입선출 )
# a, b, c , ==> c, b, a

# 에제 5-1

def stack():

    stack = []
    stack.append(5)
    stack.append(2)
    stack.append(3)
    stack.append(7)
    stack.pop()
    stack.append(1)
    stack.append(4)
    stack.pop()

    return stack # 최하단 원소부터 출력
    # return stack[::-1] #최상단 원소부터 출력

# print(stack())

# 큐 ( Queue )
# 놀이동산 줄 서기 ( 선입선출 )
# a, b, c ==> a, b, c

# 예제 5-2
# 큐 구현을 위한 deque 라이브러리
from collections import deque

def queue():

    # queue 구현을 위한 deque() 라이브러리 사용
    queue = deque()

    queue.append(5)
    queue.append(2)
    queue.append(3)
    queue.append(7)
    queue.popleft()
    queue.append(1)
    queue.append(4)
    queue.popleft()

    return queue #먼저 들어온 순서대로 출력
    # return queue.reverse()

# print(queue())


# 재귀함수
# 자기자신을 다시 호출하는 함수

#예제 5-3, 5-4

def recursive_function(i):

    # 이래 조건문 없다면 인터프리터 호출 제한으로 인해, 오류발생 5-3
    # 100 호출 뒤 종료를 위한 조건문 5-4
    if i == 100:
        return

    print('재귀함수 호출')
    recursive_function(i+1)

# print(recursive_function(1))

# 예제 5-5 팩토리얼

def factorial_iterative(n):

    result = 1

    for i in range(1,n + 1):
        result *= i
    return result

def factorial_recursive(n):

    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

# print('반복로 호출 ::',factorial_iterative(5))
# print('재귀로 호출 ::',factorial_recursive(5))


# 2. 탐색 알고리즘 DFS / BFS

# DFS : 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

# 그래프는 노드, 간선으로 표현되며, 이때의 노드를 정점이라고 말한다.

# 예제 5-6 인접행렬

# 무한 비용 선언
# INF = 999999999
#
# graph = [
#     [0,7,5],
#     [7,0,INF],
#     [5,INF,0]
# ]

# print(graph)

# 예제 5-7 인접리스트 방식

# graph = [[] for _ in range(3)]
#
# # 노드 0에 연결된 노드 정보 저장
# graph[0].append((1,7))
# graph[0].append((2,5))
#
# # 노드 1에 연결된 노드 정보 저장 ( 노드, 거리 )
# graph[1].append((0,7))
#
# # 노드 2에 연결된 노드 정보 저장 ( 노드, 거리 )
# graph[2].append((0,5))
#
# print(graph)


# 5-8 DFS 예제
# 방문순서 : 1 -> 2 -> 7 -> 6 -> 8 -> 3 -> 4 -> 5

def dfs(graph,v,visited):

    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i ,visited)


# DFS 예제 그래프
# [ 노드번호, 자식노드1, 자식노드2 ]
graph = [
    [], # 0
    [2,3,8], # 1
    [1,7], # 2
    [1,4,5], # 3
    [3,5], # 4
    [3,4], # 5
    [7], # 6
    [2,6,8], # 7
    [1,7] # 8
]

# 방문정보를 리스트 자료형으로 표현
# [ False, False, False, False, False, False, False, False, False, False, False ]
visited = [False] *9

#print(dfs(graph,1,visited))


# BFS : 너비우선탐색, 가까운노드부터 탐색하는 알고리즘

# 예제 5-9 BFS 예제
# 방문순서 : 1 -> 2 -> 3 -> 8 -> 7 -> 4 -> 5 -> 6

from collections import deque

def bfs(graph, start, visited):

    queue = deque([start])

    visited[start] = True

    while queue:

        v = queue.popleft() # 큐에서 빼는 숫자 값
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


#print(bfs(graph,1,visited))


# DFS vs BFS
# 스택    큐
# 재귀함수  큐 자료구조
# 인접      최소


# 3. 음료수 얼려 먹기

# 구멍이 뚫린 부분 0, 칸막이 존재하는 부분 1
# 구멍이 뚫린 부분 상하좌우로 붙어 있을 경우 서로 연결된 것으로 간주
# 이 때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수는 ?
# 문제 4 * 5 틀에서는 3개가 생성된다.

# graph 4*5 ==> return 3
# 00110
# 00011
# 11111
# 00000

# n, m = map(int, input().split())
#
# graph = []
#
# for i in range(n):
#     graph.append(list(map(int,input())))

def drinkIcy(n,m):

    result = 0

    for i in range(n):
        for j in range(m):

            if dfs2(i,j) == True:
                result += 1

    return result


def dfs2(x,y):

    if x <= -1 or x >= n or y <= -1 or y>= m:
        return False

    if graph[x][y] == 0:

        graph[x][y] = 1 # 방문처리

        # 상하좌우 위치도 모두 재귀적으로 호출
        # (0,0) (0,1) (0,2) (0,3)
        # (1,0) (1,1) (1,2) (1,3)
        # (2,0) (2,1) (2,2) (2,3)
        dfs2(x - 1,y)   #상
        dfs2(x, y - 1)  #좌
        dfs2(x + 1, y)  #하
        dfs2(x , y + 1) #우
        return True

    return False


#print(drinkIcy(n,m))


# 4. 미로 탈출

# 출발 1,1 ( 실제 0,0 ) , 탈출 N,M
# 괴물이 있는부분 0, 올바른 길 1
# 동빈이가 탈출하기 위해 움직여야하는 최소 칸의 개수?
# 3 * 3 Graph => 아래 그래프의 경우 최소칸 개수는 5개
# 1 0 0
# 1 1 1
# 0 0 1

# 1 0 0
# 2 3 4
# 0 0 5 => 최소 5칸

from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))


def bfs2(x,y):

    # 이동할 네방향 ( 상하좌우 )
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            # 영역 밖으로 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문한 경우에만 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 이동할때마 1씩 더해서, 최종 칸수 확인
                queue.append((nx,ny))

    # 가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]


print(bfs2(0,0))