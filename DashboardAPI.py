import json
from github import Github

class GithubUser:
    ''' 
        Class that access a Github account
    '''

    def __init__(self, token, repo):        
        g = Github(token)
        self.user = g.get_user()
        self.repo = self.user.get_repo(repo)

class Project:
    '''
        Class that returns the main information from a Github project available from the 
        GITHUB_TOKEN we have generated
    '''

    def __init__(self, github_user):
        self.github_user = github_user
   
    def create_JSON(self):
        return [{"id": self.get_id(),
                "name": self.get_name(),
                "html_url" : self.get_html_url(),
                "language" : self.get_main_language(),
                "languages": self.get_languages(),
                "contributors": self.get_contributors(),
                "branches" : self.get_branches(),
                "badges" : self.get_badges(),
                "open_issues_count" : self.get_open_issues_count(),
                "lastCommit": "",
                "ciStatus": ""
                }]

    def get_id(self):
        return self.github_user.repo.id

    def get_name(self):
        return self.github_user.repo.name

    def get_html_url(self):
        return self.github_user.repo.html_url
    
    def get_contributors(self):
        contributors = []
        for contributor in self.github_user.repo.get_contributors():
            dic = {"login":contributor.login,
                    "id":contributor.id,
                    "avatar_url":contributor.avatar_url,
                    "html_url":contributor.html_url,
                    "type":contributor.type,
                    "contributions":contributor.contributions}
            contributors.append(dic)

        return contributors 

    def get_main_language(self):
        return self.github_user.repo.language

    def get_languages(self):
        languages = []
        return ""

    def get_badges(self):
        ''' In order to get the badges, we have to acces the readme file content, the API gives us the content encoded in base64, we must then decode it and after parse the content to find the badges (that's a way of doing it'''
        return ""

    def get_branches(self):
        #TODO
        branches = []
        for branch in self.github_user.repo.get_branches():
            dic_branch = {"name" : branch.name,
                        "commit": ""}
        
        branches.append(dic_branch)

        return branches  

    def get_open_issues_count(self):
        return self.github_user.repo.open_issues_count



    
   
