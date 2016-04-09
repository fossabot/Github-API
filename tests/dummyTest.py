#! /usr/bin/env python

import unittest
from team9 import GithubUser
from unittest.mock import MagicMock


class GithubUserTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        repos = self.initRepo(self)
        github = MagicMock()
        user = MagicMock()
        user.get_repos = repos
        github.get_user = user
        self.GithubUser = GithubUser.GithubUser(github)

    def initRepo(self):
        repo = MagicMock()
        repo.id = 1
        repo.name = "Aziz"
        repo.html_url = "Aziz.com"
        repo.language = "Python"
        repo.get_languages = {"Java": 40000, "C": 45000}

        return [repo]

    def test_starting_out(self):
        projects = self.GithubUser.get_projects()
        self.assertEqual(len(projects), 1)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
