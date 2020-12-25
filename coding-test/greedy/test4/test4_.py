from test4 import service

if __name__ == '__main__':
    sv1 = service.Service(17, 4)
    sv2 = service.Service(25, 5)
    sv3 = service.Service(9, 3)
    sv4 = service.Service(25, 3)
    sv5 = service.Service(257, 3)

    print(sv1.run())
    print(sv2.run())
    print(sv3.run())
    print(sv4.run())
    print(sv5.run())
