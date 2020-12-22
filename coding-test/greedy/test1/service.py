class Service(object):
    _COINS = (500, 100, 50, 10,)

    def __init__(self, change):
        self.change = change

    def __repr__(self):
        return f'{self.__class__}'

    def get_change(self):
        result = 0
        for _, coin in enumerate(self._COINS):
            # >>>>>>>>>>>
            # 내가 짠 코드
            # num = int(self.change / coin)
            # self.change = self.change - (coin * num)
            # result += num
            # <<<<<<<<<<<

            # 풀이를 보고 수정한 코드
            result += self.change // coin
            self.change %= coin

        return result
