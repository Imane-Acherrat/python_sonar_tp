# Python SonarQube TP Project

This project is used for practicing SonarQube analysis.  
It intentionally contains some bugs, security issues, and code smells.

## How to use

1. Pull this project from GitHub:
   ```bash
        git clone <your-github-link>
        cd python_sonar_tp
   ```
2. (Optional) Create a virtual environment:
    ```bash
        python -m venv venv
        source venv/bin/activate   # Linux / macOS
        venv\Scripts\activate      # Windows
   ```
3. Install requirements:
    ```bash
        pip install -r requirements.txt
    ```
4. Run the project:
    ```bash
        python main.py
    ```
5. Installer l’outil de couverture
    ```bash
       pip install coverage
    ```
6. Run tests avec coverage:
    ```bash
    coverage run -m unittest discover -s tests
   ```
- Lance tous les tests du dossier tests

- Mesure quelles lignes de code sont exécutées

- Remplace python -m unittest par une version avec analyse de couverture
7. Afficher le rapport de couverture dans le terminal
   ```bash
      coverage report -m
   ```
8. Générer le rapport de couverture pour SonarQube
     ```bash
      coverage xml
   ```
     - Génère le fichier coverage.xml
     - Format compatible avec SonarQube et GitLab CI
     - Obligatoire pour que SonarQube prenne en compte la couverture
9. Scan it with SonarQube and SonarLint 
10. Fix the issues
11. Scan again to verify improvements
