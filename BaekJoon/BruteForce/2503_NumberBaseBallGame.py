
# 숫자야구

# 브루트 포스 ( 완전 탐색 ) 문제

# 1~9까지 서로 다른 숫자 세 개로 구성

# ex. 영수 324

#민혁: 123
#영수: 1 스트라이크 1 볼.
#민혁: 356
#영수: 1 스트라이크 0 볼.
#민혁: 327
#영수: 2 스트라이크 0 볼.
#민혁: 489
#영수: 0 스트라이크 1 볼.

# 이때 가능한 답은 324와 328, 총 2 가지

# 가능한 답 갯수 찾는 알고리즘 구현 진행

# 예제 입력
#4  --> 민혁 정답도전 갯수
#123 1 1 --> 정답값 스트라이크 볼
#356 1 0
#327 2 0
#489 0 1

# 예제 출력
# 2 --> 324, 328 2가지

import itertools

# 정답 도전 횟수
q = int(input())
data = []

for i in range(q):
    data.append(list(map(int, input().split())))



def baseball_fun(x,y):
    x = list(x); y = list(y)
    s = 0; b=0

    for i in range(3):
        if x[i] in y:
            if y.index(x[i]) == i: s+=1
            else : b += 1
    return [s,b]

def NumberBaseBallGame(data):

    cnt = 0

    v = list(map(lambda x: str(x[0]), data))
    r = list(map(lambda x: [x[1],x[2]],data))

    print(v)
    print(r)

    allCase = list(itertools.permutations(range(1, 10), 3))
    allCase = list(map(lambda x: list(map(str, x)), allCase))
    print(allCase)

    for x in allCase:

        if [baseball_fun(x,y) for y in v ] == r: cnt+=1

    return cnt


print(NumberBaseBallGame(q,data))

