#!/usr/bin/env python
import unittest
import operator


def lexicographic_sort(l, s):
    '''
    Sort list l lexicographically by string s
    '''
    # Cache scoring dictionary for custom alphabet
    precalc = calc_alphabet(s)

    # Calculate dict of word->value pairs
    d = dict()
    for word in l:
      d[word] = score_word_by_alphabet(word, precalc, len(s))
    
    # Sort via standard python sort and return.
    # Could also split off keys(), quicksort or better, and then iterate
    return sorted(d, key=d.get)

def calc_alphabet(alpha):
    '''Precalculate the required alphabet for sorting the list'''
    # Essentially, this just creates a bitfield where each letter is 2^x 
    d = dict()
    counter = 0
    for a in alpha:
      d[a] = 1 << counter
      counter += 1
    return d

def score_word_by_alphabet(word, precalcalpha, max_bits):
  # max_bits is simply the length of the alphabet here.
  total = 0
  for letter in word:
    # Should be able to AND the lower bits, but this triggers errors for me
    # And since we shift the bits by max_bits with each pass, 2 letter words
    # are ALWAYS going to sort out before three letter words, and collisions
    # are impossible. Plus, python will scale up to arbitrarily large numbers,
    # so this will keep working as long as you have ram.
    total = ( total << max_bits ) + precalcalpha[letter]

  return total


class TestLexicographicSort(unittest.TestCase):
  def test_example_1(self):
      out = lexicographic_sort(["acb", "abc", "bca"], "abc")
      self.assertEqual(out, ["abc", "acb", "bca"])

  def test_example_2(self):
      out = lexicographic_sort(["acb", "abc", "bca"], "cba")
      self.assertEqual(out, ["bca", "acb", "abc"])

  def test_example_3(self):
      out = lexicographic_sort( ["aaa","aa",""], "a")
      self.assertEqual(out, ["", "aa", "aaa"])


if __name__ == '__main__':
   unittest.main()
   print calc_alphabet("abc")
   print lexicographic_sort(["acb", "abc", "bca"], "abc")