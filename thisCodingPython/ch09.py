
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
# INF = int(1e9) # 무한값을 의미 : 10억으로 설정
#
# # 노드 개수, 간선 개수 입력
# n,m = map(int,input().split())
#
# #시작 노드
# start = int(input())
#
# # 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트
# graph = [[] for i in range(n+1)]
#
#
# # 모든 간선 정보를 입력받기
# for _ in range(m):
#     a, b, c = map(int, input().split()) # a노드에서 b노드로 가는 비용이 c라는 의미
#     graph[a].append((b,c))
#
# print(graph)
# graph
# [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]

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

def dijkstra2(start,n):

    q = []

    # 방문 이력 리스트
    visited = [False] * (n+1)

    # 최단 거리 테이블 모두 무한으로 초기화
    distance = [INF] * (n+1)

    # 시작노드로 가기위한 최단경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # 큐가 비어있지 않다면 계속 진행

        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        print('q :: ',q)
        dist, now = heapq.heappop(q) # heap에서 가장 작은 항목을 빼낸다!!!
        #print('dist :: ',dist,' now :: ',now)

        #현재노드가 이미 처리된 적 있는 노드라면 무시
        #print('distance[', now, '] :: ', distance[now])
        if distance[now] < dist:
            continue

        #print('graph[',now,'] :: ',graph[now])
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #print('cost :: '+str(cost))

            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


# dijkstra2(start,n)
#
#
# for i in range(1, n+1):
#
#     if distance[i] == INF:
#         print('INFINITY') # 도달할 수 없는 경우, 무한이라고 출력
#     else:
#         print(distance[i])


# 플로이드 워셜 알고리즘
# 2차원 리스트 "최단거리" 정보 저장 ( 다익스트라는 1차원 ) --> 다른 모든 노드로 가는 최단거리 정보를 담아야 하기 때문
# 플로이드 => 다이나믹 프로그래밍 방식, 다익스트라 => 그리디

# 4 노드개수
# 7 간선 개수
# graph
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2


INF = int(1e9)

n = int(input()) # 노드 개수
m = int(input()) # 간선 개수

graph = [[INF]*(n+1) for _ in range(n+1)] # 2차원 리스트 ( 그래프 생성 및 모든값 무한으로 초기화 )
#print(graph)

# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for a in range(1,n+1):
    for b in range(1, n+1):
        if a==b :
            graph[a][b] = 0



# 각 간선 정보 입력 받아 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c


print(graph)
#[ [1000000000, 1000000000, 1000000000, 100000000, 1000000000],
# [1000000000, 0, 4, 1000000000, 6], # 0 => 1번노드 자기자신 비용, 4 => 2번노드까지 비용, 6 => 4번노드까지 비용
# [1000000000, 3, 0, 7, 1000000000],
# [1000000000, 5, 1000000000, 0, 4],
# [1000000000, 1000000000, 1000000000, 2, 0] ]

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


# 수행된 결과 출력
for a in range(1, n+1):
    for b in range(1,n+1):

        if graph[a][b] == INF:
            #도달할 수 없는 경우 INFINITY 출력
            print("INFINITY", end=" ")
        else:
            # 도달할 수 있는 경우 거리 출력 ( 노드 4개인 경우, 모든 노드로 가는 최단거리 값 출력 )
            print(graph[a][b],end=" ")
            # 0 4 8 6 3 0 7 9 5 9 0 4 7 11 2 0
            # 모든 노드 최단 거리 출력
            # 0 4 8 6 #  4: 1번에서 2번까지 최단거리, 8: 1번에서 3번까지 최단거리, 6: 1번에서 4번까지 최단거리
            # 3 0 7 9
            # 5 9 0 4
            # 7 11 2 0


# 2. 미래 도시

# 방문판매원 A가 회사 개수가 N개 일 때, K번 회사를 거쳐서 X번 회사를 가는 최소 이동시간 꾸하기
# 간석 개수 7개
# (1번, 2번), (1번, 3번), (1번, 4번), (2번, 4번), (3번, 4번), (3번, 5번), (4번, 5번)
#  1번 -> 3번 -> 5번 -> 4번 순으로 총 3만큼 시간 이동할 수 있다.

# 입력 예시
# 5 7 -> 회사개수, 간선개수
# 1 2 -> K -> X 이동 루트
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5


