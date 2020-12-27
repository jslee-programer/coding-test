from greedy.test4.service import Service

if __name__ == '__main__':
    sv1 = Service(17, 4)
    sv2 = Service(25, 5)
    sv3 = Service(9, 3)
    sv4 = Service(25, 3)
    sv5 = Service(257, 3)

    print(sv1.run())
    print(sv2.run())
    print(sv3.run())
    print(sv4.run())
    print(sv5.run())
