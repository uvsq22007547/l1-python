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

# print(testeConjecture(10000))

def tempsVol(n):
    """ Retourne le temps de vol de n """
    l = syracuse(n)
    return len(l) - 1

# print("Le temps de vol de", 3, "est", tempsVol(3))

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    #l_res = []
    #for i in range(1, n_max + 1):
    #    l_res.append(tempsVol(i))
    #return l_res

    # solution 2, avec une liste par compréhension:
    return [tempsVol(i) for i in range(1, n_max + 1)]

# print(tempsVolListe(100))

tvl = tempsVolListe(10)
print(tvl)
m = max(tvl)
print(m)
indice = tvl.index(m)
print(indice)
print("Le temps de vol max est", m, "atteint pour la valeur", indice + 1)

def altitudeMax(n):
    """ retourne l'altitude max de l'entier n """
    syr = syracuse(n)
    return max(syr)

# print(altitudeMax(3))

def altitudeMaxListe(n_max):
    """ Retourne la liste de tous les altitudes max de 1 à n_max """
    return [altitudeMax(i) for i in range(1, n_max + 1)]

# print(altitudeMaxListe(100))

aml = altitudeMaxListe(10000)
m = max(aml)
indice = aml.index(m)
# print("La plus grande altitude max est", m, "atteint pour la valeur", indice + 1)
