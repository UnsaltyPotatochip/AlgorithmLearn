# 2024-05-02 알고리즘 공부
# 깊이우선탐색(DFS) 구현해보기

# 인접그래프
graph = {
    1 : [2, 3],
    2 : [4, 5],
    3 : [],
    4 : [6, 7],
    5 : [],
    6 : [],
    7 : []
}
# 노드 탐색 여부용 배열
check = [0, 0, 0, 0, 0, 0, 0]
# 스택
stack = []
def pop_print(node):
    tmp = node
    stack.pop()
    print(tmp, end=' ')

# DFS 재귀함수
# 스택 배열을 사용하게끔 함수를 수정하자
def DFS(node):
    stack.append(node)
    if check[node - 1] == 0:
        pop_print(node)
        check[node - 1] = 1
        for i in graph[node]:
            if check[i-1] == 0:
                DFS(i)

# 결과
DFS(1)