# 2024-04-19 알고리즘 공부(Studying Algorithm)
# 삽입정렬 구현해보기
size = int(input("size >>> "))
tmp = input(">>> ")
arr = list(map(int, tmp.split()))

print("\nBefore -> %s" % arr)

# recursion ver.
def binary_search(array, select, buff):
    if array[select] < array[buff]:
        if array[buff] > array[select] >= array[buff - 1]: return buff
        return binary_search(array, select, buff // 2)
    elif array[select] > array[buff]:
        if array[buff] < array[select] <= array[buff + 1]: return buff + 1
        return binary_search(array, select, (select + buff) // 2)
    else:
        return buff

# loop ver.
# def binary_search(array, select):
#     buff = select // 2
#     f = 0
#     while True:
#         if array[buff] > array[select] >= array[buff - 1]:
#             break
#         if array[buff] < array[select] <= array[buff + 1]:
#             f = 1
#             break
#         if array[select] < array[buff]: buff //= 2
#         elif array[select] > array[buff]: buff = (select + buff) // 2
#         else: break
#     if f == 1:
#         return buff+1
#     else:
#         return buff

index = 0
flag = 0
for i in range(size):
    # 처음은 패스
    if i == 0:
        index += 1
        continue
    # 삽입 위치 탐색
    flag = binary_search(arr, index, index//2)
    # shift 연산
    buffer = arr[index]
    for j in range(index, flag-1, -1):
        arr[j] = arr[j-1]
    arr[flag] = buffer
    index += 1

print("After -> %s" % arr)