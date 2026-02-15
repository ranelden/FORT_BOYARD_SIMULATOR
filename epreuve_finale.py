import json
import random
from pathlib import Path

def salle_de_tresor():
    racine = Path(__file__).resolve().parent
    chemin_fichier = racine / "data" / "indicesSalle.json"
    
    if not chemin_fichier.exists():
        print("Erreur : Le fichier " + str(chemin_fichier) + " est introuvable.")
        return False

    with open(chemin_fichier, "r", encoding="utf-8") as f:
        data = json.load(f)

    donnees_fort = data.get("Fort Boyard", {})
    if not donnees_fort:
        print("Erreur : Format de donnees invalide.")
        return False

    annees = list(donnees_fort.keys())
    annee_choisie = random.choice(annees)
    
    emissions = list(donnees_fort[annee_choisie].keys())
    emission_choisie = random.choice(emissions)
    
    jeu_donnees = donnees_fort[annee_choisie][emission_choisie]
    
    mot_code = jeu_donnees["MOT-CODE"]
    indices = jeu_donnees["Indices"]
    
    print("\n" + "="*50)
    print("       BIENVENUE DANS LA SALLE DU TRESOR")
    print("="*50)
    print("Tu as obtenu l'acces a la salle du tresor !")
    print("Voici les 3 premiers indices pour deviner le mot-code :")
    print("1. " + indices[0])
    print("2. " + indices[1])
    print("3. " + indices[2])
    print("-" * 50)
    
    essais = 3
    gagne = False
    indice_actuel = 3
    
    while essais > 0 and not gagne:
        print("\nTentatives restantes : " + str(essais))
        proposition = input("Votre proposition : ").strip().upper()
        
        if proposition == mot_code.upper():
            gagne = True
        else:
            essais -= 1
            if essais > 0:
                print("\nCe n'est pas le bon mot-code.")
                if indice_actuel < len(indices):
                    print("Voici un nouvel indice :")
                    print("-> " + indices[indice_actuel])
                    indice_actuel += 1
                print("-" * 50)

    print("\n" + "="*50)
    if gagne:
        print("BRAVO ! Tu as trouve le mot-code et libere le tresor !")
        resultat = True
    else:
        print("ECHEC ! Tu as epuise tous tes essais.")
        print("Le mot-code etait : " + mot_code)
        resultat = False
    print("="*50 + "\n")
    
    return resultat