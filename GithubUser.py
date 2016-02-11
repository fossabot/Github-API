from github import Github

class GithubUser:
    ''' 
        Class that returns informations about your Github projects 
    '''

    def __init__(self, token):        
        g = Github(token)
        self.projects = []
        self.repos = g.get_user().get_repos()

    def get_projects(self):
        for repo in self.repos:
            project = {"id": repo.id,
                        "name": repo.name,
                        "html_url" : repo.html_url,
                        "language" : repo.language,
                        "languages": repo.get_languages(),
                        "contributors": self.get_contributors(repo),
                        "branches" : self.get_branches(repo),
                        "open_issues_count" : repo.open_issues_count
                        }
            self.projects.append(project)

        return self.projects
       
    def get_contributors(self, repo):
        contributors = []
        for contributor in repo.get_contributors():
            dic = {"login":contributor.login,
                    "id":contributor.id,
                    "avatar_url":contributor.avatar_url,
                    "html_url":contributor.html_url,
                    "type":contributor.type,
                    "contributions":contributor.contributions}
            contributors.append(dic)

        return contributors 

    def get_branches(self, repo):
        branches = []
        for branch in repo.get_branches():
            dic_branch = {"name" : branch.name,
                    "commit": {"sha":branch.commit.sha,
                               "url":branch.commit.url}}
            branches.append(dic_branch)

        return branches  


