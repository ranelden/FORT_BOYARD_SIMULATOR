import json
import random
import os

def salle_de_tresor():
    if not os.path.isfile("data/indicesSalle.json"):
        print(" Fichier data/indicesSalle.json introuvable.")
        return False

    f = open("data/indicesSalle.json", "r", encoding="utf-8")
    data = json.load(f)
    f.close()

    if isinstance(data, dict) and "codes" in data:
        codes = data["codes"]
    elif isinstance(data, list):
        codes = data
    else:
        print(" Format de données non reconnu dans indicesSalle.json.")
        return False

    if not codes:
        print(" Aucun code disponible dans indicesSalle.json.")
        return False

    code = random.choice(codes)
    mot_code = code.get("mot", "").strip().upper()
    indices = code.get("indices", [])

    print("\n=======||||||||========== SALLE DU TRESOR ========|||||||=========")
    print("Tu as obtenu l'accès à la salle du trésor !")
    print("Tu vas recevoir plusieurs indices pour trouver le mot-code.")
    print("Tu as 3 essais maximum. Bonne chance !")
    print("======||||==========||||=================|||||===================\n")

    for i, indice in enumerate(indices, start=1):
        print(f"Indice {i} : {indice}")

    essais_restants = 3
    while essais_restants > 0:
        proposition = input(f"\nTon mot-code (il te reste {essais_restants} essai(s)) : ").strip().upper()

        if proposition == mot_code:
            print("\n Bravo ! Tu as trouvé le mot-code et libéré le trésor !")
            return True
        else:
            print(" Ce n'est pas le bon mot-code...")
            essais_restants -= 1

    print("\n Tu as épuisé tous tes essais. Le trésor restera fermé.")
    print(f"Le mot-code était : {mot_code}")
    return False
