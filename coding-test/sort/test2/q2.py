# 위에서 아래로
arr = [1, 15, 27, 12, 99, 20, 30]
result = arr
for i, n in enumerate(arr):
    pivot = n
    for j, m in enumerate(arr):
        if pivot > m:
            arr[i], arr[j] = m, pivot
            pivot = m

print(arr)

# 성적이 낮은 순서로 학생 출력하기
