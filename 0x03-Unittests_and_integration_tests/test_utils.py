class TestAccessNestedMap(unittest.TestCase):
    """
    testing function
    """
    @parameterized.expand([
    ({'a': 1}, ('a',), 1),
    ({'a': {'b': 2}}, ('a',), {'b': 2}),
    ({'a': {'b': 2}}, ('a', 'b'), 2),    
])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
