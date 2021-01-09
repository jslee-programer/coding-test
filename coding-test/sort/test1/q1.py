# 선택 정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(arr)):
    min_index = i
    # print(i)
    for j in range(i + 1, len(arr)):
        # print(j)
        if arr[min_index] > arr[j]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print('선택정렬', arr)

# 삽입 정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(arr)):
    for j in range(i, 0, -1):  # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if arr[j] < arr[j - 1]:  # 한 칸씩 인쪽으로 이동
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else:
            break

print('삽입정렬', arr)

# 퀵정렬

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]

        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(arr, 0, len(arr) - 1)
print('퀵정렬', arr)
