import json
import random
def salle_de_tresor():
    """
    Charge les indices depuis data/indicesSalle.json,
    choisit un code au hasard et laisse 3 essais pour trouver le mot-code.
    Retourne True si le mot est trouvé, False sinon.
    """
    # 1. Charger le fichier JSON
    try:
        with open("data/indicesSalle.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ Fichier data/indicesSalle.json introuvable.")
        return False
    except json.JSONDecodeError:
        print("❌ Erreur de lecture du fichier JSON.")
        return False

    # data doit contenir une liste de codes ou un dict -> on s'adapte
    # Exemple attendu : {"codes": [{"mot": "TIGRE", "indices": ["...", "..."]}, ...]}
    if isinstance(data, dict) and "codes" in data:
        codes = data["codes"]
    elif isinstance(data, list):
        codes = data
    else:
        print("❌ Format de données non reconnu dans indicesSalle.json.")
        return False

    if not codes:
        print("❌ Aucun code disponible dans indicesSalle.json.")
        return False

    # 2. Choisir un code au hasard
    code = random.choice(codes)  # nécessite une liste non vide
    mot_code = code.get("mot", "").strip().upper()
    indices = code.get("indices", [])

    print("\n================= SALLE DU TRESOR =================")
    print("Tu as obtenu l'accès à la salle du trésor !")
    print("Tu vas recevoir plusieurs indices pour trouver le mot-code.")
    print("Tu as 3 essais maximum. Bonne chance !")
    print("====================================================\n")

    # 3. Afficher les indices un par un
    for i, indice in enumerate(indices, start=1):
        print(f"Indice {i} : {indice}")

    # 4. Donner 3 essais au joueur
    essais_restants = 3
    while essais_restants > 0:
        proposition = input(f"\nTon mot-code (il te reste {essais_restants} essai(s)) : ").strip().upper()

        if proposition == mot_code:
            print("\n✅ Bravo ! Tu as trouvé le mot-code et libéré le trésor !")
            return True
        else:
            print("❌ Ce n'est pas le bon mot-code...")
            essais_restants -= 1

    print("\n⛔ Tu as épuisé tous tes essais. Le trésor restera fermé.")
    print(f"Le mot-code était : {mot_code}")
    return False
