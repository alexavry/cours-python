import math

def f(x):
    """
    Calcule la valeur de la fonction f pour un vecteur x.

    Paramètres:
    x (list): un vecteur de n éléments (x_1, ..., x_n).

    Retourne:
    float: La valeur de la fonction f(x).
    """
    # Calculer la somme des sin^2(x_i)
    somme_sin2 = sum(math.sin(xi) ** 2 for xi in x)

    # Calculer la somme des x_i^2
    somme_x2 = sum(xi ** 2 for xi in x)

    # Calculer la valeur de f(x)
    resultat = 1 + somme_sin2 - 0.1 * math.exp(somme_x2)

    return resultat

x = [1, 2, 3]
resultat = f(x)
print(resultat)