
# Part2 Chapter07 이진탐색

# 1. 범위를 반씩 좁혀가는 탐색

# 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

# 예제 7-1 순차탐색

def sequential_search(n, target, array):

    for i in range(n):

        if array[i] == target:
            return i+1



# print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
#
# input_data = input().split()
# n = int(input_data[0])
# target = input_data[1]
#
# print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
#
# array = input().split()
#
# #순차 탐색 수행 결과 출력 ( 시간복잡도 O(N) )
# print(sequential_search(n,target,array))



# 이진탐색 : 이미 정렬 상태인 데이터 목록에서 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교

# 예제 7-2 재귀함수로 구현한 이진 탐색 소스코드

def binary_search(array, target, start ,end):

    if start > end:
        return None

    mid = (start+end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)

    else:
        return  binary_search(array,target,mid+1,end)


# n (원소의 개수)과 target (찾고자 하는 문자열)을 입력받기 ( 시간복잡도 O(logN) )
# n, target = list(map(int,input().split()))
#
# array = list(map(int,input().split()))
#
#
# result = binary_search(array,target,0,n-1)
#
# if result == None:
#     print('원소가 존재하지 않습니다.')
# else:
#     print(result+1)


# 예제 7-3 반복문으로 구현한 이진 탐색 소스코드

def binary_search2(array,target,start,end):

    while start <= end:
        mid = (start+end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid -1

        else:
            start = mid +1

    return None


# n (원소의 개수)과 target (찾고자 하는 문자열)을 입력받기 ( 시간복잡도 O(logN) )
# n, target = list(map(int,input().split()))
#
# array = list(map(int,input().split()))
#
#
# result = binary_search(array,target,0,n-1)
#
# if result == None:
#     print('원소가 존재하지 않습니다.')
# else:
#     print(result+1)


# 예제 7-4 한 줄 입력받아 출력하는 소스코드

import sys

# input_data = sys.stdin.readline().rstrip() # rstrip : 줄바꿈 공백 제거

# print(input_data)


# 2. 부품 찾기

# N = 5 [ 8, 3, 7, 9, 2 ] 상점 부품정보
# M = 3 [ 5 , 7 , 9 ] 손님 요구 부품정보
# 결과 no, yes, yes

# 위 binary_search2 함수를 이용한다!

# n = int(input())
#
# array = list(map(int,input().split()))
# array.sort()
#
# m = int(input())
# x = list(map(int,input().split()))
#
#
# for i in x:
#
#     result = binary_search2(array, i, 0, n-1)
#     if result != None:
#         print('YES',end=' ')
#     else:
#         print('NO',end=' ')



# 게수 정렬 이용

# n = int(input())
# array = [0] * 1000001
#
# for i in input().split():
#     array[int(i)] = 1
#
# m = int(input())
# x = list(map(int,input().split()))
#
# for i in x:
#     if array[i] == 1:
#         print('YES',end=' ')
#     else:
#         print('NO', end=' ')


# 집합 자료형 이용

# n = int(input())
# array = set(map(int,input().split()))
#
# m = int(input())
# x = list(map(int,input().split()))
#
# for i in x:
#     if i in array:
#         print('YES',end=' ')
#     else:
#         print('NO', end=' ')



# 3. 떡볶이 떡 만들기

# 파라메트릭 서치 : 최적화 문제를 결정 문제로 바꾸어 해결하는 기법

n, m = list(map(int, input().split()))

array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while(start <= end):
    total = 0
    mid = (start+end) // 2
    for x in array:

        # 잘랐을 때 떡양 계산
        if x > mid:
            total += x - mid

    # 떡의 양이 부족한 경우 더 많이 자르기
    if total < m:
        end = mid -1

    # 떡의 양이 충분한 경우 덜 자르기
    else:
        result = mid #최대한 덜 잘랐을 때가 정답이므로, 여기에서 result 기록
        start = mid +1

print(result)