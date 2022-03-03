# Part2 Chapter04 구현

# 1. 아이디어를 코드로 바꾸는 구현

# 예제 4-1 상하좌우
# N * N 평면 지도에서 명령어로 여행가의 도착지점 출력하기
# 명령어 종류 : L - 왼쪽, R - 오른쪽, U - 위, D - 아래

# n = int(input())
# plans = input().split()


def findArrivePoint(n,plans):
    x, y = 1, 1  # start

    # 0,-1 좌, 0,1 우, -1,0 상, 1,0 하
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    move_types = ['L','R','U','D']

    for plan in plans:

        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > n or ny > n: # if문 범위 초과하면, 초과값 이전 도착지점을 호출 ( 벽에 막혀서 못가는 구조 )
            continue

        x,y = nx, ny

    return x,y


# print(findArrivePoint(n,plans))


# 예제 4-2 시각
# 00시 00분 00초 ~ n시 59분 59초까지 '3'이 들어간 경우의 수 찾기
# 60 * 60 * 24 하루 = 86400

# h = int(input())

def findTimeNumber3(h):

    count = 0

    for i in range(h+1):
        for j in range(60):
            for k in range(60):

                if '3' in str(i)+str(j)+str(k):
                    count += 1

    return count


# print(findTimeNumber3(h))

# 2. 왕실의 나이트

# 나이트의 이동경로 경우의 수
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# input_data = input()
# row = int(input_data[1])

# ord() : 문자를 아스키코드로 A -> 65
# chr() : 아스키코드를 문자로 65 -> A

# column = int(ord(input_data[0])) - int(ord('a')) +1

def knightMove(row,column,steps):

    result = 0

    for step in steps:

        next_row = row + step[0]
        next_col = column + step[1]

        if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
            result +=1

    return result

# print(knightMove(row,column,steps))


# 3. 게임 개발


# 캐릭터 회전방향 0 : 북, 1 : 동. 2 : 남, 3 : 서

# 맵 지형 0 : 육지 , 1: 바다

# n, m = map(int, input().split())


# 왼쪽으로 회전
def turn_left(direction):
    direction -=1
    if direction == -1:
        direction = 3

    return direction


def simulationMove(n,m):

    # 방문위치를 저장하기 위해 맵을 생성하여, 0으로 초기화 ( 리스트 내포 방법 )
    d = [[0] * m for _ in range(n)]

    # 현재 캐릭터의 X좌표, Y좌표, 방향을 입력받기
    x, y, direction = map(int, input().split())
    d[x][y] = 1  # 현재 좌표 방문처리

    # 전체 맵 정도를 입력받기
    array = []
    for i in range(n):
        array.append(list(map(int, input().split())))

    # 북, 동, 남, 서 방향 정의

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    count = 1
    turn_time = 0

    while True:

        direction = turn_left(direction)

        nx = x + dx[direction]
        ny = y + dy[direction]

        # 회전 후, 정면에 가보지않은 칸이 존재하는 경우 이동
        if d[nx][ny] == 0 and array[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue

        # 회전한 이후에 정면에 가보지않은 칸이 없거나 바다인 경우
        else:
            turn_time += 1

        # 네 방향 모두 갈 수 없는 경우

        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]

            # 뒤로 갈 수 있다면 이동하기

            if array[nx][ny] == 0:
                x = nx
                y = ny

            else:
                break
            turn_time = 0

    return count


# print(simulationMove(n,m))