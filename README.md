# Git mastery Training

## Projet d'entraînement Git : Objectif "Maîtrise complète des commandes"

Pour s'entraîner efficacement sur la quasi-totalité des commandes Git, il est
pertinent de structurer un projet pédagogique qui nous fera explorer les
commandes essentielles, avancées, et même certaines moins courantes. Voici un plan de projet complet, adapté à un environnement macOS Sequoia (Intel), que l'on pourra réaliser dans le dossier `/Users/<logname>/Projets`.

---

### **1. Initialisation et configuration**

- Installer Git si ce n’est pas déjà fait.
- Configurer son identité :

  ```bash
  git config --global user.name "Your name"
  git config --global user.email "Your.email@example.com"
  ```

- Créer un nouveau dossier de projet et initialiser un dépôt :

  ```bash
  mkdir git-mastery
  cd git-mastery
  git init
  ```

---

### **2. Manipulation de fichiers et commits**

- Créer plusieurs fichiers (ex : `README.md`, `script.py`, `notes.txt`).
- Ajoutez-les à l’index, puis faites un commit :

  ```bash
  git add README.md script.py notes.txt
  git commit -m "Premier commit avec plusieurs fichiers"
  ```

- Modifier un fichier, vérifier l’état :

  ```bash
  git status
  git diff
  ```

- Ajouter et committer à nouveau :

  ```bash
  git add script.py
  git commit -m "Modification du script"
  ```

---

### **3. Gestion des branches**

- Créer et naviguer entre plusieurs branches :

  ```bash
  git branch feature-x
  git checkout feature-x
  # ou, plus moderne :
  git switch feature-x
  ```

- Fusionner une branche :

  ```bash
  git checkout main
  git merge feature-x
  ```

- Expérimenter le rebase :

  ```bash
  git rebase feature-x
  ```

- Alternativement :

  ```bash
  git checkout feature-x
  git rebase main
  ```

---

### **4. Gestion des dépôts distants**

- Simuler un dépôt distant avec un second dossier ou utiliser GitHub/GitLab :

  ```bash
  git remote add origin 
  git push -u origin main
  git pull origin main
  ```

---

### **5. Manipulation avancée**

- Stasher des modifications :

  ```bash
  git stash
  git stash list
  git stash pop
  ```

- Supprimer des fichiers suivis et non suivis :

  ```bash
  git rm notes.txt
  git clean -n
  git clean -f
  ```

- Ignorer des fichiers/dossiers (ex : `__pycache__`) :
  - Ajouter à `.gitignore`, puis vérifier avec `git status`[4].

---

### **6. Exploration de l’historique et annulation**

- Explorer l’historique :

  ```bash
  git log
  git log --oneline --graph --all
  ```

- Revenir à un état antérieur :

  ```bash
  git reset --hard HEAD~1
  ```

- Annuler des modifications :

  ```bash
  git checkout -- script.py
  # ou, plus moderne :
  git restore script.py
  ```

---

### **7. Commandes diverses et personnalisations**

- Configurer des alias :

  ```bash
  git config --global alias.lg "log --oneline --graph"
  ```

- Lister toutes les branches, tags, remotes :

  ```bash
  git branch -a
  git tag
  git remote -v
  ```

- Utiliser l’aide intégrée :

  ```bash
  git help 
  ```

---

## **Liste non exhaustive des commandes à pratiquer**

| Commande              | Description                                      |
|-----------------------|--------------------------------------------------|
| git init              | Initialiser un dépôt                             |
| git clone             | Cloner un dépôt distant                          |
| git status            | État du dépôt                                    |
| git add               | Ajouter à l’index                                |
| git commit            | Créer un commit                                  |
| git log               | Historique des commits                           |
| git diff              | Voir les différences                             |
| git branch            | Gérer les branches                               |
| git checkout/switch   | Changer de branche/restaurer un fichier          |
| git merge             | Fusionner des branches                           |
| git rebase            | Rejouer des commits                              |
| git remote            | Gérer les dépôts distants                        |
| git pull              | Récupérer et fusionner du distant                |
| git push              | Envoyer au distant                               |
| git stash             | Mettre de côté des modifications                 |
| git rm                | Supprimer des fichiers suivis                    |
| git clean             | Supprimer des fichiers non suivis                |
| git tag               | Gérer les tags                                   |
| git reset             | Réinitialiser HEAD ou l’index                    |
| git revert            | Annuler un commit en créant un commit inverse    |
| git config            | Configurer Git                                   |
| git show              | Afficher des objets Git (commit, tag, etc.)      |
| git blame             | Voir qui a modifié chaque ligne                  |
| git cherry-pick       | Appliquer un commit précis sur une autre branche |

[1](https://www.hostinger.com/fr/tutoriels/commandes-git)
[2](https://www.datacamp.com/fr/blog/git-commands)
[5](https://www.datacamp.com/fr/tutorial/github-and-git-tutorial-for-beginners)

---

## **Conseils pour aller plus loin**

- Documenter chaque étape dans un fichier `JOURNAL.md`.
- Utiliser des erreurs volontaires (commits à annuler, conflits à résoudre).
- Tester les commandes de récupération (`git reflog`, `git fsck`, etc.).
- Explorer la personnalisation via `git config` (alias, couleurs, éditeur par défaut...).

---

## **Ressources complémentaires**

- [Hostinger - Commandes Git][https://www.hostinger.com/fr/tutoriels/commandes-git](1)
- [DataCamp - Guide pratique Git][https://www.datacamp.com/fr/blog/git-commands](2)
- [Exercices guidés Git][https://supports.uptime-formation.fr/02-git-et-gitlab/git_1_exo/](4)

---

On peut ainsi se créer un "bac à sable" Git où l'on s'autorise toutes les
manipulations, y compris celles qui "cassent" l'historique, afin de comprendre
l'effet de chaque commande. En suivant ce plan, on pratiquera la quasi-totalité
des commandes Git utiles dans la vie réelle et on pourra compléter avec la
documentation officielle ou l'aide intégrée pour les commandes plus rares.

[1] https://www.hostinger.com/fr/tutoriels/commandes-git
[2] https://www.datacamp.com/fr/blog/git-commands
[3] https://talks.freelancerepublik.com/git-commandes-indispensables-developpeurs/
[4] https://supports.uptime-formation.fr/02-git-et-gitlab/git_1_exo/
[5] https://www.datacamp.com/fr/tutorial/github-and-git-tutorial-for-beginners
[6] https://blog.stephane-robert.info/docs/developper/version/git/
[7] https://training.github.com/downloads/fr/github-git-cheat-sheet.pdf
[8] https://www.macg.co/logiciels/2018/04/decouvrez-et-apprenez-git-avec-ce-nouveau-tutoriel-video-102093?page=1
[9] https://www.atlassian.com/fr/git/tutorials/install-git
[10] https://gist.github.com/dgageot/656299
