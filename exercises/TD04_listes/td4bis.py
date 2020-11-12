def syracuse(n):
    l = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        l.append(n)
    return l
#print(syracuse(3))

def testeConjecture(n_max):
    for i in range(2, n_max+1):
        syracuse(i)
    return
#print(testeConjecture(10000))


