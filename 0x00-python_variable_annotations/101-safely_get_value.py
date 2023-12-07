#!/usr/bin/env python3
"""
safely_get_value - Safely retrieve a value from a
dictionary with a default option.

Parameters:
    dct (Mapping): The dictionary to retrieve the value from.
    key (Any): The key to look for in the dictionary.
    default (Union[T, None], optional):
    The default value to return if the
    key is not found. Defaults to None.

Returns:
    Union[Any, T]: The value associated with the key,
    or the default value if the key is not present.
"""

from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == "__main__":
    annotations = safely_get_value.__annotations__
    print("Here's what the mappings should look like:")
    for k, v in annotations.items():
        print(f"{k}: {v}")
