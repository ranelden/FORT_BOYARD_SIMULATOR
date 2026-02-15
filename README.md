# Fort Boyard
Ce projet est une simulation du jeu télévisé Fort Boyard, réalisée dans le cadre d’un projet scolaire en Python.  
Le joueur constitue une équipe, choisit des épreuves et tente de gagner des clés pour accéder à la salle du trésor.

# 1. Règles du jeu

- Le joueur crée une équipe de **1 à 3 joueurs**.
- Chaque joueur a un **nom**, une **profession** et un **rôle** (leader ou membre).
- Le jeu propose plusieurs types d’épreuves :
  - Épreuves mathématiques
  - Épreuves de hasard
  - Épreuves logiques
  - Énigmes du Père Fouras
- Chaque épreuve réussie fait gagner **une clé**.
- Avec **3 clés**, l’équipe peut tenter d’accéder à la **salle du trésor** (mot-code à deviner à partir d’indices).

---

# 2. Lancer le jeu

### Prérequis

- Python 3 installé sur la machine.
- (Optionnel) Git si vous souhaitez cloner le dépôt.

### Installation

git clone https://github.com/<loicsaffo25-lab>/FORT_BOYARD_SIMULATOR.git
cd FORT_BOYARD_SIMULATON

# En suite faire une exécution du main
  python main.py

Le jeu se lance dans le terminal et vous guide étape par étape.

# 3. Fichiers principaux
main.py
Point d’entrée du programme. Gère le menu principal, la boucle de jeu et l’enchaînement des épreuves.

fonctions_utiles.py
Contient les fonctions générales utilisées dans tout le jeu, par exemple :

introduction() : affiche le message d’accueil.

composer_equipe() : permet de créer l’équipe de 1 à 3 joueurs.

menu_epreuves() : affiche le menu des épreuves.

choisir_joueur(equipe) : permet de sélectionner le joueur qui participe à l’épreuve.

epreuve_finale.py
Contient la salle du trésor et/ou les fonctions liées à l’épreuve finale :

Gestion de l’accès à la salle du trésor.

Lecture des indices et du mot-code.

Gestion des essais du joueur pour trouver le mot-code.

epreuves_mathematiques.py
Implémente les différentes épreuves à base de calculs.

epreuves_hasard.py
Implémente les épreuves basées sur le hasard (tirages aléatoires, etc.).

enigme_pere_fouras.py (si présent)
Gère les énigmes textuelles du Père Fouras.

data/indicesSalle.json (si présent)
Fichier de données contenant les mots-code et les indices utilisés pour la salle du trésor.

# 4. Technologies utilisées
Langage : Python 3

Modules standard :

random (gestion du hasard)

json (lecture des indices depuis un fichier JSON )

# 5. Auteurs

#### Socning saffo Loic:
     j'ai Développé:  les fonctions utilitaires 
                      l’épreuve finale
                      realisé le fichier readme structuré et detaillé 

#### Cyril DABERNARD:




#### Rayane GAREH:



#### Clement VIENOT:




#### Axil MEDDAHI: 


#### Youcef: 

