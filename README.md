# GLOO-2003 API  ![Build Status](https://travis-ci.com/glo2003/team9.svg?token=Epmbu7uyWDkfVaXsgPa9&branch=master) ![Heroku Status](https://heroku-badge.herokuapp.com/?app=github-api-team9)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fluiseduardo1%2FGithub-API.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fluiseduardo1%2FGithub-API?ref=badge_shield)

## Vision

Notre API permet de vous connecter à Github et de collecter de nombreuses informations sur vos projets Github accessibles. 

### Comment contribuer au projet?
Si vous voulez contribuer à notre projet ou bien si vous avez trouvé un bogue dans le code référez-vous au fichier [CONTRIBUTING](CONTRIBUTING.md).

[contributing]: /CONTRIBUTING
## Instructions:

Pour commencer, vous devez vous créer un token Github pour accéder à l'API de Github. Vous pouvez suivre les étapes suivantes pour vous créer un token : [Se créer un Github token](https://help.github.com/articles/creating-an-access-token-for-command-line-use/).

Une fois votre Github token récupéré, vous devez l'ajouter comme environnement de variable sous le nom "GITHUB_TOKEN".

Si vous n'avez pas de Github token, l'application vous demandera votre nom d'utilisateur et mot de passe de votre compte Github.

### Dépendances et installation:

Vous devez utiliser [Python 3](https://www.python.org/download/) pour exécuter l'application, celle-ci utilise les dépendances suivantes:
* Flask
* Flask-CORS
* PyGithub
* PEP8
* Coverage

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

### Données métriques sur le projet
Le projet utilise l'outil "Coverage" qui permet de mesurer la couverture des tests en python. Dans notre cas, nous l'utilisons pour déterminer le pourcentage de tests réussis lors des builds effectués par Travis-ci.

Si vous voulez, vous pouvez le tester localement en exécutant :
```bash
 coverage run votreTest.py
 coverage report
```

### Vérification de style
Notre projet doit respecter les normes de style du [PEP8] (https://www.python.org/dev/peps/pep-0008/) qui est à la norme à respecter en python. Travis-Ci ne permettra pas de déployer le code si celui-ci ne respecte pas le style, si tel est le cas les erreurs de style seront affichés dans Travis-ci. 

Dans notre projet, nous vérifions le style de code grâce à [flake8] (https://pypi.python.org/pypi/flake8) qui inspecte notamment le code selon PEP8.
Si vous voulez, vous pouvez le tester localement en exécutant :
```bash
  flake8 team9/
```

## Comment exécuter le projet?
Pour démarrer le serveur:
```bash
python PythonServer.py
```

Si l'application ne trouve pas votre Github token, celle-ci vous demandera de fournit votre nom d'utilisateur et mot de passe pour se connecter à l'API.

Le serveur roule sur le port 5000.

Vous pouvez tester l'API, avec une interface actualisée, à la page suivante:
http://glo2003.github.io/team9/?server=http://localhost:5000

Pour consulter les réponses aux questions du projet, vous pouvez acceder à notre wiki:
- TP1 : https://github.com/glo2003/team9/wiki/R%C3%A9ponses-questions-TP1
- TP2 : https://github.com/glo2003/team9/wiki/R%C3%A9ponses-questions-TP2
- TP3 : https://github.com/glo2003/team9/wiki/R%C3%A9ponses-questions-TP3
- TP4 : https://github.com/glo2003/team9/wiki/R%C3%A9ponses-questions-TP4


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fluiseduardo1%2FGithub-API.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fluiseduardo1%2FGithub-API?ref=badge_large)