import random

def introduction():
    print(" ")
    print("        BIENVENUE DANS LE FORT BOYARD SIMULATOR     ")
    print(" ")
    print("Tu vas constituer une équipe de 1 à 3 joueurs.")
    print("Chaque épreuve réussie te fera gagner une clé.")
    print("Avec 3 clés, tu pourras tenter d'accéder à la salle du trésor !")
    print()

def composer_equipe():
    equipe = []
    # nombre de joueurs
    while True:
            nb = int(input("Combien de joueurs dans l'équipe ? (1 à 3) : "))
            if 1 <= nb <= 3:
                break
            elif 1 > nb:
                print(" Merci de saisir un nombre entre 1 et 3.")
            elif 3 < nb:
                print(" Merci de saisir un nombre entre 1 et 3.")
            else:
                print(" Entrée invalide, merci de saisir un nombre.")

    # saisie des noms
    for i in range(1, nb + 1):
        nom = ""
        while nom.strip() == "":
          nom = input(f"Nom du joueur{i}:").strip()
        if nom == "":
              print(" Le nom ne peut pas être vide.")
        equipe.append(joueur)

    # choix du leader
    if nb == 1:
        equipe[0]["leader"] = True
        print(f"{equipe[0]['nom']} est automatiquement le leader de l'équipe.")
    else:
        print("Qui sera le leader de l'équipe ?")
    for i, joueur in len(equipe):
        print(f"{i}. {joueur['nom']}")

        while True:
                choix = int(input("Numéro du leader : ")) or input("Nom du leader : ")
                if 1 <= choix <= len(equipe):
                    equipe[choix - 1]["leader"] = True
                    break
                else:
                    print(" Merci de choisir le leadeur parmit les membre de l'equipe")

        print(f" {equipe[choix - 1]['nom']} est le leader de l'équipe ")

    return equipe

def menu_epreuves():
    print(" MENU DES EPREUVES ")
    print("1 - Epreuves mathématiques")
    print("2 - Epreuves de hasard")
    print("3 - Epreuves logiques")
    print("4 - Enigmes du Père Fouras")
    print("0 - Quitter le jeu")
    print("")

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
            print(" Choix invalide, merci de saisir 0, 1, 2, 3 ou 4.")

def choisir_joueur(equipe):
    print("Quel joueur va participer à cette épreuve ?")
    for i, joueur in len(equipe):
        info_leader = " (leader)" if joueur.get("leader") else ""
        print(f"{i}. {joueur['nom']} - Clés : {joueur['cles']}{info_leader}")

    while True:
            choix = int(input("Numéro du joueur : "))
            if 1 <= choix <= len(equipe):
                joueur_choisi = equipe[choix - 1]
                print(f" {joueur_choisi['nom']} entre dans l'épreuve !\n")
                return joueur_choisi
            elif 1 > choix or choix > len(equipe):
                print(f" Merci de saisir un nombre entre 1 et {len(equipe)}.")
            else:
                print(" Entrée invalide, merci de saisir un nombre.")
