import json
import random
from pathlib import Path

def charger_enigmes():
    racine = Path(__file__).resolve().parent
    chemin_fichier = racine / "data" / "enigmesPF.json"
    
    if not chemin_fichier.exists():
        print(f"Erreur : Le fichier {chemin_fichier} est introuvable.")
        return []

    with open(chemin_fichier, "r", encoding="utf-8") as f:
        enigmes = json.load(f)
        
    if not isinstance(enigmes, list) or len(enigmes) == 0:
        print("Erreur : Le fichier d'énigmes est vide ou mal formé.")
        return []
        
    return enigmes

def enigme_pere_fouras():
    print("\n" + "="*70)
    print("LE PÈRE FOURAS VOUS ACCUEILLE DANS SA VIGIE")
    print("="*70)
    print("Vous avez 3 tentatives pour trouver la réponse et gagner une clé.")
    print("="*70 + "\n")
    
    enigmes = charger_enigmes()
    
    if not enigmes:
        print("Erreur : Impossible de lancer l'épreuve (données absentes).")
        return False
    
    enigme_choisie = random.choice(enigmes)
    question = enigme_choisie.get("question", "")
    reponse_correcte = enigme_choisie.get("reponse", "")
    
    if question == "" or reponse_correcte == "":
        print("Erreur : L'énigme sélectionnée est incomplète.")
        return False
        
    print("Le Père Fouras dit :")
    print(question)
    print("Faites attention aux accents et à la ponctuation !")
    
    nombre_tentatives = 3
    
    for tentative in range(1, nombre_tentatives + 1):
        print(f"\nTentative {tentative}/{nombre_tentatives}")
        reponse_joueur = input("Votre réponse : ").strip()
        
        if reponse_joueur.lower() == reponse_correcte.lower():
            print("\n" + "="*70)
            print("BRAVO ! Vous avez trouvé la bonne réponse !")
            print("Le Père Fouras vous remet une clé.")
            print("="*70 + "\n")
            return True
        else:
            tentatives_restantes = nombre_tentatives - tentative
            if tentatives_restantes > 0:
                print(f"Mauvaise réponse. Il vous reste {tentatives_restantes} tentative(s).")
    
    print("\n" + "="*70)
    print("ÉCHEC ! Vous n'avez plus de tentatives.")
    print(f"La bonne réponse était : {reponse_correcte}")
    print("="*70 + "\n")
    return False

if __name__ == "__main__":
    print("--- DÉBUT DE LA BATTERIE DE TESTS (ÉNIGMES) ---")
    
    liste_test = charger_enigmes()
    if liste_test:
        print(f"Test 1 (Chargement) : OK ({len(liste_test)} énigmes trouvées)")
        
        test_e = liste_test[0]
        if "question" in test_e and "reponse" in test_e:
            print("Test 2 (Structure des données) : OK")
        else:
            print("Test 2 (Structure des données) : ERREUR")
    else:
        print("Test 1 (Chargement) : ERREUR")

    print("\n--- TEST DU GAMEPLAY ---")
    resultat = enigme_pere_fouras()
    print(f"Test terminé. Résultat renvoyé : {resultat}")