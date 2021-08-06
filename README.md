### Prérequis
<ol>
    <li>avoir python3.8 installer</li>
    <li>avoir Docker installer pour faire l'image serveur</li>
</ol>

### Lancer en mode dev
<ol>
    <li>`pip install -r requirements.txt` pour intaller les dépendences</li>
    <li>"py essai.py" pour lancer le serveur</li>
</ol>

### Creer une image docker.
<ol>
    <li>`docker build -t entityback .` pour créer l'image du serveur</li>
    <li>`docker run -p 5000:5000 --name entityback entityback` pour démarrer le serveur</li>
</ol>