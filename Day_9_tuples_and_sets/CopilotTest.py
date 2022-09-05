def is_palindrome(s):
    """
    (str) -> bool
    Return True if s is a palindrome, False otherwise.
    """
    return s == s[::-1]


def is_pangram(s):
    """
    (str) -> bool
    Return True if s is a pangram, False otherwise.
    """
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())


def find_needle_in_haystack(haystack, needle):
    """
    (list, str) -> int
    Return the index of the first occurrence of needle in haystack.
    """
    return haystack.index(needle)