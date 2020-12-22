# 큰 수의 법칙

from test2 import service

if __name__ == '__main__':
    print("hello")
    sv1 = service.Service("5 8 3", "2 4 5 4 6")
    print(sv1.get_max_num())

    sv2 = service.Service("5 7 2", "3 4 3 4 3")
    print(sv2.get_max_num())
