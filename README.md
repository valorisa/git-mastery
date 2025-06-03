# Formation Git Mastery : Objectif Maîtrise Complète

Ce projet est un guide d'entraînement approfondi pour maîtriser Git, de ses bases à ses usages avancés. Il vous accompagne pas à pas, en expliquant chaque commande, ses usages, ses pièges, et en fournissant des conseils pratiques pour progresser efficacement.

> **Environnement recommandé** : Ce guide a été conçu sur macOS Sequoia (Intel) avec un dossier de travail type `/Users/<logname>/Projets`, mais toutes les commandes Git sont universelles et fonctionnent sur Linux et Windows (via Git Bash ou WSL). Remarque : `<logname>`est une commande Linux/macOS.

---

## 🚀 1. Initialisation et Configuration Initiale

Avant de commencer, assurez-vous que Git est installé :

```bash
git --version
```
Si ce n'est pas le cas, installez-le via [git-scm.com](https://git-scm.com/downloads).

### Configuration de votre identité Git

Il est indispensable de configurer votre nom et votre adresse email, car ils seront associés à chaque commit :

```bash
git config --global user.name "Your_Name"
git config --global user.email "your.email@example.com"
```
> **Astuce** : Utilisez `--global` pour appliquer la configuration à tous vos dépôts, ou sans `--global` pour ne la définir que dans le projet courant.

### Création de votre projet d'entraînement

Créez un dossier dédié et initialisez un dépôt Git :

```bash
mkdir git-mastery-training
cd git-mastery-training
git init
```
Votre "bac à sable" Git est prêt !

---

## 🛠️ 2. Manipulations de Base : Fichiers et Commits

### Création et suivi de fichiers

1. Créez quelques fichiers (par exemple, `README.md`, `script.py`, `notes.txt`) :
    ```bash
    touch README.md script.py notes.txt
    ```
2. Ajoutez-les à la zone de préparation (index) :
    ```bash
    git add README.md script.py notes.txt
    # Ou pour tous les fichiers : git add .
    ```
3. Effectuez votre premier commit :
    ```bash
    git commit -m "Premier commit : ajout des fichiers initiaux"
    ```

> **Conseil** : Commencez toujours par des petits commits atomiques, cela facilitera l’historique et la relecture.

### Modification et consultation

1. Modifiez un fichier (par exemple, `script.py`) avec votre éditeur préféré.
2. Vérifiez l’état du dépôt :
    ```bash
    git status
    ```
3. Visualisez les modifications apportées :
    ```bash
    git diff
    ```
4. Ajoutez et commitez les changements :
    ```bash
    git add script.py
    git commit -m "Modifie script.py : ajout d'une fonction"
    ```

---

## 🌿 3. Gestion des Branches

Les branches permettent de travailler sur des fonctionnalités ou corrections sans impacter la branche principale.

### Création et navigation

1. Créez une nouvelle branche :
    ```bash
    git branch feature-nouvelle-fonctionnalite
    ```
2. Basculez dessus :
    ```bash
    git checkout feature-nouvelle-fonctionnalite
    # Ou, plus moderne :
    git switch feature-nouvelle-fonctionnalite
    ```
    > **Astuce** : Créez et basculez en une seule commande :
    > ```bash
    > git checkout -b feature-nouvelle-fonctionnalite
    > # ou
    > git switch -c feature-nouvelle-fonctionnalite
    > ```

### Fusion de branches (merge)

1. Faites des commits sur votre branche de fonctionnalité.
2. Revenez sur la branche principale :
    ```bash
    git checkout main
    # ou git switch main
    ```
3. Fusionnez la branche :
    ```bash
    git merge feature-nouvelle-fonctionnalite
    ```
    > **Conseil** : Résolvez les conflits de fusion si besoin, puis validez la fusion.

### Réécriture de l’historique (rebase)

Le rebase permet de "rejouer" vos commits sur une base plus récente, gardant un historique linéaire.

- **Rebaser votre branche de fonctionnalité sur la branche principale (le plus courant)** :
    ```bash
    git checkout feature-nouvelle-fonctionnalite
    git fetch origin # Pour récupérer les dernières mises à jour distantes
    git rebase main  # ou git rebase origin/main si vous suivez la version distante
    ```
    > **Attention** : Ne faites pas de rebase sur des branches déjà partagées avec d'autres, car cela réécrit l’historique !

- **Rebaser la branche principale sur votre branche de fonctionnalité** (rare, mais illustratif) :
    ```bash
    git checkout main
    git rebase feature-nouvelle-fonctionnalite
    ```

#### 💡 Différence merge vs rebase

- **merge** : conserve l’historique de branchement (commits parallèles, puis commit de fusion).
- **rebase** : réécrit l’historique pour donner l’impression d’un développement linéaire.

---

## ☁️ 4. Travailler avec des Dépôts Distants

