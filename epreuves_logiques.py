import random

def affiche_batonnets(n):
    print(f"Bâtonnets restants : {'|' * n}")

def joueur_retrait(n):
    choix = 0
    while choix not in [1, 2, 3] or choix > n:
        saisie = input("Combien de bâtonnets voulez-vous retirer (1, 2 ou 3) ? : ").strip()
        if saisie.isdigit():
            choix = int(saisie)
            if choix not in [1, 2, 3]:
                print("Erreur : Vous devez choisir 1, 2 ou 3.")
            elif choix > n:
                print(f"Erreur : Il ne reste que {n} bâtonnet(s).")
                choix = 0
        else:
            print("Erreur : Veuillez entrer un chiffre (1, 2 ou 3).")
    return choix

def maitre_retrait(n):
    retrait = (n - 1) % 4
    if retrait == 0:
        retrait = random.randint(1, min(3, n))
    print(f"Le maître du jeu retire {retrait} bâtonnets.")
    return retrait

def jeu_nim():
    nb_batonnets = 20
    tour_joueur = True
    while nb_batonnets > 0:
        affiche_batonnets(nb_batonnets)
        if tour_joueur:
            print("Tour du joueur.")
            nb_batonnets -= joueur_retrait(nb_batonnets)
            if nb_batonnets == 0:
                print("Vous avez retiré le dernier bâtonnet. Le maître du jeu gagne !")
                return False
        else:
            nb_batonnets -= maitre_retrait(nb_batonnets)
            if nb_batonnets == 0:
                print("Le maître du jeu a retiré le dernier bâtonnet. Le joueur gagne !")
                return True
        tour_joueur = not tour_joueur

def affiche_grille_morpion(grille):
    for i in range(3):
        print(f" {grille[i][0]} | {grille[i][1]} | {grille[i][2]} ")
        if i < 2:
            print("-----------")

def verifier_victoire(grille, symbole):
    for i in range(3):
        if all(grille[i][j] == symbole for j in range(3)) or \
           all(grille[j][i] == symbole for j in range(3)):
            return True
    if (grille[0][0] == symbole and grille[1][1] == symbole and grille[2][2] == symbole) or \
       (grille[0][2] == symbole and grille[1][1] == symbole and grille[2][0] == symbole):
        return True
    return False

def grille_complete(grille):
    for ligne in grille:
        if " " in ligne:
            return False
    return True

def coup_maitre(grille, symbole):
    adversaire = "X" if symbole == "O" else "O"
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = symbole
                if verifier_victoire(grille, symbole):
                    grille[i][j] = " "
                    return (i, j)
                grille[i][j] = " "
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = adversaire
                if verifier_victoire(grille, adversaire):
                    grille[i][j] = " "
                    return (i, j)
                grille[i][j] = " "
    libres = [(i, j) for i in range(3) for j in range(3) if grille[i][j] == " "]
    return random.choice(libres)

def tour_joueur(grille):
    valide = False
    while not valide:
        saisie = input("Joueur X, où voulez-vous placer votre symbole (ligne,colonne) ? : ").strip()
        if "," in saisie:
            parts = saisie.split(",")
            if parts[0].isdigit() and parts[1].isdigit():
                l, c = int(parts[0]) - 1, int(parts[1]) - 1
                if 0 <= l < 3 and 0 <= c < 3:
                    if grille[l][c] == " ":
                        grille[l][c] = "X"
                        valide = True
                    else:
                        print("Case déjà occupée !")
                else:
                    print("Coordonnées hors grille (1 à 3) !")
            else:
                print("Veuillez entrer des chiffres.")
        else:
            print("Format invalide (ligne,colonne).")

def tour_maitre_morpion(grille):
    print("Tour du maître du jeu (O)...")
    l, c = coup_maitre(grille, "O")
    grille[l][c] = "O"

def jeu_tictactoe():
    grille = [[" " for _ in range(3)] for _ in range(3)]
    while True:
        affiche_grille_morpion(grille)
        tour_joueur(grille)
        if verifier_victoire(grille, "X"):
            affiche_grille_morpion(grille)
            print("Le joueur a gagné !")
            return True
        if grille_complete(grille):
            affiche_grille_morpion(grille)
            print("Match nul !")
            return False
        tour_maitre_morpion(grille)
        if verifier_victoire(grille, "O"):
            affiche_grille_morpion(grille)
            print("Le maître du jeu a gagné !")
            return False
        if grille_complete(grille):
            affiche_grille_morpion(grille)
            print("Match nul !")
            return False

def suiv(joueur):
    return 1 - joueur

def grille_vide():
    return [[" " for _ in range(3)] for _ in range(3)]

def affiche_grille_navale(grille, message):
    print(f"\n{message}")
    for ligne in grille:
        print(f"| {' | '.join(ligne)} |")
    print("-" * 13)

