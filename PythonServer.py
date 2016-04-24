import json
import os
import GithubUser
import getpass

from github import Github
from flask import Flask, Response
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

# Get your Github token from your Github account
token = os.environ.get('GITHUB_TOKEN')
if (token):
    g = Github(token)
else:
    username = input('Enter your Github username : ')
    password = getpass.getpass('Enter your Github password : ')
    g = Github(username, password)

print('Connecting to your Github account and getting all yours projects... ')
user = GithubUser.GithubUser(g)
ret_projects_JSON = json.dumps(user.get_projects())

# Filtering output
issuesDescendingOrder = sorted(user.projects, key=lambda projects: projects.get(
    'open_issues_count'), reverse=True)
ret_descending_order_JSON = json.dumps(issuesDescendingOrder)

issuesAscendingOrder = sorted(
    user.projects, key=lambda projects: projects.get('open_issues_count'))
ret_ascending_order_JSON = json.dumps(issuesAscendingOrder)

contributorsAscendingOrder = sorted(user.projects, key=lambda projects: len(
    projects.get('contributors')), reverse=True)
ret_contributors_order_JSON = json.dumps(contributorsAscendingOrder)


@app.route('/')
def get_repos_name():
    return "New Project dashboard api"


@app.route('/projects', methods=['GET'])
def getProject():
    response = Response(response=ret_projects_JSON,
                        status=200,
                        mimetype="application/json")

    return response


@app.route('/filter_max_min', methods=['GET'])
def getProject2():
    response2 = Response(response=ret_descending_order_JSON,
                         status=200,
                         mimetype="application/json")

    return response2


@app.route('/filter_min_max', methods=['GET'])
def getProject3():
    response3 = Response(response=ret_ascending_order_JSON,
                         status=200,
                         mimetype="application/json")

    return response3


@app.route('/filter_contributors', methods=['GET'])
def getProject4():
    response4 = Response(response=ret_contributors_order_JSON ,
                         status=200,
                         mimetype="application/json")

    return response4


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
