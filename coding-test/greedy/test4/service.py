class Service:
    def __init__(self, n, k):
        self.n = n
        self.k = k

    def __repr__(self):
        return f'{self.__class__}'

    def run(self):
        cnt = 0
        while True:
            cnt += 1
            q, r = self._div()

            if r != 0:
                self._minus()
            else:
                self.n = q

            if self.n == 1 or q == 1:  # 몫으로 루프문을 점검하는 건 빼기로 답이 나오는 경우엔 오류를 발생시킨다.
                break

        return cnt

    def _minus(self):
        self.n -= 1

    def _div(self):
        return self.n // self.k, self.n % self.k
