
# Part2 Chapter09 최단 경로

# 1. 가장 빠른 길 찾기

# 최단 경로 : 가장 짧은 경로를 찾는 알고리즘
#  ex. 다익스트라 최단경로, 플로이드 워셜, 벨만 포드 알고리즘 등
# ( 다익스트라와 플로이드 워셜이 테스트로 많이 나옴 )


# 다익스트라 최단 경로 알고리즘 : 여러개의 노드가 있을 때, 특정한 노드에서 출발하여, 다른노드로 가는 각각의 최단 경로를 구하는 알고리즘
# ( 가장 비용이 적은 노드를 선택하여 임의의 과정을 반복 )


# 예제 9-1 간단한 다익스트라 알고리즘 ( 시간복잡도 : O(V^2) -> V는 노드 수 )
# 입력 예시
# 6 11 -> 노드, 간선
# 1 -> 시작노드
# 1 2 2 -> a노드에서 b노드로 가는 비용이 c라는 의미
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2


import sys
input = sys.stdin.readline
INF = int(1e9) # 무한값을 의미 : 10억으로 설정

# 노드 개수, 간선 개수 입력
n,m = map(int,input().split())

#시작 노드
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트
graph = [[] for i in range(n+1)]

# 방문 이력 리스트
visited = [False] * (n+1)

# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split()) # a노드에서 b노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))


# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1,n+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#
#     return index
#
#
#
# def dijkstra(start):
#
#     distance[start] = 0
#     visited[start] = True
#
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#
#     # 시작노드를 제외한 전체 n-1개의 노드에 대해 반복
#     for i in range(n-1):
#
#         # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
#         now = get_smallest_node()
#         visited[now] = True
#
#         # 현재 노드와 연결된 다른 노드를 확인
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#
#             # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
#
#
# dijkstra(start)
#
# for i in range(1, n+1):
#
#     if distance[i] == INF:
#         print('INFINITY') # 도달할 수 없는 경우, 무한이라고 출력
#     else:
#         print(distance[i])




# 예제 9-2 개선된 다익스트라 알고리즘 ( 시간복잡도 : O(ElogV) -> V는 노드 수, E는 간선의 수 )

# 힙을 사용하여 구현 ( heapq 라이브러리 )
# 우선순위 큐 : 가장 우선순위가 높은 데이터부터 추출
# 입력 예시
# 6 11 -> 노드, 간선
# 1 -> 시작노드
# 1 2 2 -> a노드에서 b노드로 가는 비용이 c라는 의미
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2

import heapq # 힙 라이브러리

def dijkstra2(start):

    q = []

    # 시작노드로 가기위한 최단경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # 큐가 비어있지 않다면 계속 진행

        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        print('q :: ',q)
        dist, now = heapq.heappop(q) # heap에서 가장 작은 항목을 빼낸다!!!
        print('dist :: ',dist,' now :: ',now)

        #현재노드가 이미 처리된 적 있는 노드라면 무시
        print('distance[', now, '] :: ', distance[now])
        if distance[now] < dist:
            continue

        print('graph[',now,'] :: ',graph[now])
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            print('cost :: '+str(cost))

            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


dijkstra2(start)


for i in range(1, n+1):

    if distance[i] == INF:
        print('INFINITY') # 도달할 수 없는 경우, 무한이라고 출력
    else:
        print(distance[i])


