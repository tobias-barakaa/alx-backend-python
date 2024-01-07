#!/usr/bin/env python3

"""
Test suite for the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class.
    """
    @parameterized.expand([
            ("google"),
            ("abc"),
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """
        Test that the result of _public_repos_url is the expected one
        based on the mocked payload.
        """
        expected = "www.yes.com"
        payload = {"repos_url": expected}
        with patch('client.GithubOrgClient.org',
                   return_value=payload) as mock_method:
            client = GithubOrgClient("x")
            result = client._public_repos_url
            self.assertEqual(result, expected)
            mock_method.assert_called_once_with()

    def test_public_repos(self):
        """
        Test that the list of repos is what you expect from the chosen payload.
        """
        payload = [{"name": "Google"}, {"name": "Twttr"}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = payload
            with patch('client.get_json',
                       return_value=payload) as mock_get_json:
                client = GithubOrgClient("x")
                result = client.public_repos()
                self.assertEqual(result, ["Google", "Twttr"])
                mock_public_repos_url.assert_called_once_with()
                mock_get_json.assert_called_once_with(payload)

    @parameterized.expand([
            ({'license': {'key': 'my_license'}}, "my_license", True),
            ({'license': {'key': 'other_license'}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that GithubOrgClient.has_license returns the correct value.
        """
        client = GithubOrgClient("x")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)
