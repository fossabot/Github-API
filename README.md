# GLOO-2003 API  ![Build Status](https://travis-ci.com/glo2003/team9.svg?token=Epmbu7uyWDkfVaXsgPa9&branch=master)

## Vision

Notre API permet de vous connecter à de nombreux API (Github, Travis) et collecte de nombreuses informations sur vos projets Github accessibles. 

### Comment contribuer au projet?
Si vous voulez contribuer à notre projet ou bien si vous avez trouvé un bogue dans le code référez-vous au fichier [CONTRIBUTING](CONTRIBUTING.md).

[contributing]: /CONTRIBUTING
## Instructions:

Pour commencer, vous devez vous créer un token Github pour accéder à l'API de Github. Vous pouvez suivre les étapes suivantes pour vous créer un token : [Se créer un Github token](https://help.github.com/articles/creating-an-access-token-for-command-line-use/).

Une fois votre Github token récupéré, vous devez l'ajouter comme environnement de variable sous le nom "GITHUB_TOKEN".

### Dépendances et installation:

Vous devez utiliser [Python 3](https://www.python.org/download/) pour exécuter l'application, celle-ci utilise les dépendances suivantes:
* Flask
* Flask-CORS
* PyGithub

[pip](http://pip.readthedocs.org/en/latest/installing.html) est aussi recommandé pour installer les dépendances.  

Nous vous suggérons de créer un nouveau environnement virtuel Python avec virtualenv, voici la commande pour créer un nouveau environnement en spécifiant le path pour votre Python 3:
```bash
virtualenv -p /path/to/your/Python3 newenv 
```

Une fois que l'environnement virtuel est installé vous pouvez ajouter les dépendances en exécutant la commande suivante:
```bash
pip install -r requirements.txt
```

### Intégration continue
L'intégration continue du projet s'exécute avec Travis-ci, lorsque les tests réussisent celui déploie automatiquement le projet sur Heroku.
Le projet est accesible à l'adresse suivante : https://github-api-team9.herokuapp.com/ .
Il est important toutefois de bien sauvegarder votre Github token pour qu'Heroku puisse démarrer le projet. Voir la section suivante pour voir comment enregistrer vos variables de configuration pour Heroku.

### Si vous voulez déployer directement sur Heroku
Voici les étapes à suivre si vous voulez déployer le projet directement sur Heroku sans passer par l'entremise de Travis-ci:

    1. Récupérer le code du projet et accéder au dossier
    2. Tapper ```bash  
                 heroku 
              ```
    3. Puis ```bash
               git push heroku master
            ```
    4. Afin qu'Heroku puisse reconnaitre votre Github token, il faut l'ajouter aux variables de configuration d'Heroku, voici la commande à exécuter:
        heroku config:set GITHUB_TOKEN=VOTRE_TOKEN
    5. Finalement, vous n'avez qu'à accéder à l'URL de votre application Heroku qui vous sera retourné.

### Comment l'utiliser?
Pour démarrer le serveur:
```bash
python PythonServer.py
```
Le serveur roule sur le port 5000.

Vous pouvez tester l'API à la page suivante:
http://glo2003.xyz/?server=http://localhost:5000 .

Pour consulter les réponses aux questions du projet, vous pouvez acceder à notre wiki:
- TP1 : https://github.com/glo2003/team9/wiki/R%C3%A9ponses-questions-TP1
- TP2 : https://github.com/glo2003/team9/wiki/R%C3%A9ponses-questions-TP2

