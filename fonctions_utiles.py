import random

def introduction():
<<<<<<< HEAD
    print("====|||||||||============|||||||===========||||||-======")
    print("        BIENVENUE DANS LE FORT BOYARD SIMULATOR     ")
    print("====|||||||============|||||||-=============|||||||||=======")
=======
    print("====================================================")
    print("        BIENVENUE DANS LE FORT BOYARD SIMULATOR     ")
    print("====================================================")
>>>>>>> origin/main
    print("Tu vas constituer une equipe de 1 a 3 joueurs.")
    print("Chaque epreuve reussie te fera gagner une cle.")
    print("Avec 3 cles, tu pourras tenter d'acceder a la salle du tresor !")
    print()

<<<<<<< HEAD

def composer_equipe():
    equipe = []

=======
def composer_equipe():
    equipe = []
    
>>>>>>> origin/main
    nb_joueurs = ""
    while nb_joueurs not in ["1", "2", "3"]:
        nb_joueurs = input("Combien de joueurs dans l'equipe ? (1 a 3) : ").strip()
        if nb_joueurs not in ["1", "2", "3"]:
            print("Saisie invalide. Merci de choisir 1, 2 ou 3.")

    nb = int(nb_joueurs)

    for i in range(1, nb + 1):
        print("\n--- Joueur", i, "---")
<<<<<<< HEAD

=======
        
>>>>>>> origin/main
        nom = input("Nom du joueur : ").strip()
        while nom == "":
            print("Le nom ne peut pas etre vide.")
            nom = input("Nom du joueur : ").strip()
<<<<<<< HEAD

        profession = input("Profession du joueur : ").strip()

=======
            
        profession = input("Profession du joueur : ").strip()
        
>>>>>>> origin/main
        role_input = ""
        while role_input not in ["oui", "non"]:
            role_input = input("Est-ce le leader de l'equipe ? (oui/non) : ").strip().lower()
            if role_input not in ["oui", "non"]:
                print("Repondez par 'oui' ou 'non'.")

        joueur = {
            "nom": nom,
            "profession": profession,
            "leader": (role_input == "oui"),
            "cles_gagnees": 0
        }
        equipe.append(joueur)

<<<<<<< HEAD
    # S'assurer qu'il y a un leader
=======
>>>>>>> origin/main
    leader_trouve = False
    for j in equipe:
        if j["leader"]:
            leader_trouve = True
<<<<<<< HEAD

=======
            
>>>>>>> origin/main
    if not leader_trouve:
        equipe[0]["leader"] = True
        print("\nAucun leader choisi,", equipe[0]['nom'], "est designe leader par defaut.")

    return equipe

<<<<<<< HEAD

def menu_epreuves():
    print("\n=====||||||========= MENU DES EPREUVES =====||||||-=========")
=======
def menu_epreuves():
    print("\n============== MENU DES EPREUVES ==============")
>>>>>>> origin/main
    print("1 - Epreuves mathematiques")
    print("2 - Epreuves de hasard")
    print("3 - Epreuves logiques")
    print("4 - Enigmes du Pere Fouras")
    print("0 - Quitter le jeu")
<<<<<<< HEAD
    print("======||||||||||=================|||||||||-========================")
=======
    print("===============================================")
>>>>>>> origin/main

    choix = ""
    while choix not in ["1", "2", "3", "4", "0"]:
        choix = input("Ton choix : ").strip()
        if choix not in ["1", "2", "3", "4", "0"]:
            print("Choix invalide, merci de saisir 0, 1, 2, 3 ou 4.")
<<<<<<< HEAD

    return int(choix)


def choisir_joueur(equipe):
    print("\n Quel joueur va participer a cette epreuve ?")
=======
            
    return int(choix)

def choisir_joueur(equipe):
    print("\nQuel joueur va participer a cette epreuve ?")
>>>>>>> origin/main
    for i, joueur in enumerate(equipe, start=1):
        role = "Leader" if joueur["leader"] else "Membre"
        print(str(i) + ". " + joueur['nom'] + " (" + joueur['profession'] + ") - " + role)

    selection = ""
    valide = False
    while not valide:
        selection = input("Numero du joueur : ").strip()
        if selection.isdigit():
            index = int(selection)
            if 1 <= index <= len(equipe):
                valide = True
            else:
                print("Numero hors limite (1 a " + str(len(equipe)) + ").")
        else:
            print("Veuillez entrer un nombre valide.")
<<<<<<< HEAD

    joueur_choisi = equipe[int(selection) - 1]
    print("Le joueur selectionne est : " + joueur_choisi['nom'])
    return joueur_choisi

=======
            
    joueur_choisi = equipe[int(selection) - 1]
    print("Le joueur selectionne est : " + joueur_choisi['nom'])
    return joueur_choisi
>>>>>>> origin/main
