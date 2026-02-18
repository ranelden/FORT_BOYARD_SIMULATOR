from pathlib import Path
from fonctions_utiles import introduction, composer_equipe, choisir_joueur, menu_epreuves, enregistrer_historique
from epreuve_finale import salle_de_tresor
from enigme_pere_fouras import enigme_pere_fouras
from epreuves_mathematiques import epreuve_math
from epreuves_hasard import epreuve_hasard
from epreuves_logiques import epreuve_logique

def afficher_equipe(equipe):
    print("\n" + "="*70)
    print("COMPOSITION DE L'EQUIPE")
    print("="*70)
    for i, joueur in enumerate(equipe, 1):
        role = "Leader" if joueur['leader'] else "Membre"
        print(str(i) + ". " + joueur['nom'] + " (" + joueur['profession'] + ") - " + role)
        print("   Cles gagnees : " + str(joueur['cles_gagnees']))
    print("="*70 + "\n")


def calculer_total_cles(equipe):
    total = 0
    for joueur in equipe:
        total += joueur['cles_gagnees']
    return total

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
    print("Objectif : Collecter " + str(cles_requises) + " cles\n")
    
    while calculer_total_cles(equipe) < cles_requises:
        print("\nCles collectees par l'equipe : " + str(calculer_total_cles(equipe)) + "/" + str(cles_requises))
        print("Epreuves completees : " + str(epreuves_completees) + "\n")
        
        joueur_actuel = choisir_joueur(equipe)
        choix_epreuve = menu_epreuves()
        
        if choix_epreuve == 0:
            print("\nL'aventure s'arrete ici.")
            break
        
        input("\nAppuyez sur Entree pour commencer l'epreuve...")
        
        resultat = False
        nom_epreuve = ""
        
        if choix_epreuve == 1:
            nom_epreuve = "Mathematiques"
            resultat = epreuve_math()
        elif choix_epreuve == 2:
            nom_epreuve = "Hasard"
            resultat = epreuve_hasard()
        elif choix_epreuve == 3:
            nom_epreuve = "Logique"
            resultat = epreuve_logique()
        elif choix_epreuve == 4:
            nom_epreuve = "Pere Fouras"
            resultat = enigme_pere_fouras()
        
        if resultat:
            joueur_actuel['cles_gagnees'] += 1
            print("\n" + joueur_actuel['nom'] + " remporte une cle !")
        else:
            print("\n" + joueur_actuel['nom'] + " n'a pas gagne de cle.")
        
        if nom_epreuve != "":
            enregistrer_historique(nom_epreuve, joueur_actuel['nom'], resultat)
        
        epreuves_completees += 1
        afficher_equipe(equipe)
        
        if calculer_total_cles(equipe) >= cles_requises:
            print("\n" + "="*70)
            print("OBJECTIF ATTEINT !")
            print("="*70)
            print("L'equipe a collecte " + str(calculer_total_cles(equipe)) + " cles.")
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
        
        enregistrer_historique("Salle du Tresor", "Equipe", victoire_finale)
        
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
    print("Epreuves completees : " + str(epreuves_completees))
    print("Cles collectees : " + str(calculer_total_cles(equipe)) + "/" + str(cles_requises))
    print("\nPerformances individuelles :")
    for joueur in equipe:
        print("  - " + joueur['nom'] + " : " + str(joueur['cles_gagnees']) + " cle(s)")
    print("="*70)
    print("\nMerci d'avoir joue a Fort Boyard !")
    print("="*70 + "\n")

def demo_scenario():

    import random
    from epreuves_logiques import jeu_nim, jeu_tictactoe, jeu_bataille_navale
    from enigme_pere_fouras import enigme_pere_fouras
    from epreuves_mathematiques import epreuve_math_equation, epreuve_math_factorielle, epreuve_math_premier, epreuve_roulette_mathematique
    from epreuves_hasard import bonneteau, jeu_lance_des
    from epreuve_finale import salle_de_tresor
    from fonctions_utiles import composer_equipe

    print("\n" + "!"*70)
    print("DEMONSTRATION COMPLETE DU FORT BOYARD SIMULATOR")
    print("!"*70)

    print("\n[ETAPE 1] : Création de l'équipe")
    equipe = composer_equipe()
    input("Appuyez sur Entree pour continuer...")
    afficher_equipe(equipe)
    print(f"vous avez choisi : {menu_epreuves()}")
    input("Appuyez sur Entree pour continuer...")

    print("\n[ETAPE 2] : Jeu de NIM (Bâtonnets)")
    jeu_nim()
    input("Appuyez sur Entree pour continuer...")
    
    print("\n[ETAPE 3] : Morpion (Tic-Tac-Toe)")
    jeu_tictactoe()
    input("Appuyez sur Entree pour continuer...")

    print("\n[ETAPE 4] : Bataille Navale")
    jeu_bataille_navale()
    input("Appuyez sur Entree pour continuer...")

    print("\n[ETAPE 5] : Énigme du Père Fouras (Force la 1ère énigme)")
    original_choice = random.choice
    random.choice = lambda x: x[0] 
    enigme_pere_fouras()
    random.choice = original_choice
    input("Appuyez sur Entree pour continuer...")

    print("\n[ETAPE 6] : Épreuves Mathématiques (Equation et Factorielle)")
    epreuve_math_equation()
    input("Appuyez sur Entree pour continuer...")
    epreuve_math_factorielle()
    input("Appuyez sur Entree pour continuer...")
    epreuve_roulette_mathematique()
    input("Appuyez sur Entree pour continuer...")
    epreuve_math_premier()  
    input("Appuyez sur Entree pour continuer...")

    print("\n[ETAPE 7] : Épreuves de Hasard (Bonneteau)")
    bonneteau()
    input("Appuyez sur Entree pour continuer...")
    jeu_lance_des()
    input("Appuyez sur Entree pour continuer...")

    print("\n[ETAPE 8] : Salle du Trésor (Indices JSON)")
    salle_de_tresor()
    input("Appuyez sur Entree pour continuer...")

    return True

if __name__ == '__main__':
    print("1. Lancer le jeu normalement")
    print("2. Lancer la démonstration complète (Scénario)")
    choix = input("Votre choix : ")
    
    if choix == "2":
        demo_scenario()
    else:
        main()



