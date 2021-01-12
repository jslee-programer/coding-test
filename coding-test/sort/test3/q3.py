# 두 배열의 원소 교체


def solution(k, li1, li2):
    limit = len(li1)
    array1 = sorted(li1, reverse=True)
    array2 = sorted(li2, reverse=True)
    result_ = array1[:limit - k] + array2[:k]
    result = sum(result_)
    print(result)


k = 3
arr1_ = [1, 2, 5, 4, 3, 7, 1, 2]
arr2_ = [5, 5, 6, 6, 5, 3, 2, 8]

solution(k, arr1_, arr2_)

k = 2
arr1_ = [1, 2, 5, 4, 3]
arr2_ = [5, 5, 6, 6, 5]

solution(k, arr1_, arr2_)
