class Service:
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def run(self):
        pass

    def recursive_fn(self, i):
        print('재귀 함수')
        if i == 100:
            return

        print(f'{i} 번째 재귀 함수에서, {i + 1} 번째 재귀함수를 호출 합니다.')
        self.recursive_fn(i + 1)
        print(f'{i} 번째 재귀함수를 종료합니다.')

    # 반복적으로 구현한 n!
    @staticmethod
    def factorial_iterative(n):
        result = 1
        for i in range(1, n + 1):
            result *= i

        return result

    # 재귀적으로 구현한 n!
    def factorial_recursive(self, n):
        if n <= 1:
            return 1

        return n * self.factorial_recursive(n - 1)
