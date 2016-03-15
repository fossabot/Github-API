import json
import os
import GithubUser

from flask import Flask, Response
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

# Get your Github token from your Github account
token = os.environ.get('GITHUB_TOKEN')
user = GithubUser.GithubUser(token)
ret_JSON = json.dumps(user.get_projects())


@app.route('/')
def get_repos_name():
    return "New Project dashboard api"


@app.route('/projects', methods=['GET'])
def getProject():
    response = Response(response=ret_JSON,
                        status=200,
                        mimetype="application/json")

    return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
