import json
import random
"""fait par Cyril Dabernard"""

def charger_enigmes(fichier="data/enigmesPF.json"):

#    Charge les enigmes depuis data
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            enigmes = json.load(f)
            return enigmes
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fichier}' est introuvable.")
        return []
    except json.JSONDecodeError:
        print("Erreur : Format JSON invalide.")
        return []


def enigme_pere_fouras(fichier="data/enigmesPF.json"):


    print("\n" + "="*70)
    print("LE PERE FOURAS VOUS ACCUEILLE DANS SA VIGIE")
    print("="*70)
    print("Vous avez 3 tentatives pour trouver la reponse et gagner une cle.")
    print("="*70 + "\n")
    
    enigmes = charger_enigmes(fichier)
    
    if not enigmes:
        print("Impossible de charger les enigmes.")
        return False
    
    enigme_choisie = random.choice(enigmes)
    question = enigme_choisie.get('question', '')
    reponse_correcte = enigme_choisie.get('reponse', '')
    
    if not question or not reponse_correcte:
        print("Enigme incomplete.")
        return None # verifie none pour gerer exeption
        
    
    print("Le Pere Fouras dit :")
    print(question)
    print(" faite attention aux accents et a la ponctuation !")
    
    nombre_tentatives = 3
    
    for tentative in range(1, nombre_tentatives + 1):
        print(f"Tentative {tentative}/{nombre_tentatives}")
        reponse_joueur = input("Votre reponse : ").strip()
        
        if reponse_joueur.lower() == reponse_correcte.lower():
            print("\n" + "="*70)
            print("BRAVO ! Vous avez trouve la bonne reponse !")
            print("Le Pere Fouras vous remet une cle.")
            print("="*70 + "\n")
            return True
        else:
            tentatives_restantes = nombre_tentatives - tentative
            if tentatives_restantes > 0:
                print(f"Mauvaise reponse. Il vous reste {tentatives_restantes} tentative(s).\n")
    
    print("\n" + "="*70)
    print("ECHEC ! Vous n'avez plus de tentatives.")
    print(f"La bonne reponse etait : {reponse_correcte}")
    print("="*70 + "\n")
    return False


if __name__ == "__main__":
    print("\nTest du module enigme_pere_fouras\n")
    resultat = enigme_pere_fouras()
    print(f"\nResultat : {'Reussi' if resultat else 'Echoue'}")
