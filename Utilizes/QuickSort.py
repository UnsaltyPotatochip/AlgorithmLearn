# 2024-04-21 알고리즘 공부(Studying Algorithm)
# 퀵정렬 구현해보기
size = int(input("size >>> "))
tmp = input(">>> ")
arr = list(map(int, tmp.split()))

print("\nBefore -> %s" % arr)

# 따로 swap 함수를 만들지 않아도, 파이썬에서는 언패킹이 가능하므로 단순 값교환이 가능하다.
# 따로 배열을 return 하지않아도 원본 배열을 직접 수정하므로 괜찮다.

def quick_sort(array, start, end):
    # 종료 조건
    if start < end:
        # pivot 설정
        pivot = array[end]
        # pivot보다 작은 영역을 추려낼 인덱스
        s_index = start - 1

        for i in range(start, end):
            # 현재 요소가 pivot보다 작거나 같을때
            if arr[i] <= pivot:
                s_index += 1
                # swap
                array[s_index], array[i] = array[i], array[s_index]

        # pivot을 적절한 위치로 갖고오기
        array[s_index+1], array[end] = array[end], array[s_index+1]

        # pivot을 기준으로 분할하여 재귀함수 호출
        quick_sort(array, start, s_index)
        quick_sort(array, s_index+2, end)


quick_sort(arr, 0, size-1)
print("After -> %s" % arr)