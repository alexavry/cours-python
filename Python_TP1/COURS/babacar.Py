mot = "AABAACAADAABAABA"
occurences = 0
liste_positions=[]
for i in range(len(mot) - 1):
    if mot[i] == "A" and mot[i + 1] == "A" and mot[i + 2] == "B" and mot[i + 3] == "A":
        occurences +=1
        liste_positions.append(i)
print(f"Il y a {occurences} de AABA dans le texte et elles sont en position {liste_positions}")


