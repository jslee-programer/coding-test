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
info = {
    '성적순': 10,
    '홍길동': 95,
    '이순신': 77,
    '강아지': 100,
    '가나다': 50,
}
index = 0
result = [k for k in info.keys()]

for i, name in enumerate(result):
    pivot_name = name
    pivot_score = info[name]
    for j, name_ in enumerate(result):
        score = info[name_]
        if pivot_score < score:
            result[i], result[j] = name_, pivot_name
            pivot_name = name_
            pivot_score = score

print(result)