
# Part2 Chapter03 그리디

# 탐욕적 알고리즘 : 현재 상황에서 지금 당장 좋은 것만 고르는 방법


# 3-1 거스름돈
# coin_type 순서대로 동전 갯수 카운트

def changeMoney(n):

    cnt = 0;

    coin_types = [500,100,50,10]

    for coin in coin_types:
        cnt += n // coin
        n %= coin

    return cnt

# print(changeMoney(1260))



# 3-2 큰 수의 법칙
# ex. 5 8 3
#     2 4 5 4 6
#     6+6+6+5+6+6+6+5 = 46

# n, m, k = map(int, input().split())
#
# data = list(map(int,input().split()))

def bigNumber(n,m,k,data):

    data.sort() #큰 수 정렬 내림차순
    first = data[n - 1] # 첫번째로 큰 수
    second = data[n - 2] # 두번째로 큰 수

    result = 0

    while True:
        for i in range(k):
            if m == 0:
                break
            result += first
            m -= 1
        if m == 0:
            break
        result += second
        m -= 1

    return result

# print(bigNumber(n,m,k,data))

# 가장 큰 수가 더해지는 횟수
# count = int(m / (k+1)) * k
# count += m % (k+1)
#
# data.sort()
# first = data[n - 1]
# second = data[n - 2]
#
# # 총합 구하기
# result = 0
# result += (count)* first # 첫번째 큰 수 카운트 합
# result += (m-count)* second # 두번째 큰 수 카운트 합
#
# print(result, count)


# 3-3 숫자카드게임
# 선택한 행에서 가장 낮은 수의 카드를 뽑을 때, 그 카드가 가장 큰 수인 값 찾기

# ex. 3 3
#     3 1 2 ( 가장 낮은 수 1 )
#     4 1 4 ( 가장 낮은 수 1 )
#     2 2 2 ( 가장 낮은 수 2 => 가장 낮은 수 중, 가장 큰 수 )
#     result = 2

# ex2. 2 4
#      7 3 1 8
#      3 3 3 4
#      result = 3

# n, m = map(int, input().split())

def numberCardGame(n,m):

    result = 0;

    for i in range(n):
        data = list(map(int,input().split()))

        min_value = min(data)

        result = max(result,min_value)

    return result

# print(numberCardGame(n,m))


# 3-4 1이 될 때 까지
# 1. N-1
# 2. N/K
# 위 순서를 이용하여, 1이 되는 횟수
# 25 5 -> 25/5 (1) -> 5/5 (2) -> 1
# resulit = 2

n, k = map(int, input().split())

def numberOneMinCnt(n,k):

    result = 0
    while n >= k:

        while n % k != 0:
            n -= 1
            result += 1

        n //= k
        result += 1

    # k값으로 나눠지지않는 마지막으로 남은 수에 대하여 1씩 차감
    while n > 1:
        n -= 1
        result += 1

    return result


# print(numberOneMinCnt(n,k))

def numberOneMinCnt2(n,k):

    result = 0

    while True:

        target = (n//k)*k # // -> 몫, % -> 나머지
        result += (n-target) #4 -> n 이 1이되면 target은 0 이라 기존 횟수에 1추가
        n = target # n이 1일 시에, target은 0이므로 n은 0으로 초기화

        if n < k:
            break

        result += 1 #5
        n //=k


    result += (n-1)
    return result


print(numberOneMinCnt2(n,k))