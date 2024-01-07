#!/usr/bin/env python3

"""Test suite for the GithubOrgClient class."""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Tests that org() returns the correct value and
        calls get_json() once with the expected argument.
        """

        expected_url = GithubOrgClient.ORG_URL.format(org=org_name)
        expected_return_value = {"key": "value"}
        mock_get_json.return_value = expected_return_value
        client = GithubOrgClient(org_name)
        result = client.org()
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, expected_return_value)
