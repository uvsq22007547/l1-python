# question 1

carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
# print(carre_mag)
# print(carre_mag[0])
# print(carre_mag[0][0])
# i = 2
# j = 3
# print(carre_mag[i][j]) # affiche la valeur qui est à la ligne i et colonne j

# question 2

carre_pas_mag = list(carre_mag)
for i in range(len(carre_pas_mag)):
    carre_pas_mag[i] = list(carre_pas_mag[i])
carre_pas_mag[3][2] = 7
# print(carre_pas_mag)
# print(carre_mag)


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for ligne in carre:
        print(ligne)
    print()

# afficheCarre(carre_mag)
# afficheCarre(carre_pas_mag)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    somme = sum(carre[0]) # somme des élements de la premières ligne
    for ligne in carre:
        if sum(ligne) != somme:
            return -1
    return somme
    

print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))