### Connecter un dépôt local à un dépôt distant

Créez un dépôt distant (ex : GitHub) et copiez son URL :
```bash
git remote add origin https://github.com/votre-utilisateur/git-mastery-training.git
```
> **Conseil** : Utilisez `git remote -v` pour vérifier la configuration.

### Envoyer vos modifications

- Premier push (avec suivi de branche) :
    ```bash
    git push -u origin main
    ```
- Pushs suivants :
    ```bash
    git push
    ```

### Récupérer les modifications distantes

```bash
git pull origin main
# ou simplement
git pull
```
> **Explication** : `git pull` = `git fetch` + `git merge` (ou `git rebase` selon la config).

### Cloner un dépôt existant

```bash
git clone https://github.com/votre-utilisateur/git-mastery-training.git
```

---

## ✨ 5. Techniques Avancées et Utilitaires

### Mise de côté temporaire (stash)

Pour sauvegarder des modifications non commitées :
```bash
git stash push -m "Travail en cours sur la fonctionnalité Y"
git stash list
git stash pop  # Applique et retire le dernier stash
# git stash apply # Applique sans retirer
# git stash drop # Supprime un stash spécifique
```
> **Astuce** : Utilisez le stash pour changer rapidement de branche sans perdre votre travail en cours.

### Suppression de fichiers

- **Supprimer un fichier suivi par Git et du système de fichiers** :
    ```bash
    git rm notes.txt
    git commit -m "Supprime notes.txt"
    ```
- **Supprimer des fichiers non suivis (dangereux)** :
    ```bash
    git clean -n   # Simulation
    git clean -f   # Suppression effective
    git clean -fd  # Supprime aussi les dossiers non suivis
    ```

### Ignorer des fichiers avec `.gitignore`

1. Créez un fichier `.gitignore` à la racine.
2. Ajoutez-y les motifs à ignorer :
    ```
    # Fichiers Python compilés
    __pycache__/
    *.pyc

    # Dépendances Node.js
    node_modules/

    # Fichiers de log
    *.log
    ```
3. Ajoutez et commitez le `.gitignore` :
    ```bash
    git add .gitignore
    git commit -m "Ajoute .gitignore"
    git status
    ```

> **Conseil** : Un bon `.gitignore` protège votre dépôt des fichiers inutiles ou sensibles.

---

## 📜 6. Explorer l'Historique et Annuler des Modifications

### Visualisation de l’historique

```bash
git log
git log --oneline
git log --graph --oneline --all --decorate
```
> **Astuce** : Utilisez `q` pour quitter la vue log.

### Revenir à un état antérieur

- **Annuler le dernier commit et supprimer les modifications du répertoire de travail** :
    ```bash
    git reset --hard HEAD~1
    ```
- **Annuler le dernier commit mais garder les modifications en staging** :
    ```bash
    git reset --soft HEAD~1
    ```
- **Annuler le dernier commit mais garder les modifications dans le répertoire de travail** :
    ```bash
    git reset --mixed HEAD~1
    ```

> **Attention** : `--hard` efface définitivement les modifications non sauvegardées !

### Annuler des modifications non commitées

- **Restaurer un fichier à sa version du dernier commit** :
    ```bash
    git restore nom_du_fichier.txt
    # Ancienne méthode :
    git checkout -- nom_du_fichier.txt
    ```
- **Retirer un fichier de la zone de préparation (index)** :
    ```bash
    git restore --staged nom_du_fichier.txt
    # Ancienne méthode :
    git reset HEAD nom_du_fichier.txt
    ```

### Annuler un commit publié (méthode sûre)

Pour annuler un commit déjà poussé :
```bash
git revert 
```
> **Explication** : `git revert` crée un nouveau commit qui annule les changements, sans réécrire l’historique partagé.

### Récupérer des commits perdus

Utilisez le reflog pour retrouver des commits supprimés par erreur :
```bash
git reflog
# Puis, pour revenir à un état précédent :
git reset --hard 
```

---

## 🔬 7. Comparaison Détaillée : Local vs Distant

### Mettre à jour les références distantes

```bash
git fetch origin
```

### Comparer le contenu des fichiers

```bash
git diff origin/main
```

### Lister les fichiers différents

```bash
git diff --name-status origin/main
```

### Comparer un fichier précis

```bash
git diff origin/main -- chemin/vers/fichier.txt
```

### Voir les commits présents sur le distant mais pas en local

```bash
git log main..origin/main --oneline
```

### Voir les commits locaux non poussés

```bash
git log origin/main..main --oneline
```

### Vérifier l’avance/retard de la branche

```bash
git status
```

#### Tableau récapitulatif

