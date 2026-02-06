import random
from pathlib import Path
from fonctions_utiles import introduction, composer_equipe, choisir_joueur, menu_epreuves
from epreuve_finale import salle_de_tresor
from enigme_pere_fouras import enigme_pere_fouras
from epreuves_mathematiques import epreuve_math
#from epreuves_logiques import epreuve_logique
from epreuves_hasard import epreuve_hasard
"""fait pas cyril dabernard"""

RACINE = Path(__file__).resolve().parent

def afficher_equipe(equipe):
    print("\n" + "="*70)
    print("COMPOSITION DE L'EQUIPE")
    print("="*70)
    for i, joueur in enumerate(equipe, 1):
        role = "Leader" if joueur['leader'] else "Membre"
        print(f"{i}. {joueur['nom']} - {role}")
        print(f"   Cles gagnees : {joueur['cles_gagnees']}")
    print("="*70 + "\n")

def epreuve_logique():
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
    try : # j'ai is ca car j'ai aps envie d avoir des erreur a chaque fois que je fais ctrl+c pour arreter le programme
        main()
    except KeyboardInterrupt:
        print("\n\nL'aventure a ete interrompue par l'utilisateur.")
        print("Merci d'avoir joue a Fort Boyard !")