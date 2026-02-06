import random
from pathlib import Path
from epreuve_finale import salle_de_tresor
from enigme_pere_fouras import enigme_pere_fouras
#from epreuves_mathematiques import epreuve_math
#from epreuves_logiques import epreuve_logique
#from epreuves_hasard import epreuve_hasard
"""fait pas cyril dabernard"""


def introduction():
    print("\n" + "="*70)
    print(" " * 20 + "BIENVENUE A FORT BOYARD")
    print("="*70)
    print("\nREGLES DU JEU :")
    print("-" * 70)
    print("Vous devez accomplir des epreuves pour gagner des cles.")
    print("Objectif : Collecter 3 cles pour acceder a la salle du tresor.")
    print("\nTypes d'epreuves disponibles :")
    print("  1. Epreuves de Mathematiques")
    print("  2. Epreuves de Logique")
    print("  3. Epreuves du Hasard")
    print("  4. Enigme du Pere Fouras")
    print("\nChaque epreuve reussie vous rapporte 1 cle.")
    print("-" * 70 + "\n")


def composer_equipe(): # erreur avec leader
    equipe = []
    
    while True:
        try:
            nb_joueurs = int(input("Combien de joueurs dans l'equipe (1 a 3) ? "))
            if 1 <= nb_joueurs <= 3:
                break
            else:
                print("Erreur : L'equipe doit comporter entre 1 et 3 joueurs.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")

    has_leader = False
    for i in range(nb_joueurs):
        print(f"--- Joueur {i + 1} ---")
        nom = input("Nom du joueur : ").strip()
        profession = input("Profession : ").strip()

        if i == nb_joueurs - 1 and not has_leader:
            print("Le dernier joueur doit etre le leader de l'equipe.")
            input("Appuyez sur Entree pour continuer...")
            est_leader = True
            has_leader = True
        
        if not has_leader:
            leader_reponse = input("Est-ce le leader de l'equipe ? (oui/non) : ").strip().lower()
            if leader_reponse == "oui":
                has_leader = True
                est_leader = True
            else:
                est_leader = False
        
        joueur = {
            'nom': nom,
            'profession': profession,
            'leader': est_leader,
            'cles_gagnees': 0
        }
        equipe.append(joueur)
        print()
    
    if not any(j['leader'] for j in equipe):
        equipe[0]['leader'] = True
        print(f"{equipe[0]['nom']} est designe(e) comme leader par defaut.\n")
    
    return equipe


def afficher_equipe(equipe):
    print("\n" + "="*70)
    print("COMPOSITION DE L'EQUIPE")
    print("="*70)
    for i, joueur in enumerate(equipe, 1):
        role = "Leader" if joueur['leader'] else "Membre"
        print(f"{i}. {joueur['nom']} ({joueur['profession']}) - {role}")
        print(f"   Cles gagnees : {joueur['cles_gagnees']}")
    print("="*70 + "\n")


def choisir_joueur(equipe):
    print("\n--- Selection du joueur pour l'epreuve ---")
    for i, joueur in enumerate(equipe, 1):
        role = "Leader" if joueur['leader'] else "Membre"
        print(f"{i}. {joueur['nom']} ({joueur['profession']}) - {role}")
    
    while True:
        try:
            choix = int(input("\nEntrez le numero du joueur : "))
            if 1 <= choix <= len(equipe):
                joueur_choisi = equipe[choix - 1]
                print(f"\n{joueur_choisi['nom']} a ete selectionne(e) pour cette epreuve.\n")
                return joueur_choisi
            else:
                print(f"Erreur : Choisissez un numero entre 1 et {len(equipe)}.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")


def menu_epreuves():
    print("\n" + "="*70)
    print("MENU DES EPREUVES")
    print("="*70)
    print("1. Epreuve de Mathematiques")
    print("2. Epreuve de Logique")
    print("3. Epreuve du Hasard")
    print("4. Enigme du Pere Fouras")
    print("="*70)
    
    while True:
        try:
            choix = int(input("\nChoix : "))
            if 1 <= choix <= 4:
                return choix
            else:
                print("Erreur : Choisissez un numero entre 1 et 4.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")


