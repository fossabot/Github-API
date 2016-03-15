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
L'intégration continue du projet s'exécute avec Travis-ci, lorsque les tests réussisent celui-ci déploie automatiquement le projet sur Heroku. Afin que Travis-ci puisse déployer automatiquement le projet, il faut ajouter son Heroku api key afin qu'il puisse s'y connecter. Pour plus d'informations à cet effet, aller sur ce [lien](https://blog.travis-ci.com/2013-07-09-introducing-continuous-deployment-to-heroku/).

Le projet est accesible à l'adresse suivante : https://github-api-team9.herokuapp.com/ .

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

