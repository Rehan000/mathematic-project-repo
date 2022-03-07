import mathematics

if __name__ == '__main__':
    ob1 = mathematics.Mathematics(4)
    ob2 = mathematics.Mathematics(16)

    print("-"*100)
    print(ob1.factorial())
    print(ob1.square())
    print(ob1.cube())
    print(ob1.square_root())

    print("-"*100)
    print(ob2.factorial())
    print(ob2.square())
    print(ob2.cube())
    print(ob2.square_root())
