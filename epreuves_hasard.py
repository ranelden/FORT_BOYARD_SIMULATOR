import random

def bonneteau():
    print("\n=== EPREUVE DU BONNETEAU ===")
    print("La cle est cachee sous l'un des trois bonneteaux (A, B ou C).")
    print("Vous avez 2 essais pour la trouver !\n")
    
    bonneteaux = ['A', 'B', 'C']
    bonneteau_avec_cle = random.choice(bonneteaux)
    essais_restants = 2
    
    while essais_restants > 0:
        print("Il vous reste " + str(essais_restants) + " essai(s).")
        
        choix = ""
        while choix not in bonneteaux:
            saisie = input("Sous quel bonneteau se cache la cle ? (A, B ou C) : ").strip().upper()
            
            if len(saisie) != 1:
                print("Erreur : Vous devez entrer une seule lettre (A, B ou C).")
            elif saisie not in bonneteaux:
                print("Erreur : Choix invalide ! Veuillez choisir A, B ou C.")
            else:
                choix = saisie
        
        if choix == bonneteau_avec_cle:
            print("Felicitations ! Vous avez trouve la cle !\n")
            return True
        else:
            essais_restants -= 1
            print("Dommage ! La cle n'etait pas sous le bonneteau " + choix + ".\n")
    
    print("Vous avez epuise vos essais. La cle était sous le bonneteau " + bonneteau_avec_cle + ".\n")
    return False

def jeu_lance_des():
    print("\n=== EPREUVE DU LANCER DE DES ===")
    print("Vous et le maitre du jeu lancez chacun deux des.")
    print("Le premier a obtenir un 6 remporte la partie !")
    print("Vous avez 3 essais maximum.\n")
    
    essais_max = 3
    
    for essai in range(1, essais_max + 1):
        print("--- Essai " + str(essai) + " ---")
        input("Appuyez sur Entree pour lancer vos des...")

        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        print("Vos des : " + str(d1) + " et " + str(d2))
        
        if d1 == 6 or d2 == 6:
            print("\nVous avez obtenu un 6 ! Vous gagnez !")
            return True

        print("Le maitre du jeu lance ses des...")
        m1 = random.randint(1, 6)
        m2 = random.randint(1, 6)
        print("Des du maitre : " + str(m1) + " et " + str(m2))
        
        if m1 == 6 or m2 == 6:
            print("\nLe maitre du jeu a obtenu un 6 ! Vous perdez.")
            return False
        
        print("Personne n'a obtenu de 6 cette fois.\n")
    
    print("Match nul apres 3 essais ! Vous perdez cette epreuve.\n")
    return False

def epreuve_hasard():
    epreuves = [bonneteau, jeu_lance_des]
    epreuve = random.choice(epreuves)
    return epreuve()

if __name__ == "__main__":
    print("--- TEST DU MODULE HASARD ---")
    print("1. Test de l'epreuve Bonneteau")
    res1 = bonneteau()
    print("Resultat Bonneteau : " + str(res1))
    
    print("\n2. Test de l'epreuve Lancer de des")
    res2 = jeu_lance_des()
    print("Resultat Des : " + str(res2))
    
    print("\n3. Test de la selection aleatoire (epreuve_hasard)")
    res3 = epreuve_hasard()
    print("Resultat selection aleatoire : " + str(res3))