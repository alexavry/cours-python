import random

def tirer_des():
    tirage = []
    i = 0
    while i < 5:
        tour = random.randint(1,6)
        tirage.append(tour)
        i += 1
    return tirage

class Player:
    def __init__(self):
        self.brelan = False #somme des 3 dés identiques
        self.carre = False #40pts
        self.full = False #35PTS
        self.petite_suite = False #40pts
        self.grande_suite = False #50pts
        self.chance = False #55 pts
        self.yams = False #somme des 5 dés

        self.score = 0


def count(tirage):
    counter = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for each in tirage:
        if each == 1:
            counter[1] += 1
        elif each == 2:
            counter[2] += 1
        elif each == 3:
            counter[3] += 1
        elif each == 4:
            counter[4] += 1
        elif each == 5:
            counter[5] += 1
    return counter
def verif_brelan(dico):
    return 3 in dico.values()

def verif_carre(dico):
    return 4 in dico.values()

def verif_full(dico):
    if 3 in dico.values() and 2 in dico.values():
        return True

def verif_petite_suite(dico):
    suites_possibles = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
    for i in range(1,4):
        if i >= 1 and i+1 >= 1 and i+2 >= 1 and i+3 >= 1 :
            return True

def verif_grande_suite(dico):
    grande_suite_1 = {1, 2, 3, 4, 5}
    grande_suite_2 = {2, 3, 4, 5, 6}
    for i in range(1,5):

def tout_verif(dico):
    resultat =""
    if verif_brelan(dico):
        resultat = "Brelan"
    if verif_carre(dico):
        resultat = "Carré"
    if verif_full(dico):
        resultat = "Full"
    if verif_petite_suite(dico):
        resultat = "Petite suite"
    if verif_grande_suite(dico):
        resultat = "Grande suite"
newdico = {}
j1 = tirer_des()
j1bis = count(j1)
print(j1)
print(j1bis)

