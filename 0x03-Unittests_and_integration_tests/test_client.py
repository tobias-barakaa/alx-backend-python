#!/usr/bin/env python3

"""Test suite for the GithubOrgClient class."""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @patch('client.get_json')
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    def test_org(self, org_name, mock_get_json):
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with
        (f"https://api.github.com/orgs/{org_name}")
