# Base image Python
FROM python:3.12-slim

# Informations sur le mainteneur
LABEL maintainer="TonNom <tonemail@example.com>"

# Créer le répertoire de l'application
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
COPY add_users.py .
COPY users.csv .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier les autres fichiers (si besoin)
COPY . .

# Indiquer que le conteneur utilise un fichier .env
ENV PYTHONUNBUFFERED=1

# Commande par défaut
CMD ["python", "add_users.py"]
