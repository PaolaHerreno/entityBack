### Prérequis
<ol>
    <li>avoir python3.8 installer</li>
    <li>avoir Docker installer pour faire l'image serveur</li>
</ol>

### Lancer en mode dev
<ol>
    <li><pre>pip install -r requirements.txt</pre> pour intaller les dépendences</li>
    <li><pre>py essai.py</pre> pour lancer le serveur</li>
</ol>

### Creer une image docker.
<ol>
    <li><pre>docker build -t entityback .</pre> pour créer l'image du serveur</li>
    <li><pre>docker run -p 5000:5000 --name entityback entityback</pre> pour démarrer le serveur</li>
</ol>