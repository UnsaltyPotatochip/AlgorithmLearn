# 2024-04-19 알고리즘 공부(Studying Algorithm)
# 삽입정렬에 활용할 인덱스를 리턴하는 이진탐색 함수

# recursion
def binary_search_recurs(arr, index, buff):
    if arr[index] < arr[buff]:
        if arr[buff] > arr[index] >= arr[buff-1]: return buff
        return binary_search_recurs(arr, index, buff//2)
    elif arr[index] > arr[buff]:
        if arr[buff] < arr[index] <= arr[buff+1]: return buff+1
        return binary_search_recurs(arr, index, (index+buff)//2)
    else:
        return buff

# loop
def binary_search_loop(arr, index):
    buff = index//2
    flag = 0
    while True:
        if arr[buff] > arr[index] >= arr[buff - 1]:
            break
        if arr[buff] < arr[index] <= arr[buff + 1]:
            flag = 1
            break
        if arr[index] < arr[buff]: buff //= 2
        elif arr[index] > arr[buff]: buff = (index+buff)//2
        else: break
    if flag == 1:
        return buff+1
    else:
        return buff

# result
array = [10, 20, 30, 40, 50, 60, 26]
print(array)

# testcase
print(array[binary_search_recurs(array, len(array)-1, (len(array)-1)//2)])
print(array[binary_search_loop(array, len(array)-1)])

# 삽입정렬에서 적절한 삽입위치를 탐색할 때 이진탐색 등과 같은 탐색 알고리즘을 사용하면
# 탐색시 발생하는 시간복잡도를 O(N)에서 O(logN)으로 줄일 수 있다.

# 이진탐색 알고리즘은 재귀함수든지, 반복문 방식이든지 시간복잡도가 O(logN)으로 동일하므로
# 공간복잡도에서 효율적인 반복문 방식이 비교적 효율적인 방식이다.