# 2024-04-17 알고리즘 공부(Studying Algorithm)
# 버블정렬 구현해보기
size = int(input("size >>> "))
tmp = input(">>> ")
arr = list(map(int, tmp.split()))

print("\nBefore -> %s" % arr)

def swap(front, second):
    buff = front
    front = second
    second = buff
    return front, second

flag = 0
block = size-1
for i in range(size):
    flag = 0
    for j in range(block):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = swap(arr[j], arr[j+1])
            flag += 1
    block -= 1
    if flag == 0:
        break

print("After -> %s" % arr)