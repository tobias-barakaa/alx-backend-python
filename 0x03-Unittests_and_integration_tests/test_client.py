#!/usr/bin/env python3
"""Generic utilities for github org client.
"""

from parameterized import parameterized
import unittest
from client import GithubOrgClient
from unittest.mock import patch
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """
    function/method test
    """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    def test_org(self, org_name: str, mock_payload: Dict):
        """
        test org
        """
        with patch('client.get_json') as mock_get:
            mock_get.return_value = mock_payload
            test_class = GithubOrgClient(org_name)
            test_class.org()
            mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
            self.assertEqual(test_class._org_name, org_name)
