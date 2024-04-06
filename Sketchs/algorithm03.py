# 2024-04-06 알고리즘 공부(Studying Algorithm)
# 백준 11660 - 구간 합 구하기 5
# 일일이 계산하는 것보다 합배열로 구하는 것이 효율적이다.
import sys
input = sys.stdin.readline
# 시간초과 방지, 반복문으로 여러줄을 빠르게 입력 받기 위함

n, m = map(int, input().split())
# n : 리스트의 크기, m : 질의 수 -> 두 변수를 정수로 입력받는다.
A = [[0] * (n+1)]
# 단일 행을 가진 2차원 배열 - 원본배열
D = [[0] * (n+1) for k in range(n+1)]
# n+1개의 행을 가진 2차원 배열 - 합배열
# 원본 배열과 합배열을 정의해준다.

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    # 0을 맨 앞에 붙이고, 그 뒤에 정수들을 입력받아서 원소로 넣는다.
    A.append(A_row)
    # 위 리스트를 원본배열의 하나의 열로 추가한다.

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
        # 합배열 만드는 공식으로 합배열을 만든다.

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    # 질의에 대한 답을 result에 할당해준다, 합배열로 결과를 계산해준다.
    print(result)