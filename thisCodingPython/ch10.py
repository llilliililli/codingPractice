# Part2 Chapter10 그래프 이론

# 1. 서로소 집합
# 공통 원소가 없는 두 집합
# ex. { 1, 2 } , { 3, 4 } => 서로소 관계
#     { 1, 2 } , { 2, 3 } => 서로소 관계가 아니다

# 10-1. 기본적인 서로소 집합 알고리즘 소스코드
# 입력 예시
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6

# 출력 예시
# 각 원소가 속한 집합 : 1 1 1 1 5 5 -> 1~6까지 원소의 루트노드 ( { 1,2,3,4 } , { 5,6 } 으로 나뉨 )
# 부모 테이블 : 1 1 2 1 5 5 ->

def find_parent(parent,x):

    # 루트노드가 아니라면, 루트노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int,input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

#각 원소가 속한 집합 출력
print('각 원소가 속한 집합 : ', end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')

print()

#부모 테이블 내용 출력
print('부모 테이블 : ', end='')
for i in range(1,v+1):
    print(parent[i],end=' ')




# 10-2. 경로 압축기법 소스코드
def find_parent2(parent,x):

    # 루트노드가 아니라면, 루트노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent2(parent,parent[x])
    return parent[x]




# 10-3. 개선된 서로소 집합 알고리즘 소스코드
# 10-2. 경로 압축기법 소스코드 find_parent2 이용하여, 서로소 집합 구하기

# 두 원소가 속한 집합을 합치기
def union_parent2(parent,a,b):
    a = find_parent2(parent,a)
    b = find_parent2(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int,input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a,b = map(int,input().split())
    union_parent2(parent,a,b)

#각 원소가 속한 집합 출력
print('각 원소가 속한 집합 : ', end='')
for i in range(1,v+1):
    print(find_parent2(parent,i),end=' ')

print()

#부모 테이블 내용 출력
print('부모 테이블 : ', end='')
for i in range(1,v+1):
    print(parent[i],end=' ')





# 10-4. 서로소 집합을 활용한 사이클 판별 소스코드
# 입력 예시
# 3 3
# 1 2
# 1 3
# 2 3

# 출력 예시
# 사이클이 발생했습니다.

#특정 원소가 속한 집합을 찾기
def find_parent3(parent,x):

    # 루트노드가 아니라면, 루트노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent3(parent,parent[x])
    return parent[x]



# 두 원소가 속한 집합을 합치기
def union_parent3(parent,a,b):
    a = find_parent3(parent,a)
    b = find_parent3(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int,input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i


cycle = False # 사이클 발생 여부

for i in range(e):
    a,b = map(int,input().split())

    # 사이클이 발생한 경우 종료
    if find_parent3(parent,a) == find_parent3(parent,b):
        cycle = True
        break

    # 사이클이 발생하지 않았다면 합집합(union) 수행
    else:
        union_parent3(parent,a,b)


    if cycle:
        print('사이클이 발생했습니다.')
    else:
        print('사이클이 발생하지 않았습니다.')