def epreuve_math():
    pass


def epreuve_logique():
    pass


def epreuve_hasard():
    pass


def salle_de_tresor():
    pass


def calculer_total_cles(equipe):
    return sum(joueur['cles_gagnees'] for joueur in equipe)


def main():
    introduction()
    
    input("Appuyez sur Entree pour commencer l'aventure...")
    
    equipe = composer_equipe()
    afficher_equipe(equipe)
    
    input("Appuyez sur Entree pour continuer...")
    
    cles_requises = 3
    epreuves_completees = 0
    
    print("\n" + "="*70)
    print("DEBUT DES EPREUVES")
    print("="*70)
    print(f"Objectif : Collecter {cles_requises} cles\n")
    
    while calculer_total_cles(equipe) < cles_requises:
        print(f"\nCles collectees par l'equipe : {calculer_total_cles(equipe)}/{cles_requises}")
        print(f"Epreuves completees : {epreuves_completees}\n")
        
        joueur_actuel = choisir_joueur(equipe)
        choix_epreuve = menu_epreuves()
        
        input("\nAppuyez sur Entree pour commencer l'epreuve...")
        
        resultat = False
        
        if choix_epreuve == 1:
            resultat = epreuve_math()
        elif choix_epreuve == 2:
            resultat = epreuve_logique()
        elif choix_epreuve == 3:
            resultat = epreuve_hasard()
        elif choix_epreuve == 4:
            resultat = enigme_pere_fouras()
        
        if resultat:
            joueur_actuel['cles_gagnees'] += 1
            print(f"\n{joueur_actuel['nom']} remporte une cle !")
        else:
            print(f"\n{joueur_actuel['nom']} n'a pas gagne de cle.")
        
        epreuves_completees += 1
        
        afficher_equipe(equipe)
        
        if calculer_total_cles(equipe) >= cles_requises:
            print("\n" + "="*70)
            print("OBJECTIF ATTEINT !")
            print("="*70)
            print(f"L'equipe a collecte {calculer_total_cles(equipe)} cles.")
            print("Vous pouvez maintenant acceder a la salle du tresor !")
            print("="*70 + "\n")
            break
        
        continuer = input("\nContinuer les epreuves ? (oui/non) : ").strip().lower()
        if continuer != "oui":
            print("\nL'aventure s'arrete ici.")
            break
    
    if calculer_total_cles(equipe) >= cles_requises:
        input("\nAppuyez sur Entree pour tenter l'epreuve finale...")
        victoire_finale = salle_de_tresor()
        
        if victoire_finale:
            print("\n" + "="*70)
            print("FELICITATIONS !")
            print("="*70)
            print("Votre equipe a reussi a ouvrir la salle du tresor !")
            print("Vous repartez avec le tresor de Fort Boyard !")
            print("="*70 + "\n")
        else:
            print("\nDommage, vous n'avez pas reussi l'epreuve finale.")
    
    print("\n" + "="*70)
    print("RECAPITULATIF DE L'AVENTURE")
    print("="*70)
    print(f"Epreuves completees : {epreuves_completees}")
    print(f"Cles collectees : {calculer_total_cles(equipe)}/{cles_requises}")
    print("\nPerformances individuelles :")
    for joueur in equipe:
        print(f"  - {joueur['nom']} : {joueur['cles_gagnees']} cle(s)")
    print("="*70)
    print("\nMerci d'avoir joue a Fort Boyard !")
    print("="*70 + "\n")


if __name__ == '__main__':
    try : 
        main()
    except KeyboardInterrupt:
        print("\n\nL'aventure a ete interrompue par l'utilisateur.")
        print("Merci d'avoir joue a Fort Boyard !")