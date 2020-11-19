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
print(carre_pas_mag)
print(carre_mag)
