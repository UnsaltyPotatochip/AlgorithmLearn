# 2024-04-23 알고리즘 공부(Studying Algorithm)
# 병합정렬 구현해보기
size = int(input("size >>> "))
tmp = input(">>> ")
arr = list(map(int, tmp.split()))

print("\nBefore -> %s" % arr)

# 병합 연산
def merge(array1, array2):
    d1, d2 = 0, 0
    r_index = 0
    # 결과배열의 크기는 첫번째와 두번째 배열의 크기를 합친 것만큼 크다.
    result = [0 for _ in range(len(array1)+len(array2))]
    # 둘 중 한 배열에서 결과 배열에 추가할 원소가 없을 때까지 돈다.
    while d1 < len(array1) and d2 < len(array2):
        if array1[d1] < array2[d2]:
            result[r_index] = array1[d1]
            d1 += 1
        else:
            result[r_index] = array2[d2]
            d2 += 1
        r_index += 1
    # 루프가 끝나고 아직 원소가 남은 배열에서 추가시킨다.
    # 첫번째 배열이 아직 원소가 낭은 경우
    if d1 < len(array1):
        for i in range(d1, len(array1)):
            result[r_index] = array1[i]
            r_index += 1
    # 두번째 배열이 아직 원소가 남은 경우
    if d2 < len(array2):
        for i in range(d2, len(array2)):
            result[r_index] = array2[i]
            r_index += 1
    # 결과배열을 반환한다.
    return result

# 병합정렬
def merge_sort(array):
    # 배열의 크기가 1 이하라면 이미 정렬된 것으로 판단
    if len(array) <= 1: return array
    # 반으로 나눈 인덱스를 기준으로 좌 우로 나눠서 재귀적으로 병합정렬한다.
    part = len(array) // 2
    left = merge_sort(array[:part])
    right = merge_sort(array[part:])
    return merge(left, right)

print("After -> %s" % merge_sort(arr))