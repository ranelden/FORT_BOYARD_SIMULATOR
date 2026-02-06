from fonctions_utiles import introduction, composer_equipe, menu_epreuves, choisir_joueur
from epreuve_finale import salle_de_tresor
""
def main():
    introduction()
    equipe = composer_equipe()

    while True:
        choix = menu_epreuves()
        if choix == "quitter":
            print("Merci d'avoir joué, à bientôt dans le Fort !")
            break

        joueur = choisir_joueur(equipe)
        print(f"(Ici on lancerait l'épreuve {choix} pour {joueur['nom']})")
        # plus tard : appel à epreuves_mathématiques, hasard, etc.

if __name__ == "__main__":
    main()
