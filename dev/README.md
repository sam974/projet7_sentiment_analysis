Lancer l'Application Streamlit
Pour cette étape, vous aurez besoin de deux terminaux.

Terminal 1 : L'API (le backend)

Assurez-vous que votre API FastAPI est toujours en cours d'exécution. Si ce n'est pas le cas, relancez-la :

Bash

# Se placer dans le dossier api/
cd api
uvicorn main:app --reload


Si tout se passe bien, votre terminal affichera quelque chose comme : Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)


Terminal 2 : L'Interface (le frontend)

Ouvrez un nouveau terminal.

Installez Streamlit s'il n'est pas déjà présent : pip install streamlit

Placez-vous à la racine de votre projet (mon_projet_ia/) et lancez l'application Streamlit :

Bash

streamlit run app.py
Votre navigateur web devrait s'ouvrir automatiquement sur une nouvelle page (généralement http://localhost:8501).