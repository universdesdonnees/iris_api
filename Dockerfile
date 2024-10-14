# Utilisation d'une image Python plus récente et légère
FROM python:3.12

# Mettre à jour pip
RUN pip install --upgrade pip

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt pour installer les dépendances
COPY requirements.txt .

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Copier le reste des fichiers de l'application
COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

