import math

calcul = input("Veuillez entrer votre calcul : ")
signe = ""
partieA = ""
partieB = ""
trouvé = False
resultat = ""
for caracter in calcul:
    if caracter in "+-/*":
        signe = caracter
        trouvé = True
    elif caracter == " ":
        continue
    elif trouvé == False :
        partieA += caracter
    else:
        partieB += caracter

if signe ==  "+":
    resultat = int(partieA) + int(partieB)
elif signe == "-":
    resultat = int(partieA) - int(partieB)
elif signe == "*":
    resultat = int(partieA) * int(partieB)
elif signe == "/":
    resultat = int(partieA) / int(partieB)
else:
    resultat = "erreur"

print(f"Le résultat de votre calcul est {resultat}")