| Action                                 | Commande                                        |
| :------------------------------------- | :---------------------------------------------- |
| Mettre à jour les infos du distant     | `git fetch origin`                              |
| Diff de contenu (local vs distant)     | `git diff origin/main`                          |
| Liste des fichiers modifiés            | `git diff --name-status origin/main`            |
| Diff d’un fichier précis               | `git diff origin/main -- chemin/vers/fichier`   |
| Commits distants non présents en local | `git log main..origin/main --oneline`           |
| Commits locaux non poussés             | `git log origin/main..main --oneline`           |
| Vérifier l’avance/retard               | `git status`                                    |

---

## ⚙️ 8. Commandes Diverses et Personnalisations

### Configurer des alias utiles

```bash
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.st "status"
git config --global alias.co "checkout"
git config --global alias.br "branch"
```
> **Astuce** : Ces alias accélèrent votre workflow quotidien !

### Lister branches, tags, remotes

```bash
git branch       # Branches locales
git branch -r    # Branches distantes
git branch -a    # Toutes les branches
git tag          # Tous les tags
git remote -v    # Voir les dépôts distants
```

### Utiliser l’aide intégrée

```bash
git help 
# Exemples :
git help log
git help commit
git help rebase
```

---

## 📋 9. Liste Récapitulative des Commandes à Pratiquer

| Commande          | Description                                               |
| :---------------- | :------------------------------------------------------- |
| `git init`        | Initialiser un dépôt Git local                           |
| `git clone`       | Cloner un dépôt distant existant                         |
| `git config`      | Configurer les options Git (utilisateur, alias, etc.)    |
| `git status`      | Afficher l'état des fichiers du répertoire de travail    |
| `git add`         | Ajouter des modifications à l'index (staging)            |
| `git commit`      | Enregistrer les modifications dans l'historique          |
| `git log`         | Afficher l'historique des commits                        |
| `git diff`        | Afficher les différences entre commits, branches, fichiers|
| `git branch`      | Lister, créer ou supprimer des branches                  |
| `git checkout`    | Changer de branche ou restaurer des fichiers             |
| `git switch`      | (Moderne) Changer de branche                             |
| `git restore`     | (Moderne) Restaurer des fichiers / annuler des indexations|
| `git merge`       | Fusionner des branches                                   |
| `git rebase`      | Réappliquer des commits sur une autre base               |
| `git remote`      | Gérer les dépôts distants                                |
| `git fetch`       | Télécharger les objets et références d'un dépôt distant  |
| `git pull`        | `fetch` suivi d'un `merge` (ou `rebase`)                 |
| `git push`        | Envoyer les commits locaux vers un dépôt distant         |
| `git stash`       | Mettre de côté temporairement des modifications locales  |
| `git rm`          | Supprimer des fichiers de l'index et du répertoire       |
| `git clean`       | Supprimer les fichiers non suivis du répertoire          |
| `git tag`         | Marquer des commits avec des étiquettes                  |
| `git reset`       | Annuler des commits ou des indexations (attention)       |
| `git revert`      | Créer un commit qui annule un commit précédent           |
| `git show`        | Afficher divers objets Git (commits, tags, etc.)         |
| `git blame`       | Afficher qui a modifié chaque ligne d'un fichier         |
| `git cherry-pick` | Appliquer un commit spécifique sur la branche courante   |
| `git reflog`      | Afficher le journal des références (récupération)        |

---

## 💡 10. Conseils pour Approfondir

- **Tenez un journal** : Notez vos commandes, essais, erreurs et découvertes dans un fichier `JOURNAL.md`.
- **Expérimentez avec les erreurs** : Provoquez des conflits, annulez des commits, récupérez des états antérieurs pour comprendre comment Git fonctionne en profondeur.
- **Explorez la récupération** : Utilisez `git reflog` pour retrouver des commits supprimés ou perdus.
- **Personnalisez Git** : Testez différentes options de `git config` (éditeur par défaut, couleurs, comportement de pull, etc.).
- **Essayez les hooks Git** : Automatisez des actions (tests, formatage) avant ou après certains événements Git (voir `.git/hooks`).

---

## 📚 11. Ressources Complémentaires

- [Documentation officielle de Git](https://git-scm.com/doc)
- [Pro Git Book (français)](https://git-scm.com/book/fr/v2)
- [Learn Git Branching (français)](https://learngitbranching.js.org/?locale=fr_FR)
- [Atlassian Git Tutorials](https://www.atlassian.com/fr/git/tutorials)
- [GitHub Skills](https://skills.github.com/)
- [Hostinger - Commandes Git](https://www.hostinger.fr/tutoriels/commandes-git)
- [DataCamp - Guide Pratique Git](https://www.datacamp.com/fr/blog/git-commands)
- [Feuille de triche GitHub (PDF)](https://training.github.com/downloads/fr/github-git-cheat-sheet.pdf)

---

**Ce projet est votre laboratoire. Expérimentez sans crainte, testez toutes les commandes, et amusez-vous à explorer les possibilités de Git. C’est en pratiquant que vous deviendrez un expert !**

---
