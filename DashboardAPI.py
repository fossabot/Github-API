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
        self.account_id = ""
        self.name = ""
        self.html_url = ""
        self.language = ""
        self.branches = ""
        self.badges = ""
        self.openIssuesCount = ""
        self.github_user = github_user
   
    def create_JSON(self):
        return [{"id": self.get_id(),
                "name": self.get_name(),
                "html_url" : self.get_html_url(),
                "language" : self.get_main_language(),
                "languages": self.get_languages(),
                "branches" : self.get_branches(),
                "badges" : self.get_badges(),
                "open_issues_count" : self.get_open_issues_count()
                }]

    def get_id(self):
        return self.github_user.repo.id

    def get_name(self):
        return self.github_user.repo.name

    def get_html_url(self):
        return self.github_user.repo.html_url
    
    def get_contributors(self):
        contributors = []
        return ""

    def get_main_language(self):
        return self.github_user.repo.language

    def get_languages(self):
        languages = []
        return ""

    def get_badges(self):
        return ""

    def get_branches(self):
        branches = []
        for branch in self.github_user.repo.get_branches():
            branches.append(branch.name)
        return branches  

    def get_open_issues_count(self):
        return self.github_user.repo.open_issues_count


class Contributor:

    def __init__(self, login, contributor_id, avatar_url, html_url, contributor_type, nb_contributions):
        self.login = login
        self.contributor_id = contributor_id
        self.avatar_url = avatar_url
        self.html_url = hmtl_url
        self.contributor_type = contributor_type
        self.nb_contributions = nb_contributions




    
   
