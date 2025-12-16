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
5. Run tests:
    ```bash
        python -m unittest discover -s tests
   ```
   
6. Scan it with SonarQube and SonarLint 
7. Fix the issues
8. Scan again to verify improvements