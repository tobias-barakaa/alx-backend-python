#!/usr/bin/env python3

"""Test suite for the GithubOrgClient class."""

from parameterized import parameterized
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={'example_key': 'example_value'})
    def test_org(self, org_name, mock_get_json):
        """
        Test the GithubOrgClient.org method.

        Parameters:
            - org_name: Name of the GitHub organization to test.
            - mock_get_json: Mock object for the get_json function.

        This test verifies that the GithubOrgClient.org method returns the
        expected result and that the get_json function is called with the
        correct URL.
        """
        client = GithubOrgClient(org_name)
        result = client.org()
        expected_url = f'https://api.github.com/orgs/{org_name}'
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, {'example_key': 'example_value'})
