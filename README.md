Voici une proposition de fichier `README.md` complet et bien formaté pour votre projet GitHub, basée sur les fichiers sources et les consignes du sujet.

---

# Fort Boyard Simulator

## 1. Présentation Générale

### Contributeurs

* **Socning Saffo Loïc** : Développement des fonctions utilitaires, de l'épreuve finale et rédaction de la documentation.
* **Cyril Dabernard** : [Répartition à compléter]
* **Rayane Gareh** : [Répartition à compléter]
* **Clement Vienot** : [Répartition à compléter]
* **Axil Meddahi** : [Répartition à compléter]
* **Youcef** : [Répartition à compléter]

### Description

Ce projet est une simulation interactive en Python du célèbre jeu télévisé **Fort Boyard**. Il a été réalisé dans le cadre du module "Développement en Python" (XICS403). L'objectif est de constituer une équipe de joueurs, de réussir une série d'épreuves pour collecter des clés, et enfin d'accéder à la salle du trésor.

### Fonctionnalités Principales


**Constitution d'équipe** : Création d'une équipe de 1 à 3 joueurs avec noms, professions et rôles (leader/membre).


**Gestion des épreuves** : Quatre types d'épreuves (Mathématiques, Hasard, Logique et Énigmes du Père Fouras).


**Collecte de clés** : Chaque épreuve réussie rapporte une clé ; 3 clés sont nécessaires pour l'épreuve finale.


**Épreuve finale** : Recherche d'un mot-code à l'aide d'indices stockés dans un fichier JSON.


**Historique (Bonus)** : Enregistrement des performances des joueurs dans un fichier `historique.txt`.



### Technologies Utilisées

* **Langage** : Python 3.

**Formats de données** : JSON pour les énigmes et indices.


* **Bibliothèques standards** : `random`, `json`, `pathlib`, `datetime`.

---

## 2. Installation et Utilisation

### Installation

1. **Cloner le dépôt** :
```bash
git clone https://github.com/ranelden/FORT_BOYARD_SIMULATOR

```


2. **Se déplacer dans le dossier** :
```bash
cd FORT_BOYARD_SIMULATOR

```



### Utilisation

Lancez simplement le script principal :

```bash
python main.py

```

Le jeu vous guidera ensuite à travers les étapes de création de l'équipe et de sélection des épreuves.

---

## 3. Documentation Technique

### Algorithme du jeu

1. Affichage de l'introduction et des règles.


2. Configuration de l'équipe (nombre de joueurs, noms, rôles).


3. Boucle de jeu (tant que l'équipe possède moins de 3 clés):


* Choix d'un joueur participant.
* Sélection d'un type d'épreuve.
* Lancement d'une épreuve aléatoire du type choisi.
* Mise à jour du compteur de clés en cas de succès.


4. Lancement de l'épreuve finale de la salle du trésor.


5. Affichage du récapitulatif et enregistrement de l'historique.



### Détails des modules et fonctions principales de chaque modules

| Module | Fonction | Rôle |
| --- | --- | --- |
| `main.py` | `main()` | Orchestre le déroulement global du simulateur.
| `fonctions_utiles.py` | `composer_equipe()` | Gère la saisie des informations des joueurs.
| `epreuves_mathematiques.py` | `epreuve_math()` | Propose factorielles, équations, ou nombres premiers.
| `epreuves_hasard.py` | `epreuve_hasard()` | Gère le Bonneteau ou le Lancer de dés.
| `epreuves_logiques.py` | `epreuve_logique()` | Implémente des jeux de stratégie contre l'IA.
| `enigme_pere_fouras.py` | `enigme_pere_fouras()` | Pose une énigme textuelle avec 3 essais.
| `epreuve_finale.py` | `salle_de_tresor()` | Simule la recherche du mot-code final.

### Gestion des Erreurs

Le programme traite les erreurs de saisie (entrées non numériques, choix hors menu) et vérifie l'existence des fichiers de données JSON pour éviter les arrêts inattendus.

---

## 4. Journal de Bord


### Répartition des Tâches

Socning saffo Loic:
Cyril DABERNARD:
Rayane GAREH:
Clement VIENOT:
Axil MEDDAHI:
Youcef:
---

## 5. Tests et Validation

Le projet a fait l'objet d'une campagne de tests rigoureuse pour garantir la stabilité du simulateur. Chaque module a été validé par des batteries de tests unitaires incluses dans les blocs `if __name__ == "__main__":` et par des tests d'intégration manuels pour vérifier la robustesse des interfaces.

### 5.1. Robustesse des Saisies (Module `fonctions_utiles.py`)
La gestion des erreurs de saisie a été testée pour empêcher tout plantage du programme lors de la configuration de l'équipe :
* **Nombre de joueurs** : Le système rejette les valeurs nulles, négatives ou non numériques (ex: "abc") et redemande une saisie valide entre 1 et 3.
* **Noms et Rôles** : Le programme refuse les noms vides et impose une réponse binaire ("oui" ou "non") pour la désignation du leader.
* **Leader par défaut** : Si aucun leader n'est choisi manuellement, le système désigne automatiquement le premier joueur de la liste.
* **Sélection de joueur** : Lors des épreuves, le système vérifie que l'index du joueur choisi existe bien dans l'équipe et refuse les entrées hors limites ou textuelles.

### 5.2. Validation du Menu Principal (Module `main.py`)
Le menu de sélection des épreuves a été testé pour sa tolérance aux erreurs :
* Les entrées invalides (choix inexistants comme "7" ou entrées de texte) déclenchent un message d'alerte et un retour au menu sans interrompre l'exécution.

### 5.3. Tests de Logique des Épreuves (Module `epreuves_hasard.py`)
L'épreuve du Bonneteau sert de référence pour la validation des mini-jeux :
* **Contrôle du choix** : Seules les lettres A, B ou C sont acceptées. Toute autre saisie est bloquée par un message d'erreur.
* **Gestion des tentatives** : Le décompte des essais restants est mis à jour après chaque erreur, et la solution est révélée en cas d'échec final.

### 5.4. Tests Unitaires et Intégrité des Données
Des tests automatisés assurent la fiabilité des calculs et du chargement des fichiers externes :
* **Mathématiques** : Validation des fonctions `factorielle(n)`, `est_premier(n)` et `premier_plus_proche(n)` via des cas de tests prédéfinis.
* **Accès JSON** : Vérification de la présence et de la structure des fichiers `enigmesPF.json` et `indicesSalle.json` avant le lancement des épreuves correspondantes.
* **Historique** : Confirmation de la création automatique du dossier `output/` et de l'écriture correcte des résultats dans `historique.txt`.