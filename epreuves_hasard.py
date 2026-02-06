import random

def bonneteau():
    print("\n=== ÉPREUVE DU BONNETEAU ===")
    print("La clé est cachée sous l'un des trois bonneteaux (A, B ou C).")
    print("Vous avez 2 essais pour la trouver !\n")
    
    bonneteaux = ['A', 'B', 'C']
    bonneteau_avec_cle = random.choice(bonneteaux)
    essais_restants = 2
    
    while essais_restants > 0:
        print(f"Il vous reste {essais_restants} essai(s).")
        choix = input("Sous quel bonneteau se cache la clé ? (A, B ou C) : ").upper().strip()
        
        while choix not in bonneteaux:
            print("Choix invalide ! Veuillez choisir A, B ou C.")
            choix = input("Sous quel bonneteau se cache la clé ? (A, B ou C) : ").upper().strip()
        
        if choix == bonneteau_avec_cle:
            print("Félicitations ! Vous avez trouvé la clé !\n")
            return True
        else:
            essais_restants -= 1
            print(f"Dommage ! La clé n'était pas sous le bonneteau {choix}.\n")
    
    print(f"Vous avez épuisé vos essais. La clé était sous le bonneteau {bonneteau_avec_cle}.\n")
    return False

def jeu_lance_des():
    print("\n=== ÉPREUVE DU LANCER DE DÉS ===")
    print("Vous et le maître du jeu lancez chacun deux dés.")
    print("Le premier à obtenir un 6 remporte la partie !")
    print("Vous avez 3 essais maximum.\n")
    
    essais_max = 3
    
    for essai in range(1, essais_max + 1):
        print(f"--- Essai {essai} ---")
        input("Appuyez sur Entrée pour lancer vos dés...")

        des_joueur = (random.randint(1, 6), random.randint(1, 6))
        print(f"Vos dés : {des_joueur[0]} et {des_joueur[1]}")
        
        if 6 in des_joueur:
            print("\n🎉 Vous avez obtenu un 6 ! Vous gagnez !")
            return True

        print("Le maître du jeu lance ses dés...")
        des_maitre = (random.randint(1, 6), random.randint(1, 6))
        print(f"Dés du maître : {des_maitre[0]} et {des_maitre[1]}")
        
        if 6 in des_maitre:
            print("\n Le maître du jeu a obtenu un 6 ! Vous perdez.")
            return False
        
        print("Personne n'a obtenu de 6 cette fois.\n")
    
    print("Match nul après 3 essais ! Vous perdez cette épreuve.\n")
    return False

def epreuve_hasard():
    epreuves = [bonneteau, jeu_lance_des]
    epreuve = random.choice(epreuves)
    return epreuve()

if __name__ == "__main__":
    resultat = epreuve_hasard()
    if resultat:
        print("Vous avez réussi l'épreuve !")
    else:
        print("Vous avez échoué l'épreuve !")