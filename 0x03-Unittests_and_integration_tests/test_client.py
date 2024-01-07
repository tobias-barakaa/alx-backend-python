#!/usr/bin/env python3

"""Test suite for the GithubOrgClient class."""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google", ),
        ("abc", )
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Tests that org() returns the correct value and calls get_json once.
        """
        mock_get_json.return_value = {"key": "value"}
        client = GithubOrgClient(org_name)
        org_data = client.org()
        self.assertEqual(org_data, {"key": "value"})
        mock_get_json.assert_called_once_with
        (client.ORG_URL.format(org=org_name))
