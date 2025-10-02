# Image de base Python légère
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements et le code
COPY requirements.txt .
COPY api.py .
COPY recommandations.csv .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port utilisé par FastAPI
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
