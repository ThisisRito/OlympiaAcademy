def foo():
    for i in range(len(F)):
        for j in range(len(F)):
            if F[i] + F[j] == X:
                print(i, -j)
                return
            if F[i] - F[j] == X:
                print(i, j)
                return

X = int(input())
F = [i**5 for i in range(1000)]
flg = False
foo()