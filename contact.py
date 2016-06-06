#!/usr/bin/env python
"""
Implementation of contact application.
For implementation of contact application trie data structure is used.
"""


class Node:
    """
    Node class for node in trie.
    """

    def __init__(self):         # Node Constructor
        self.contact = None
        self.nodes = {}


    def __str__(self):
        return self.contact

    def __add_contact__(self, contact, string_postion=0):
        prefix_letter = contact[string_postion]

        if prefix_letter not in self.nodes:
            self.nodes[prefix_letter] = Node();

        if (string_postion + 1 == len(contact)):
            self.nodes[prefix_letter].contact = contact
        else:
            self.nodes[prefix_letter].__add_contact__(contact,
                                string_postion + 1)

        return True


    def __search_contact__(self, prefix, string_postion):
        """
        Return contacts based on prefix
        """
        contact_list = []

        for key, node in self.nodes.iteritems():
            if(string_postion >= len(prefix) or key == prefix[string_postion]):
                if (node.contact is not None):
                    contact_list.append(node.contact)

                if (node.nodes != {}):
                    if (string_postion + 1 <= len(prefix)):
                        contact_list += node.__search_contact__(prefix,
                                        string_postion+1)
                    else:
                        contact_list += node.__search_contact__(prefix,
                                        string_postion)

        return contact_list


class Trie:
    """ Trie class to organize nodes """

    def __init__(self):
        self.root = Node()

    def add_contact(self, contact):
        return self.root.__add_contact__(contact)

    def search_contact(self, prefix, string_postion=0):
        return self.root.__search_contact__(prefix, string_postion=0)

    def exit_app(self):
        print "Happy Searching"
        return
