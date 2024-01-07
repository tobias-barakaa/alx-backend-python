#!/usr/bin/env python3
"""Generic utilities for github org client.
"""

from parameterized import parameterized
import unittest
from client import GithubOrgClient
from unittest.mock import patch
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={'example_key': 'example_value'})
    def test_org(self, org_name, mock_get_json):
        client = GithubOrgClient(org_name)
        result = client.org()
        expected_url = f'https://api.github.com/orgs/{org_name}'
        
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, {'example_key': 'example_value'})
