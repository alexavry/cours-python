import random

class Jeu:
    def __init__(self):
        self.nb_to_find = random.randint(0, 100)

    def check(self, nb_user):
        if nb_user > self.nb_to_find:
            print("Trop grand")
            return False
        elif nb_user < self.nb_to_find:
            print("Trop petit")
            return False
        else:
            print("Vous avez trouvé le nombre GG !")
            return True

    def enter(self):
        # Demande à l'utilisateur de saisir un nombre et le retourne
        nb_user = int(input("Entrer un nombre entre 0 et 100: "))
        return nb_user


jeu = Jeu()

while True:
    nb_user = jeu.enter()
    if jeu.check(nb_user):
        break