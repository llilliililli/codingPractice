
# Part2 Chapter06 정렬

# 1. 기준에 따라 데이터를 정렬

# 정렬 : 데이터를 특정한 기준에 따라서 순서대로 나열

# 종류 : 선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬 등


# 선택정렬
# 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두번째 데이터와 바꾸는과정 반복

# 예제 6-1 선택정렬

array = [7,5,9,0,3,1,6,2,4,8]

# for i in range(len(array)):
#     min_index = i
#     for j in range(i+1,len(array)):
#
#         if array[min_index] > array[j]:
#             min_index = j
#
#     array[i], array[min_index] = array[min_index], array[i] # 스와프
#
#
# print(array)


# 삽입정렬
# 특정한 데이터를 적절한 위치에 삽입한다
# ( 정렬되어있는 상태의 경우 더욱 빠르게 동작 )

# 예제 6-3 삽입정렬

# array = [7,5,9,0,3,1,6,2,4,8]

# for i in range(1,len(array)):
#     for j in range(i,0,-1): # 인덱스 i부터 1까지 감소하면서 반복
#         if array[j] < array[j-1]:
#             array[j],array[j-1] = array[j-1],array[j] #스와프
#         else:
#             break
#
#
# print(array)


# 퀵 정렬
# 기준 데이터를 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작
# 큰 수와 작은 수를 교환하기 위한 기준 : 피벗
# 피벗 기준으로 피벗값보다 큰 수 모음과 피벗값보다 작은 수 모음으로 리스트 영역을 나눈다
# 분할 방식 : 호어 분할 방식 - 리스트에서 첫번째 데이터를 피벗으로 정한다.

# 에제 6-4 퀵정렬

array2 = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):

    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:

        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1 # 피벗보다 작다면 다음 인덱스로 이동

        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1 # 피벗보다 크다면 다음 인덱스로 이동

        # 엇갈렷다면 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은데이터와 큰데이터를 교체
        else:
            array[left],array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)


# quick_sort(array2,0,len(array2)-1)
# print(array2)


# 파이썬 장점을 살린 퀵정렬

def quick_sort2(array):

    # 리스트가 하나이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot ] # 분할된 왼쪽부분
    right_side = [x for x in tail if x > pivot ] # 분할된 오른쪽부분

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

# print(quick_sort2(array2))


# 계수 정렬
# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘

# 예제 6-6 계수 정렬

array3 = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
#
# count = [0] * (max(array3) + 1)
#
# for i in range(len(array3)):
#     count[array3[i]] += 1
#
# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end=' ')


# 파이썬 정렬 라이브러리

# 파이썬 기본정렬 라이브러리 sorted() : 퀵정렬과 비슷한 병합정렬 기반

# 예제 6-7 sorted
array4 = [7,5,9,0,3,1,6,2,4,8]

# result = sorted(array4)
# print(result)

# 예제 6-8 리스트 객체 내장함수 sort()

# array4.sort()
# print(array4)

# 예제 6-9 정렬 라이브러리 key 활용한 소스코드

array5 = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

# sorted 함수에 key 매개변수를 이용하여, 딕셔너리 키로 정렬
# result = sorted(array5,key=setting)
# print(result)

# 2. 위에서 아래로

# 큰 수에서 작은 수로 내림차순 정렬
# n = 3  입력 숫자 개수
# array = [ 15, 27, 12 ] 입력숫자 리스트

# n = int(input())
#
# array = []
# for i in range(n):
#     array.append(int(input()))
#
#
# array = sorted(array, reverse=True) # reverse = True : 내림차순
#
# for i in array:
#     print(i,end=' ')



# 3. 성적이 낮은 순서로 학생 출력하기

# 학생이름과 성적 주어졌을 때, 성적이 낮은 순으로 학생이름 출력
# n = 2 입력 학생정보 개수
# 홍길동 95 , 이순신 77
# [ (홍길동,95) (이순신,77) ] 입력학생정보 리스트

# n = int(input())
#
# array = []
#
# for i in range(n):
#     input_data = input().split()
#
#     array.append((input_data[0],input_data[1]))
#
#
# array = sorted(array,key=lambda student : student[1]) # 키를 이용하여, 점수기준으로 정렬
#
#
# for i in array:
#     print(i[0],end=' ')


# 4. 두 배열의 원소 교체

# A,B 두 배열, 모두 자연수, K번 바꿔치기 가능 ( A,B 서로 교환 )
# A의 원소합이 최대가 되도록 하는것이 목표

# A = [1,2,5,4,3] , B=[5,5,6,6,5], K=3 => A = [6,6,5,4,5] => SUM(A) => 26

# n,k = map(int,input().split())  # n = 5 개의 원소, k번 바꿔치기 가능
# a = list(map(int,input().split())) # A 배열
# b = list(map(int,input().split())) # B 배열
#
# a.sort() # [ 1,2,3,4,5 ]
# b.sort(reverse=True) # B배열 내림차순으로 정렬 [ 6,6,5,5,5 ]
#
# for i in range(k):
#     if a[i] < b[i]:
#         a[i],b[i] = b[i],a[i] # 스와프
#     else:
#         break
#
# print(sum(a)) # 바꿔치기 정렬된 A 리스트 합산