def demande_position():
    valide = False
    while not valide:
        saisie = input("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2) : ").strip()
        if "," in saisie:
            parts = saisie.split(",")
            if parts[0].isdigit() and parts[1].isdigit():
                l, c = int(parts[0]) - 1, int(parts[1]) - 1
                if 0 <= l < 3 and 0 <= c < 3:
                    return (l, c)
        print("Erreur : Position invalide (format 1,2 entre 1 et 3).")

def init():
    grille = grille_vide()
    for i in range(1, 3):
        print(f"Bateau {i}")
        valide = False
        while not valide:
            l, c = demande_position()
            if grille[l][c] == " ":
                grille[l][c] = "B"
                valide = True
            else:
                print("Position déjà occupée !")
    return grille

def tour_navale(joueur, grille_tirs_joueur, grille_adversaire):
    if joueur == 0:
        affiche_grille_navale(grille_tirs_joueur, "Rappel de l'historique de vos tirs :")
        l, c = demande_position()
    else:
        l, c = random.randint(0, 2), random.randint(0, 2)
        while grille_tirs_joueur[l][c] != " ":
            l, c = random.randint(0, 2), random.randint(0, 2)
        print(f"Le maître du jeu tire en position {l+1},{c+1}")

    if grille_adversaire[l][c] == "B":
        print("Touché coulé !")
        grille_tirs_joueur[l][c] = "x"
    else:
        print("Dans l'eau...")
        grille_tirs_joueur[l][c] = "."

def gagne_navale(grille_tirs_joueur):
    nb_touches = sum(ligne.count("x") for ligne in grille_tirs_joueur)
    return nb_touches == 2

def jeu_bataille_navale():
    print("Chaque joueur doit placer 2 bateaux sur une grille de 3x3.")
    print("Positionnez vos bateaux :")
    grille_joueur = init()
    affiche_grille_navale(grille_joueur, "Découvrez votre grille de jeu avec vos bateaux :")

    grille_maitre = grille_vide()
    placed = 0
    while placed < 2:
        l, c = random.randint(0, 2), random.randint(0, 2)
        if grille_maitre[l][c] == " ":
            grille_maitre[l][c] = "B"
            placed += 1

    tirs_joueur = grille_vide()
    tirs_maitre = grille_vide()
    joueur_actuel = 0

    while True:
        if joueur_actuel == 0:
            print("\nC'est à votre tour de faire feu !")
            tour_navale(0, tirs_joueur, grille_maitre)
            if gagne_navale(tirs_joueur):
                print("Le joueur a gagné !")
                return True
        else:
            print("\nC'est le tour du maître du jeu :")
            tour_navale(1, tirs_maitre, grille_joueur)
            if gagne_navale(tirs_maitre):
                print("Le maître du jeu a gagné !")
                return False
        joueur_actuel = suiv(joueur_actuel)

def epreuve_logique():
    epreuves = [jeu_nim, jeu_tictactoe, jeu_bataille_navale]
    epreuve = random.choice(epreuves)
    return epreuve()

if __name__ == "__main__":
    print("=== BATTERIE DE TESTS : MODULE LOGIQUE ===\n")
    
    print(f"Test NIM - maitre_retrait(20): {maitre_retrait(20)} (attendu: 3)")
    print(f"Test NIM - maitre_retrait(13): {maitre_retrait(13)} (attendu: 1)")
    print(f"Test Navale - suiv(0): {suiv(0)} (attendu: 1)")
    
    gagnante_navale = [['x', '.', ' '], ['x', ' ', ' '], [' ', ' ', ' ']]
    print(f"Test Navale - gagne_navale (2 x): {gagne_navale(gagnante_navale)} (attendu: True)")

    g_victoire = [['X', 'X', 'X'], [' ', 'O', ' '], [' ', ' ', 'O']]
    g_pleine = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'X']]
    
    print(f"Test Morpion - verifier_victoire: {verifier_victoire(g_victoire, 'X')} (attendu: True)")
    print(f"Test Morpion - grille_complete: {grille_complete(g_pleine)} (attendu: True)")

    g_ia = [['X', 'X', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]
    print(f"Test IA Morpion - bloquer (0,2): {coup_maitre(g_ia, 'O')} (attendu: (0, 2))")

    print("\nTest Visuel - affiche_batonnets(5):")
    affiche_batonnets(5)
    
    print("\n=== FIN DES TESTS ===")

    if input("\nLancer une épreuve aléatoire ? (o/n) : ").strip().lower() == 'o':
        resultat = epreuve_logique()
        texte_res = "Victoire du joueur" if resultat else "Défaite du joueur"
        print(f"\nRésultat final : {texte_res}")
