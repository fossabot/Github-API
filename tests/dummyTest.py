#! /usr/bin/env python

import unittest
from team9 import GithubUser
from unittest.mock import patch


class GithubUserTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        repos = self.initRepo(self)
        github = MagicMock()
        user = MagicMock()
        user.get_repos.return_value = repos
        github.get_user.return_value = user
        self.GithubUser = GithubUser.GithubUser(github)

    def initRepo(self):
        repo = MagicMock()
        repo.id = 1
        repo.name = "Aziz"
        repo.html_url = "Aziz.com"
        repo.language = "Python"
        repo.get_languages.return_value = {"Java": 40000, "C": 45000}
        repo.open_issues_count = 75
        contributors = self.init_contributors(self)
        repo.get_contributors.return_value = contributors
        branches = self.init_branches(self)
        repo.get_branches.return_value = branches
        issues = self.init_issues(self)
        repo.get_issues.return_value = issues

        return [repo]

    def init_contributors(self):
        contributor = MagicMock()
        contributor.login = "Aziz"
        contributor.id = 2
        contributor.avatar_url = "https://github.com/images/Aziz"
        contributor.html_url = "Aziz.com"
        contributor.type = "User"
        contributor.contributions = 150

        return [contributor]

    def init_branches(self):
        branch = MagicMock()
        branch.name = "master"
        commit = MagicMock()
        commit.sha = "sha"
        commit.url = "url"
        branch.commit = commit

        return [branch]

    def test_givenAGithubUserWhenAskedToGetHisProjectsThenAllOfThemShouldBeReturned(self):
        projects = self.GithubUser.get_projects()
        self.assertEqual(len(projects), 1)

    def test_givenAGithubUserWhenAskedToGetHisProjectsThenProjectIdShouldBeCorrect(self):
        projects = self.GithubUser.get_projects()
        self.assertEqual(projects[0].get("id"), 1)

    def test_givenAGithubUserWhenAskedToGetHisProjectsThenProjectIdShouldBeCorrect(self):
        projects = self.GithubUser.get_projects()
        self.assertEqual(projects[0].get("id"), 1)

    def test_givenAGithubUserWhenAskedToGetHisProjectsThenProjectNameShouldBeCorrect(self):
        projects = self.GithubUser.get_projects()
        self.assertEqual(projects[0].get("name"), "Aziz")

    def test_givenAGithubUserWhenAskedToGetHisProjectsThenProjectHtml_urlShouldBeCorrect(self):
        projects = self.GithubUser.get_projects()
        self.assertEqual(projects[0].get("html_url"), "Aziz.com")

    def test_givenAGithubUserWhenAskedToGetHisProjectsThenProjectlanguageShouldBeCorrect(self):
        projects = self.GithubUser.get_projects()
        self.assertEqual(projects[0].get("language"), "Python")

    def test_givenAGithubUserWhenAskedToGetHisProjectsThenProjectlanguagesShouldBeCorrect(self):
        projects = self.GithubUser.get_projects()
        self.assertEqual(projects[0].get("languages"), {
                         "Java": 40000, "C": 45000})

    def test_givenAGithubUserWhenAskedToGetHisProjectsThenOpenIssuesCountShouldBeCorrect(self):
        projects = self.GithubUser.get_projects()
        self.assertEqual(projects[0].get("open_issues_count"), 75)

    def test_givenAGithubUserWhenAskedToGetHisProjectsThenProjectContributorsShouldBeAllPresent(self):
        projects = self.GithubUser.get_projects()
        self.assertEqual(len(projects[0].get("contributors")), 1)

    def test_givenAGithubUserWhenAskedToGetHisProjectsThenProjectContributorsInformationShouldBeCorrect(self):
        projects = self.GithubUser.get_projects()
        contributor = projects[0].get("contributors")[0]
        self.assertEqual(contributor.get("id"), 2)
        self.assertEqual(contributor.get("login"), "Aziz")
        self.assertEqual(contributor.get("avatar_url"),
                         "https://github.com/images/Aziz")
        self.assertEqual(contributor.get("html_url"), "Aziz.com")
        self.assertEqual(contributor.get("type"), "User")
        self.assertEqual(contributor.get("contributions"), 150)

    def test_givenAGithubUserWhenAskedToGetHisProjectsThenProjectBranchesShouldAllBePresent(self):
        projects = self.GithubUser.get_projects()
        self.assertEqual(len(projects[0].get("branches")), 1)

    def test_givenAGithubUserWhenAskedToGetHisProjectsThenProjectBranchesShouldContainTheRightInformations(self):
        projects = self.GithubUser.get_projects()
        branches = projects[0].get("branches")[0]
        self.assertEqual(branches.get("name"), "master")
        self.assertEqual(branches.get("commit").get("sha"), "sha")
        self.assertEqual(branches.get("commit").get("url"), "url")

    def test_givenAGithubUserWhenAskedToGetHisProjectsThenProjectIssuesShouldAllBePresent(self):
        projects = self.GithubUser.get_projects()
        self.assertEqual(len(projects[0].get("open_issues")), 1)

    def test_givenAGithubUserWhenAskedToGetHisProjectsThenProjectIssuesInformationShoulBeCorrect(self):
        projects = self.GithubUser.get_projects()
        issue = projects[0].get("open_issues")[0]
        self.assertEqual(issue.get("id"), 3)
        self.assertEqual(issue.get("url"), "issue_url")
        self.assertEqual(issue.get("repository_url"), "repository_url")
        self.assertEqual(issue.get("labels_url"), "labels_url")
        self.assertEqual(issue.get("comments_url"), "comments_url")
        self.assertEqual(issue.get("events_url"), "events_url")
        self.assertEqual(issue.get("html_url"), "html_url")
        self.assertEqual(issue.get("number"), 5)
        self.assertEqual(issue.get("state"), "open")
        self.assertEqual(issue.get("title"), "title")
        self.assertEqual(issue.get("body"), "git gud or git rekt")
        self.assertEqual(issue.get("assignee"), None)
        self.assertEqual(issue.get("milestone"), None)
        self.assertEqual(issue.get("labels"), None)
        self.assertEqual(issue.get("pull_request"), None)
        self.assertEqual(issue.get("comments"), "comments")

    def test_givenAGithubUserWhenAskedToGetHisProjectsThenProjectIssuesUserInformationShoulBeCorrect(self):
        projects = self.GithubUser.get_projects()
        issue = projects[0].get("open_issues")[0]
        user = issue.get("user")
        self.assertEqual(user.get("login"), "login")
        self.assertEqual(user.get("id"), 5)
        self.assertEqual(user.get("avatar_url"), " avatar_url")
        self.assertEqual(user.get("gravatar_id"), 9)
        self.assertEqual(user.get("url"), "user_url")
        self.assertEqual(user.get("html_url"), "html_url")
        self.assertEqual(user.get("followers_url"), " followers_url")
        self.assertEqual(user.get("gists_url"), "gists_url")
        self.assertEqual(user.get("starred_url"), "starred_url")
        self.assertEqual(user.get("subscriptions_url"), "subscriptions_url")
        self.assertEqual(user.get("organizations_url"), "organizations_url")
        self.assertEqual(user.get("repos_url"), "repos_url")
        self.assertEqual(user.get("events_url"), "events_url")
        self.assertEqual(user.get("received_events_url"),
                         "received_events_url ")
        self.assertEqual(user.get("type"), "user")

    def init_issues(self):
        issue = MagicMock()
        repository = MagicMock()
        repository.url = "repository_url"
        issue.id = 3
        issue.url = "issue_url"
        issue.repository = repository
        issue.labels_url = "labels_url"
        issue.comments_url = "comments_url"
        issue.events_url = "events_url"
        issue.html_url = "html_url"
        issue.number = 5
        issue.state = "open"
        issue.title = "title"
        issue.body = "git gud or git rekt"
        issue.user = self.init_user(self)
        issue.assignee = None
        issue.milestone = None
        issue.labels = None
        issue.comments = "comments"
        issue.pull_request = None
        return [issue]

    def init_user(self):
        user = MagicMock()

        user.login = "login"
        user.id = 5
        user.avatar_url = " avatar_url"
        user.gravatar_id = 9
        user.url = "user_url"
        user.html_url = "html_url"
        user.followers_url = " followers_url"
        user.gists_url = "gists_url"
        user.starred_url = "starred_url"
        user.subscriptions_url = "subscriptions_url"
        user.organizations_url = "organizations_url"
        user.repos_url = "repos_url"
        user.events_url = "events_url"
        user.received_events_url = "received_events_url "
        user.type = "user"

        return user


def main():
    unittest.main()


if __name__ == "__main__":
    main()
