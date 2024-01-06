#!/usr/bin/env python3
"""
function test
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    nested map
    """
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
       ({}, ("a",), "a"),
       ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(context.exception.args[0], expected_key)


class TestGenJson(unittest.TestCase):
    """
    test json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload):
        """
        test json
        """
        mock = unittest.mock.Mock()
        mock.json.return_value = test_payload
        with unittest.mock.patch('requests.get', return_value=mock):
            self.assertEqual(get_json(test_url), test_payload)
            mock.json.assert_called_once()
