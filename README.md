# GLOO-2003 API

Our API permits you to connect to various API (Github, Travis, etc) and collect various informations for all of your Github projects.

## Instructions:

First, you will need to create a Github token to connect to the various API. You can follow theses steps to create your own token : [Create a Github token](https://help.github.com/articles/creating-an-access-token-for-command-line-use/).

After that, you will need to set the token as an variable environment with the name "GITHUB_TOKEN".

### Installation:

You will need [Python 3](https://www.python.org/download/) to run this program. <br/> 
[pip](http://pip.readthedocs.org/en/latest/installing.html) is recommended for installing dependencies.

To create a new virtualenv:
```bash
virtualenv newenv
```

Once activated, you can install the dependencies:
```bash
pip install -r requirements.txt
```

### How to run:
For the moment, if you want to access our API dashboard, you can connect to this address in your favorite browser:
http://glo2003.xyz/?server=http://localhost:5000 .
