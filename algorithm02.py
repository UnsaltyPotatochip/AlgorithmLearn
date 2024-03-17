# 2024-03-18 알고리즘 공부(Studying Algorithm)
# 원문 코드 출처 : 인프런 'Do it! 알고리즘 코딩 테스트 with Python'
import random

testcase = int(input())
answer = 0
A = [0] * (100001)

# 인덱스 범위오류, A라는 배열 크기가 100001로 지정되있지만, 정작 배열 안에 수를 넣을때는 0부터 10000까지만 정의됨
# for i in range(0, 100001):
for i in range(0, 10001):
    A[i] = random.randrange(1, 101)

for t in range(1, testcase+1):
    start, end = map(int, input().split())

    for i in range(start, end+1):
        answer = answer + A[i]

    # 변수초기화 오류, 각 테스트 케이스 끝날때마다 answer의 값이 초기화 되야하는데 초기화가 안되있음
    # answer = 0

    # 잘못된 변수 사용 오류, 몇번째 케이스인지와 그 케이스의 답이 같이 출력되어야 하는데 t 변수를 사용하는 것이 아닌 testcase 변수를 사용함
    # 파이썬 자동 형변환 오류, answer/2를 했을때 파이썬은 자동으로 이를 float으로 처리하므로, 실수 형태로 출력되게 된다.
    # print(str(t)) + "" + str(answer//2))
    print(str(testcase) + "" + str(answer/2))