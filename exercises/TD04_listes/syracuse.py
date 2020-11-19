# suite de syracuse
# 3, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1

def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    l_res = [n]
    while n != 1:
        if n % 2 == 0:  # si n est pair
            n = n // 2
        else:  # si n est impair
            n = 3 * n + 1
        l_res.append(n)
    return l_res


# print(syracuse(3))
# print(help(syracuse))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(2, n_max + 1):
        syracuse(i)
    return "Conjecture vérifiée jusqu'à n = " + str(n_max)

print(testeConjecture(10000))
