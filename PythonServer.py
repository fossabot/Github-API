import json
import os
import GithubUser

from github import Github
from flask import Flask, Response
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

# Get your Github token from your Github account
token = os.environ.get('GITHUB_TOKEN')
g = Github(token)
user = GithubUser.GithubUser(g)
ret_JSON = json.dumps(user.get_projects())

################################################
# Filtering outuput                            #
################################################

maxMin = sorted(user.projects, key = lambda projects: projects.get('open_issues_count'), reverse=True)
ret_JSON2 = json.dumps(maxMin)

minMax = sorted(user.projects, key = lambda projects: projects.get('open_issues_count'))
ret_JSON3 = json.dumps(minMax)

contributors = sorted(user.projects, key = lambda projects: len(projects.get('contributors')), reverse=True)
ret_JSON4 = json.dumps(contributors)

################################################


@app.route('/')
def get_repos_name():
    return "New Project dashboard api"


@app.route('/projects', methods=['GET'])
def getProject():
    response = Response(response=ret_JSON,
                        status=200,
                        mimetype="application/json")

    return response


@app.route('/filter_max_min', methods=['GET'])
def getProject2():
    response2 = Response(response=ret_JSON2,
                        status=200,
                        mimetype="application/json")

    return response2

@app.route('/filter_min_max', methods=['GET'])
def getProject3():
    response3 = Response(response=ret_JSON3,
                        status=200,
                        mimetype="application/json")

    return response3

@app.route('/filter_contributors', methods=['GET'])
def getProject4():
    response4 = Response(response=ret_JSON4,
                        status=200,
                        mimetype="application/json")

    return response4


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
