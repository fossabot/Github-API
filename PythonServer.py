import json
import os
import pprint
import DashboardAPI

from flask import Flask,Response,jsonify

app = Flask(__name__)

# Get your Github token from your Github account
token = os.environ.get('GITHUB_TOKEN')
user = DashboardAPI.GithubUser(token, "GLOO")
project = DashboardAPI.Project(user)

@app.route('/')
def get_repos_name():
    return "Project dashboard api"

#@app.route('/Project', methods=['GET'])
@app.route('/projects')
def getProject():   
    ret_JSON = json.dumps(project.create_JSON()) 
    response = Response(response = ret_JSON,
            status = 200,
            mimetype = "application/json")

    return response

if __name__ == '__main__':
    app.run()
