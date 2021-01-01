from implement.test4.service import Service

if __name__ == '__main__':
    print('hello')
    sv1 = Service("5 5", "1 2 3", "1 1 1 1 1", "1 0 0 0 1", "1 0 0 0 1", "1 1 1 1 1", "1 1 1 1 1")
    print(sv1.run())

    sv2 = Service("4 4", "1 1 0", "1 1 1 1", "1 0 0 1", "1 1 0 1", "1 1 1 1")
    print(sv2.run())

    sv3 = Service("5 5", "1 2 2", "1 1 1 1 1", "1 0 0 0 1", "1 0 0 0 1", "1 0 1 0 1", "1 1 1 1 1")
    print(sv3.run())

    sv4 = Service("4 4", "1 1 0", "1 1 1 1", "1 0 0 1", "1 0 0 1", "1 1 1 1")
    print(sv4.run())

    sv5 = Service("5 5", "2 1 2", "1 1 1 1 1", "1 1 0 0 1", "1 1 0 1 1", "1 1 1 1 1", "1 1 1 1 1")
    print(sv5.run())
