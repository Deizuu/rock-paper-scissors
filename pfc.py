from random import randint

# les joueurs
pfc_selection = ['pierre', 'feuille', 'ciseaux']
pfc = pfc_selection[randint(0,2)]

# les points
points_joueur = 0
points_bot = 0

while points_joueur != 3 and points_bot != 3:

    userinput = input("Pierre, feuille ou ciseaux ? : ").lower()
    if userinput == pfc:
        print("Egalité: " + str(points_joueur) + "-" + str(points_bot))
        pfc = pfc_selection[randint(0,2)]
    elif userinput == 'pierre' and pfc == 'feuille' or userinput == 'feuille' and pfc == 'ciseaux' or userinput == 'ciseaux' and pfc == 'pierre':
        points_bot += 1
        print("Perdu: " + str(points_joueur) + "-" + str(points_bot))
        pfc = pfc_selection[randint(0,2)]
        if points_bot == 3:
            print("Mais t'es une grosse merde")
    elif userinput == 'pierre' and pfc == 'ciseaux' or userinput == 'feuille' and pfc == 'pierre' or userinput == 'ciseaux' and pfc == 'feuille':
        points_joueur += 1
        print("Gagné: " + str(points_joueur) + "-" + str(points_bot))
    elif userinput != 'pierre' or userinput != 'feuille' or userinput != 'ciseaux':
        print("j'ai dit pierre feuille ou ciseaux sale mangeur de pates")
        pfc = pfc_selection[randint(0,2)]
        if points_joueur == 3:
            print("Felicitations ! Tu as gagne !")