def o():
    l = [[1,2,3],[4,5,6]]

    def p():
        l[0][1] = 1000
        print(l)

    p()

o()