
# 회의실 배정

# 탐욕적 알고리즘 : 현재 상황에서 지금 당장 좋은 것만 고르는 방법

# ex. 1개의 회의실, N개의 회의
# 회의시작시간 , 회의끝나는시간
# 회의 겹치지 않게 하면서, 회의실을 사용할 수 있는 회의의 최대 개수 찾기
# 회의 시작 , 끝 시간 겹쳐도 상관 없음


# 예제 입력
# 11 --> 최대 회의 개수
# 1 4 --> 회의 시작 시간 / 회의 끝 시간
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14

# 예제 출력
# 4 --> 4개의 회의만 사용 가능
# Hint : (1,4), (5,7), (8,11), (12,14) 회의 사용가능

# 미팅숫자
m = int(input())

data =[]

for i in range(m):
    data.append(list(map(int, input().split())))


def meetingRoomSchedule(data):

    cnt = 0
    result = 0

    timeChk = None

    data.sort()

    for i in range(0,len(data)):

        for j in range(i+1,len(data)):

            start = data[i][0]
            startN = data[j][0]
            end = data[i][1]
            endN = data[j][1]

            if timeChk != None :
                if timeChk[0] < startN and timeChk[1] <= startN and timeChk[1] != 0:
                    print('timeChk')
                    print(timeChk)
                    print(data[j])
                    cnt += 1

            elif  start < startN and end <= startN and timeChk == None:
                print('cnt')
                print(data[i])
                print(data[j])

                timeChk = data[j]
                cnt += 1

        if result < cnt:
            result = cnt
            cnt = 0
            timeChk = None
            print('result')
            print(result)

    return result



print(meetingRoomSchedule(data))