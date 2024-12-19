from random import randint

liste_mots = ["tableau"]
index = randint(0, len(liste_mots) - 1)
word_to_find = liste_mots[index]
mot_hache = list("_" * len(word_to_find))
finish = False

while not finish:
    print("Mot à deviner : " + "".join(mot_hache))
    a = input("Merci de rentrer une lettre : ").lower()

    if a in word_to_find:
        for i in range(len(word_to_find)):
            if word_to_find[i] == a:
                mot_hache[i] = a
        print("Bonne lettre !")
    else:
        print("Cette lettre ne fait pas partie du mot.")

    if "_" not in mot_hache:
        finish = True
        print("Félicitations ! Vous avez trouvé le mot :", "".join(mot_hache))


