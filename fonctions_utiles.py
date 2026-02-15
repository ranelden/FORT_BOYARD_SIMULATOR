import random


def introduction():
    print("=======||||========================||||=====================")
    print("        BIENVENUE DANS LE FORT BOYARD SIMULATOR     ")
    print("====|||============|||===========||-=============|||============")
    print("Tu vas constituer une equipe de 1 a 3 joueurs.")
    print("Chaque epreuve reussie te fera gagner une cle.")
    print("Avec 3 cles, tu pourras tenter d'acceder a la salle du tresor !")
    print()


def composer_equipe():
    equipe = []

    nb_joueurs = ""
    while nb_joueurs not in ["1", "2", "3"]:
        nb_joueurs = input("Combien de joueurs dans l'equipe ? (1 a 3) : ").strip()
        if nb_joueurs not in ["1", "2", "3"]:
            print("Saisie invalide. Merci de choisir 1, 2 ou 3.")

    nb = int(nb_joueurs)

    for i in range(1, nb + 1):
        print("\n--- Joueur", i, "---")

        nom = input("Nom du joueur : ").strip()
        while nom == "":
            print("Le nom ne peut pas etre vide.")
            nom = input("Nom du joueur : ").strip()

        profession = input("Profession du joueur : ").strip()

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

    leader_trouve = False
    for j in equipe:
        if j["leader"]:
            leader_trouve = True

    if not leader_trouve:
        equipe[0]["leader"] = True
        print("\nAucun leader choisi,", equipe[0]['nom'], "est designe leader par defaut.")

    return equipe


def menu_epreuves():
    print("\n======||======== MENU DES EPREUVES ======||========")
    print("1 - Epreuves mathematiques")
    print("2 - Epreuves de hasard")
    print("3 - Epreuves logiques")
    print("4 - Enigmes du Pere Fouras")
    print("0 - Quitter le jeu")
    print("=======||=============||===============||============")

    choix = ""
    while choix not in ["1", "2", "3", "4", "0"]:
        choix = input("Ton choix : ").strip()
        if choix not in ["1", "2", "3", "4", "0"]:
            print("Choix invalide, merci de saisir 0, 1, 2, 3 ou 4.")

    return int(choix)


def choisir_joueur(equipe):
    print("\nQuel joueur va participer a cette epreuve ?")
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

    joueur_choisi = equipe[int(selection) - 1]
    print("Le joueur selectionne est : " + joueur_choisi['nom'])
    return joueur_choisi
