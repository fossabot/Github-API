from github import Github
import json

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
                        "open_issues_count" : repo.open_issues_count,
                        "open_issues": self.get_all_issues(repo)
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

    def get_all_issues(self, repo):
        issues = []
        for issue in repo.get_issues():         
        
#            test = json.dumps(list(issue.user.__dict__))
            #print(test)
            dic_issue = {"id" : issue.id,
                        "url" : issue.url,
                        "repository_url" : issue.repository.url,
                        "labels_url" : issue.labels_url,
                        "comments_url" : issue.comments_url,
                        "events_url" : issue.events_url,
                        "html_url" : issue.html_url,
                        "number" : issue.number,
                        "state" : issue.state,
                        "title" : issue.title,
                        "body" : issue.body,
                        "user" : self.get_user_info(issue.user),
                        "assignee" : self.get_user_info(issue.assignee),
                        "comments" : issue.comments,
                        "closed_at" : None if issue.closed_at is None else issue.closed_at.isoformat(),
                        "created_at": None if issue.created_at is None else issue.created_at.isoformat(),
                        "updated_at" : None if issue.updated_at is None  else issue.updated_at.isoformat()
                        }
            issues.append(dic_issue)
        return issues
    
    def get_user_info(self, user):
        dic_user_info = {"login" : user.login,
                         "id": user.id,
                         "avatar_url": user.avatar_url,
                         "gravatar_id" : user.gravatar_id,
                         "url": user.id,
                         "html_url" : user.html_url,
                         "followers_url" : user.followers_url,
                         "gists_url" : user.gists_url,
                         "starred_url" : user.starred_url,
                         "subscriptions_url" : user.subscriptions_url,
                         "organizations_url" : user.organizations_url,
                         "repos_url" : user.repos_url,
                         "events_url" : user.events_url,
                         "received_events_url" : user.received_events_url,
                         "type" : user.type
                         }
                         
        return dic_user_info

    def get_milestone(self, milestone):
        milestone_dic = {"url" : milestone.url,
                         "hmtl_url" : milestone.html_url,
                         "labels_url" : milestone.labels_url,
                         "id" : milestone.id,
                         "number" : milestone.number,
                         "state" : milestone.state,
                         "title" : milestone.title,
                         "description" : milestone.description,
                         "creator" : self.get_user_info(milestone.creator),
                         "open_issues" : milestone.open_issues,
                         "closed_issues" : milestone.closed_issues,
                         "created_at": milestone.created_at,
                         "updated_at" : get_isoformat_date(milestone.updated_at),
                         "closed_at": get_isoformat_date(milestone.closed_at),
                         "due_on" : get_isoformat_date(milesonte.due_on)
                         }

    def to_JSON(self, obj):
        return json.dumps(obj, skipkeys=True, default=lambda o: o.__dict__,sort_keys=True, indent=4)

    def get_isoformat_date(self, date):
        return None if date is None else date.isoformat()
