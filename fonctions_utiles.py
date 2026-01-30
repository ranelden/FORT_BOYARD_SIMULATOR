import random

def introduction():
    print("====================================================")
    print("        BIENVENUE DANS LE FORT BOYARD SIMULATOR     ")
    print("====================================================")
    print("Tu vas constituer une équipe de 1 à 3 joueurs.")
    print("Chaque épreuve réussie te fera gagner une clé.")
    print("Avec 3 clés, tu pourras tenter d'accéder à la salle du trésor !")
    print()

def composer_equipe():
    """
    Demande à l'utilisateur de créer une équipe de 1 à 3 joueurs.
    Retourne une liste de dictionnaires :
    [{'nom': 'Alice', 'cles': 0, 'leader': True}, ...]
    """
    equipe = []

    # nombre de joueurs
    while True:
        try:
            nb = int(input("Combien de joueurs dans l'équipe ? (1 à 3) : "))
            if 1 <= nb <= 3:
                break
            else:
                print("❌ Merci de saisir un nombre entre 1 et 3.")
        except ValueError:
            print("❌ Entrée invalide, merci de saisir un nombre.")

    # saisie des noms
    for i in range(1, nb + 1):
        nom = ""
        while nom.strip() == "":
            nom = input(f"Nom du joueur {i} : ").strip()
            if nom == "":
                print("❌ Le nom ne peut pas être vide.")
        joueur = {
            "nom": nom,
            "cles": 0,
            "leader": False
        }
        equipe.append(joueur)

    # choix du leader
    if nb == 1:
        equipe[0]["leader"] = True
        print(f"{equipe[0]['nom']} est automatiquement le leader de l'équipe.")
    else:
        print("\nQui sera le leader de l'équipe ?")
        for i, joueur in enumerate(equipe, start=1):
            print(f"{i}. {joueur['nom']}")

        while True:
            try:
                choix = int(input("Numéro du leader : "))
                if 1 <= choix <= nb:
                    equipe[choix - 1]["leader"] = True
                    break
                else:
                    print(f"❌ Merci de saisir un nombre entre 1 et {nb}.")
            except ValueError:
                print("❌ Entrée invalide, merci de saisir un nombre.")

        print(f"✅ {equipe[choix - 1]['nom']} est le leader de l'équipe !\n")

    return equipe

def menu_epreuves():
    """
    Affiche le menu des types d'épreuves et renvoie le choix de l'utilisateur.
    Retourne une chaîne : 'math', 'hasard', 'logique', 'pere_fouras' ou 'quitter'.
    """
    print("============== MENU DES EPREUVES ==============")
    print("1 - Epreuves mathématiques")
    print("2 - Epreuves de hasard")
    print("3 - Epreuves logiques")
    print("4 - Enigmes du Père Fouras")
    print("0 - Quitter le jeu")
    print("===============================================")

    while True:
        choix = input("Ton choix : ").strip()
        if choix == "1":
            return "math"
        elif choix == "2":
            return "hasard"
        elif choix == "3":
            return "logique"
        elif choix == "4":
            return "pere_fouras"
        elif choix == "0":
            return "quitter"
        else:
            print("❌ Choix invalide, merci de saisir 0, 1, 2, 3 ou 4.")

def choisir_joueur(equipe):
    """
    Demande quel joueur participe à l'épreuve en cours.
    Retourne le dictionnaire du joueur choisi.
    """
    print("\nQuel joueur va participer à cette épreuve ?")
    for i, joueur in enumerate(equipe, start=1):
        info_leader = " (leader)" if joueur.get("leader") else ""
        print(f"{i}. {joueur['nom']} - Clés : {joueur['cles']}{info_leader}")

    while True:
        try:
            choix = int(input("Numéro du joueur : "))
            if 1 <= choix <= len(equipe):
                joueur_choisi = equipe[choix - 1]
                print(f"👉 {joueur_choisi['nom']} entre dans l'épreuve !\n")
                return joueur_choisi
            else:
                print(f"❌ Merci de saisir un nombre entre 1 et {len(equipe)}.")
        except ValueError:
            print("❌ Entrée invalide, merci de saisir un nombre.")
