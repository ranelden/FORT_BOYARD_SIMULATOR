import random

def factorielle(n):
    if n == 0:
        return 1
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

def epreuve_math_factorielle():
    n = random.randint(1, 10)
    print("Calculez la factorielle de " + str(n) + ".")
    
    reponse_saisie = input("Votre réponse est : ").strip()
    if not reponse_saisie.isdigit():
        print("Erreur : veuillez entrer un nombre entier.")
        return False
        
    reponse = int(reponse_saisie)
    correct = factorielle(n)
    
    if reponse == correct:
        print("Bonne réponse !")
        return True
    return False

def resoudre_equation_lineaire():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    x = -b / a
    return a, b, x

def epreuve_math_equation():
    a, b, x_correct = resoudre_equation_lineaire()
    print("Épreuve de Mathématiques : Résoudre l'équation " + str(a) + "x + " + str(b) + " = 0.")
    
    reponse_saisie = input("Quelle est la valeur de x : ").strip()
    
    est_valide = True
    for c in reponse_saisie.replace(".", "", 1).replace("-", "", 1):
        if not c.isdigit():
            est_valide = False
            
    if not est_valide or reponse_saisie == "":
        print("Erreur : veuillez entrer un nombre valide.")
        return False
        
    reponse = float(reponse_saisie)
    if abs(reponse - x_correct) < 0.01:
        print("Correct ! Vous gagnez une clé.")
        return True
    return False

def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def premier_plus_proche(n):
    p = n
    while not est_premier(p):
        p += 1
    return p

def epreuve_math_premier():
    n = random.randint(10, 20)
    solution = premier_plus_proche(n)
    print("Épreuve de Mathématiques : Trouver le nombre premier le plus proche au-dessus de " + str(n) + ".")
    
    reponse_saisie = input("Votre réponse est : ").strip()
    if not reponse_saisie.isdigit():
        print("Erreur : veuillez entrer un nombre entier.")
        return False
        
    reponse = int(reponse_saisie)
    if reponse == solution:
        print("Bonne réponse !")
        return True
    return False

def epreuve_roulette_mathematique():
    nombres = [random.randint(1, 20) for _ in range(5)]
    operation = random.choice(['addition', 'soustraction', 'multiplication'])
    print("Nombres sur la roulette : " + str(nombres))
    print("Calculez le résultat en combinant ces nombres avec une " + operation + ".")

    if operation == 'addition':
        resultat = sum(nombres)
    elif operation == 'soustraction':
        resultat = nombres[0]
        for num in nombres[1:]:
            resultat -= num
    else:
        resultat = 1
        for num in nombres:
            resultat *= num

    reponse_saisie = input("Votre réponse est : ").strip()
    if not reponse_saisie.replace("-", "", 1).isdigit():
        print("Erreur : veuillez entrer un nombre entier.")
        return False
        
    reponse = int(reponse_saisie)
    if reponse == resultat:
        print("Bonne réponse !")
        return True
    return False

def epreuve_math():
    epreuves = [
        epreuve_math_factorielle,
        epreuve_math_equation,
        epreuve_math_premier,
        epreuve_roulette_mathematique
    ]
    epreuve = random.choice(epreuves)
    return epreuve()

if __name__ == "__main__":
    print("--- TESTS AUTOMATIQUES DES FONCTIONS LOGIQUES ---")
    
    print("Test factorielle(0) : " + str(factorielle(0) == 1))
    print("Test factorielle(3) : " + str(factorielle(3) == 6))
    print("Test factorielle(5) : " + str(factorielle(5) == 120))
    
    print("Test est_premier(2) : " + str(est_premier(2) == True))
    print("Test est_premier(4) : " + str(est_premier(4) == False))
    print("Test est_premier(13) : " + str(est_premier(13) == True))
    
    print("Test premier_plus_proche(10) : " + str(premier_plus_proche(10) == 11))
    print("Test premier_plus_proche(14) : " + str(premier_plus_proche(14) == 17))
    print("Test premier_plus_proche(20) : " + str(premier_plus_proche(20) == 23))

    print("\n--- TESTS INTERACTIFS DES ÉPREUVES ---")
    
    print("\n1. Test Épreuve Factorielle")
    print("Résultat : " + str(epreuve_math_factorielle()))
    
    print("\n2. Test Épreuve Équation")
    print("Résultat : " + str(epreuve_math_equation()))
    
    print("\n3. Test Épreuve Nombre Premier")
    print("Résultat : " + str(epreuve_math_premier()))
    
    print("\n4. Test Épreuve Roulette")
    print("Résultat : " + str(epreuve_roulette_mathematique()))
    
    print("\n5. Test Sélection Aléatoire")
    print("Résultat : " + str(epreuve_math()))