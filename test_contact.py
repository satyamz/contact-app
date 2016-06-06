#!/usr/bin/env python
"""
Test module for testing of contact application
"""
import unittest
from contact import Trie


def fun_trie(search_string):
    """
    Function to test Trie implementation
    """
    TestTrie = Trie()
    TestTrie.add_contact("satyamz")  # Add contact to contact list
    return TestTrie.search_contact(search_string) # Search contact in contact list


class SimplisticTest(unittest.TestCase):

    def test_contact_present(self):
        """ Test case: When searched contact is present in contact list """
        self.assertEqual(fun_trie("sa"), ['satyamz'], msg="Contact isn't present")

    def test_contact_absent(self):
        """Test case: When searched contact is not present in contact list"""
        self.assertNotEqual(fun_trie("zo"), ['satyamz'], msg="Contact is present")

if __name__ == '__main__':
    unittest.main()
