
# Part2 Chapter08 다이나믹 프로그래밍

# 1. 다이나믹 프로그래밍

# 다이나믹 프로그래밍 : 동적 계획법
# ex. 탑다운과 보텀업 방식, 피보나치 수열


# 예제 8-1 피보나치 함수 소스코드 ( 재귀함수로 구현 )
# 아래 소스코드 시간복잡도 : O(2^n) -> x값이 증가할 수록 시간소요 매우 증가!

def fibo(x):

    if x == 1 or x== 2:
        return 1
    return fibo(x-1) + fibo(x-2)


# print(fibo(4))



# 위 소스 문제 해결하기
# 메모이제이션 : 메모리공간에 메모해두고 같은식을 호출하면 결과를 그대로 가져오는 기법
# 캐싱 : 메모이제이션 값 저장 방법


# 예제 8-2 피보나치 함수 소스코드 ( 재귀적 -> 탑다운 다이나믹 프로그래밍)
# 아래 소스코드 시간복잡도 : O(N)

# 한 번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
d = [0] * 100

def fibo2(x):

    # 호출 되는 함수
    print('f('+str(x)+')', end=' ')
    if x == 1 or x== 2:
        return 1

    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]

    d[x] = fibo2(x-1) + fibo2(x-2)

    return  d[x]


# 탑다운 방식 : 큰 문제를 해결하기 위해 작은 문제를 호출하는 방식 ( 하향식 )
# 보텀업 방식 : 작은 문제부터 차근차근 답을 도출하는 방식 ( 상향식 )

# print(fibo2(6))


#예제 8-4 피보나치 수열 소스코드 ( 반복적 : 보텀업 방식 )

# d2 = [0] * 100
#
# d2[1] = 1
# d2[2] = 1
# n = 99
#
# for i in range(3, n+1):
#
#     d2[i] = d2[i-1] + d2[i-2]
#
# print(d2[n])



# 2. 1로 만들기

# x가 5로 나누어 떨어지면 5로 나눈다
# x가 3으로 나누어 떨어지면 3로 나눈다으
# x가 2로 나누어 떨어지면 2로 나눈다
# x에서 1을 뺀다
# 위 내용을 이용하여, 임의의 숫자를 1로 연산하는 최솟값 구하기
# x = 26 ==> return 3

# x = int(input())
#
# d3 = [0] * 30001
#
# for i in range(2, x+1):
#
#     d3[i] = d3[i-1] +1
#
#     if i % 2 == 0:
#         d3[i] = min(d3[i], d3[i//2]+1)
#
#     if i % 3 == 0:
#         d3[i] = min(d3[i], d3[i//3]+1)
#
#     if i % 5 == 0:
#         d3[i] = min(d3[i], d3[i//5]+1)
#
#
# print(d3[x])




# 3. 개미전사

# 일직선상에 존재하는 식량창고 약탈하기
# 인접한 식량 약탈 불가 -> 1 3 1 5 -> 1과 3은 약탈 불가, 1과 1은 가능, 첫번째 1과 5도 가능

# ex) 1 3 1 5 -> 2번째와 4번째 식량약탈시 합계 : 8 -> 최대한 많이 약탈한 식량 값을 구하기

# n = int(input()) # 입력 식량 개수
#
# storage = list(map(int,input().split())) # 식량 정보 ==> 1 3 1 5 => [ 1,3,1,5 ]
#
# d4 = [0] * 100
#
# # 다이나믹 프로그래밍 진행 ( 보텀업 )
# d4[0] = storage[0]
# d4[1] = max(storage[0],storage[1])
#
# for i in range(2, n):
#     d4[i] = max(d4[i-1],d4[i-2]+storage[i])
#
# print(d4[n-1])





# 4. 바닥 공사

# 세로 길이가 2, 가로 길이가 N인 직사각형 형태의 바닥
# 1 * 2, 2 * 1, 2 * 2 덮게로 바닥 채우는 모든 경우의 수 구하기
# 바닥을 채우는 모든 방법의 수 : 796,796
# ex. 2 * 3인 바닥의 경우의 수는 5

# n = int(input()) # 2 * n 개의 바닥 n 입력
#
# d5 = [0] * 1001
#
# d5[1] = 1 # 2 * 1 인 바닥은 경우의 수 1
# d5[2] = 3 # 2 * 2 인 바닥은 경우의 수 3
#
# for i in range(3, n+1):
#     d5[i] = (d5[i-1]+2 * d5[i-2]) % 796796
#
# print(d5[n])




# 5. 효율적인 화폐 구성

# n가지 종류의 화폐, 화폐들의 개수를 최소한으로 이용해, 합이 m원이 되도록 하기
# ex) 2원, 3원, 합 15원 -> 최소 개수 : 3원 5개
# ex2) 3원 , 5원, 7원, 합 4원 -> 최소 개수 : -1 리턴

n, m = map(int,input().split()) # n=2 화폐종류, m=15 최소한으로 나타낼 금액합

array = [] # array = [ 2,3 ] 화폐 리스트

for i in range(n):
    array.append(int(input()))

d6 = [10001] * (m+1) # 금액합 크기만큼 10001 리스트 생성 [ 10001, 10001 ... 10001 ]

d6[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        if d6[j-array[i]] != 10001: # i-k 원을 만드는 방법이 존재하는 경우
            d6[j] = min(d6[j],d6[j-array[i]]+1)

if d6[m] == 10001: # 최종적으로 m원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d6[m])