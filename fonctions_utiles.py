import random
from pathlib import Path
import datetime

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
    a_deja_un_leader = False

    for i in range(1, nb + 1):
        print("\n--- Joueur", i, "---")
        nom = input("Nom du joueur : ").strip()
        while nom == "":
            print("Le nom ne peut pas etre vide.")
            nom = input("Nom du joueur : ").strip()

        profession = input("Profession du joueur : ").strip()

        role_input = "non"
        if not a_deja_un_leader:
            while True:
                role_input = input("Est-ce le leader de l'equipe ? (oui/non) : ").strip().lower()
                if role_input in ["oui", "non"]:
                    if role_input == "oui":
                        a_deja_un_leader = True
                    break
                print("Repondez par 'oui' ou 'non'.")

        joueur = {
            "nom": nom,
            "profession": profession,
            "leader": (role_input == "oui"),
            "cles_gagnees": 0
        }
        equipe.append(joueur)

    if not a_deja_un_leader:
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

def enregistrer_historique(nom_epreuve, nom_joueur, resultat):
    racine = Path(__file__).resolve().parent
    dossier_output = racine / "output"
    
    if not dossier_output.exists():
        dossier_output.mkdir()
    
    fichier_h = dossier_output / "historique.txt"
    res_str = "SUCCES" if resultat else "ECHEC"

    maintenant = datetime.datetime.now()
    date_formatee = maintenant.strftime("%d/%m/%Y %H:%M:%S")
    
    with open(fichier_h, "a", encoding="utf-8") as f:
        ligne = "[" + date_formatee + "] "
        ligne += "Joueur: " + nom_joueur.ljust(15) + " | "
        ligne += "Epreuve: " + nom_epreuve.ljust(20) + " | "
        ligne += "Resultat: " + res_str + "\n"
        f.write(ligne)


if __name__ == "__main__":
    print("--- DÉBUT DE LA BATTERIE DE TESTS (UTILITAIRES) ---")

    # Test 1 : Composition d'équipe
    print("\nTest 1 : Création de l'équipe")
    ma_super_equipe = composer_equipe()
    print(f"Équipe créée avec {len(ma_super_equipe)} joueurs.")

    # Test 2 : Sélection de joueur
    print("\nTest 2 : Sélection d'un joueur")
    joueur = choisir_joueur(ma_super_equipe)
    print(f"Vérification : {joueur['nom']} a été bien récupéré.")

    # Test 3 : Enregistrement historique
    print("\nTest 3 : Écriture dans l'historique")
    enregistrer_historique("Test Technique", ma_super_equipe[0]['nom'], True)
    
    racine_test = Path(__file__).resolve().parent
    fichier_test = racine_test / "output" / "historique.txt"
    
    if fichier_test.exists():
        print(f"Succès : Le fichier {fichier_test} a été mis à jour.")
    else:
        print("Erreur : Le fichier d'historique n'a pas été créé.")

    print("\n--- FIN DES TESTS ---")