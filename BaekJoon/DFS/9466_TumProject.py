# 9466번 텀 프로젝트

# 문재해결 강의를 수강 학생들은 텀프로젝트를 수행해야한다. 모든 학생들이 프로젝트를 같이하고 싶은 학생을 선택하도록 하고,
# 최종적으로 어느팀에도 속하지않는 학생들의 수를 계산하는 프로그램 구현

# 1 2 3 4 5 6 7 -> 학생번호
# 3 1 3 7 3 4 6 -> 해당 번호 학생이 팀하고 싶은 번호의 학생 ( 자기자신을 택해도 팀구성 성립 )
# 팀구성 성공한 학생번호
# 3, 4,7,6( 4,7,6은 사이클형식으로 연결됨 )
# 팀구성 실패한 학생번호
# 1,2,5

# DFS 방식으로 처리
# DFS : 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘


# 예제 입력1
# 2 -> 테스트 케이스 ( 7번, 8번 2케이스 )
# 7 -> 테스트 1케이스, 학생들의 번호 ( 1~ n : 7 )
# 3 1 3 7 3 4 6 -> 번호순대로 원하는 학생들 표현
# 8 -> 테스트 2케이스, 학생들의 번호 ( 1~ n : 8 )
# 1 2 3 4 5 6 7 8


#예제 출력1
# 3 -> 테스트 1케이스 출력 ( 3명의 학생 팀구성 실패 )
# 0 -> 테스트 2케이스 출력 ( 모든 학생 팀구성 성공 )

