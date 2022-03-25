
# 14657번 준오는 최종인재야!

# 해커 준오가 최대한 많은 문제를 푸는데 걸리는 최소 날짜 수를 출력!

# DFS 방식으로 처리
# DFS : 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘


# 예제 입력1
# 6 4  -> 문제의 수 N  하루 풀이 시간 T
# 1 2 4 -> A B C -> A와 B는 서로 연결된 문제, C는 A를 풀고 B를 풀거나, B를 풀고 A를 푸는데 걸리는 시간
# 2 3 2
# 3 4 7
# 3 5 3
# 6 5 4

#예제 출력1
# 4


n, t = map(int, input().split())

graph = []

visited = [False] * n

for i in range(n):
    graph.append(list(map(int,input().split())))


def quiz(n,t,v,graph):

    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            quiz(graph, i ,visited)


