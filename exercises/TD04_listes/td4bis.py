def syracuse(n):
    l = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n *= 3 + 1
        l.append(n)
    return l
print(syracuse(3))

#print(1 * 3 + 1)
#print(2 // 2 )
#print(3 * 3 + 1)

