import random



def factorielle(n):
    if n == 0:
        return 1
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat


def guess_factorielle():
    n = random.randint(1, 10)
    print("Calcule la factorielle de " + str(n) + ".")
    reponse = int(input("Votre réponse est: "))
    correct = factorielle(n)
    if reponse == correct:
        print("Bonne réponse!!!")
        return True
    else:
        return False


def resoudre_equation_lineaire():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    x = -b / a
    return a, b, x


def epreuve_math_equation():
    a, b, x_correct = resoudre_equation_lineaire()
    print("Épreuve de Mathématiques: Résoudre l'équation " + str(a) + "x + " + str(b) + " = 0.")
    reponse = float(input("Quelle  la valeur de x: "))
    if abs(reponse - x_correct) < 0.01:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        return False


def nbr_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def premier_plus_proche(n):
    p = n
    while not nbr_premier(p):
        p += 1
    return p


def epreuve_math_premier():
    n = random.randint(10, 20)
    solution = premier_plus_proche(n)
    print("Épreuve de Mathématiques: Trouver le nombre premier le plus proche au dessus de " + str(n) + ".")
    reponse = int(input("Votre réponse est: "))
    if reponse == solution:
        print("Bonne réponse!")
        return True
    else:
        return False


def epreuve_roulette_mathematique():
    nombres = [random.randint(1, 20) for _ in range(5)]
    operation = random.choice(['addition', 'soustraction', 'multiplication'])
    print("Nombres sur la roulette : " + str(nombres))
    print("Calculez le résultat en combinant ces nombres avec une " + operation)

    if operation == 'addition':
        resultat = sum(nombres)
    elif operation == 'soustraction':
        resultat = nombres[0]
        for num in nombres[1:]:
            resultat -= num
    else:  # multiplication
        resultat = 1
        for num in nombres:
            resultat *= num

    reponse = int(input("Votre réponse est: "))
    if reponse == resultat:
        print("Bonne réponse!")
        return True
    else:
        return False


def epreuve_math():
    epreuves = [
        guess_factorielle,
        epreuve_math_equation,
        epreuve_math_premier,
        epreuve_roulette_mathematique
    ]
    epreuve = random.choice(epreuves)
    return epreuve()


print(epreuve_math())