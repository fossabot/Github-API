# GLOO-2003 API

## Vision

Notre API permet de vous connecter à de nombreux API (Github, Travis) et collecte de nombreuses informations sur vos projets Github accessibles. 

### Comment contribuer au projet?
Si vous voulez contribuer à notre projet ou bien si vous avez trouvé un bug dans le code référez-vous au fichier [CONTRIBUTING][contributing].

[contributing]: /CONTRIBUTING
## Instructions:

Pour commencer, vous devez vous créer un token Github pour accéder à l'API de Github. Vous pouvez suivre les étapes suivantes pour vous créer un token : [Se créer un Github token](https://help.github.com/articles/creating-an-access-token-for-command-line-use/).

Une fois votre Github token récupéré, vous devez l'ajouter comme environnement de variable sous le nom "GITHUB_TOKEN".

### Installation:

Vous devez utiliser [Python 3](https://www.python.org/download/) pour exécuter l'application.<br/> 
[pip](http://pip.readthedocs.org/en/latest/installing.html) est aussi recommandé pour installer les dépendances.  

Pour créer un nouveau environnement virtuel Python, tappez la commande suivante :
```bash
virtualenv newenv
```

Une fois que l'environnement virtuel est installé vous pouvez ajouter les dépendances en exécutant la commande suivante:
```bash
pip install -r requirements.txt
```

### Comment l'utiliser?
Pour démarrer le serveur:
```bash
python PythonServer.py
```

Pour le moment, si vous voulez accéder à notre dashboard qui est connecté à notre API, aller sur la page suivante:
http://glo2003.xyz/?server=http://localhost:5000 .


