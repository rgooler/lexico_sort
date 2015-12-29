#!/usr/bin/env python
import unittest


def lexicographic_sort(l, s):
    '''
    Sort list l lexicographically by string s
    '''
    return l


class TestLexicographicSort(unittest.TestCase):
    def test_example_1(self):
        out = lexicographic_sort(["acb", "abc", "bca"], "abc")
        self.assertEqual(out, ["abc", "acb", "bca"])

    def test_example_2(self):
        out = lexicographic_sort(["acb", "abc", "bca"], "cba")
        self.assertEqual(out, ["bca", "acb", "abc"])

    def test_example_3(self):
        out = lexicographic_sort(["aaa", "aa", ""], "a")
        self.assertEqual(out, ["", "aa", "aaa"])


if __name__ == '__main__':
    unittest.main()
