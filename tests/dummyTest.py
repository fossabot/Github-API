#! /usr/bin/env python

import unittest
from team9 import GithubUser
from github import Github
from unittest.mock import MagicMock
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

        return [repo]

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
        self.assertEqual(projects[0].get("languages"), {"Java": 40000, "C": 45000})


def main():
    unittest.main()


if __name__ == "__main__":
    main()
