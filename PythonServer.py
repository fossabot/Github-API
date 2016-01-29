import json
import os
import DashboardAPI

from flask import Flask,Response
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

# Get your Github token from your Github account
token = os.environ.get('GITHUB_TOKEN')
user = DashboardAPI.GithubUser(token)
ret_JSON = json.dumps(user.get_projects())


@app.route('/')
def get_repos_name():
    return "Project dashboard api"

@app.route('/projects', methods=['GET'])
def getProject():   
    response = Response(response = ret_JSON,
            status = 200,
            mimetype = "application/json")

    return response

if __name__ == '__main__':
    app.run()
