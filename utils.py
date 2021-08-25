"""
File: utils.py
Author: https://github.com/atidyshirt
Version: < 1
"""

def strip_whitespace(string: str) -> str:
    """ Strip prefix and suffix whitespace from a string """
    if string[-1] == " ":
        string = "".join(string.rstrip())
    if string[0] == " ":
        string = "".join(string.lstrip())
    return string
