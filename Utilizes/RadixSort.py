# 2024-04-29 알고리즘 공부(Studying Algorithm)
# 기수정렬 구현해보기
size = int(input("size >>> "))
tmp = input(">>> ")
arr = list(map(int, tmp.split()))

print("\nBefore -> %s" % arr)

# 큐에서 가장 먼저 들어온 데이터를 내보내는 연산
def popleft(array):
    res = array[0]
    array.remove(array[0])
    return res

k = len(str(max(arr)))
queue = [[] for _ in range(10)]

# 자릿수를 가리키는 제어변수 i
# 일의 자리부터 k번째 자리까지 탐색한다.
for i in range(k):
    # arr을 전부 탐색하는 제어변수 j
    for j in range(size):
        # 현재 자릿수에 해당하는 숫자를 추출하여 해당하는 큐에 추가
        digit = (arr[j] // (10 ** i)) % 10
        queue[digit].append(arr[j])
    # 원본 배열을 다시 정렬하기 위해 초기화 시킨다.
    arr = []
    # queue에 저장된 데이터를 arr에 옮김
    for n in range(10):
        while len(queue[n]) != 0:
            arr.append(popleft(queue[n]))

print("After -> %s" % arr)