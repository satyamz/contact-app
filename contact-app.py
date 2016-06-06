#!/usr/bin/env python
"""
implementation of contact application.
for implementation of contact application trie data structure is used.
"""


class Node:
    """
    Node class for node in trie.
    """

    def __init__(self):         # Node Constructor
        self.contact = None
        self.nodes = {}
    def __add_contact__(self, contact, string_postion=0):
        prefix_letter = contact[string_postion]

        if prefix_letter not in self.nodes:
            self.nodes[prefix_letter] = Node();

        if (string_postion + 1 == len(contact)):
            self.nodes[prefix_letter].contact = contact
        else:
            self.nodes[prefix_letter].__add_contact__(contact, string_postion + 1)
        return True

    def search_contact(self, prefix, string_postion):
        """
        Return contacts based on prefix
        """
        contact_list = list()
        for key, node in self.nodes.iteritems():
            if(key == prefix[string_postion] or string_postion >= len(prefix)):
                if (node.contact is not None):
                    contact_list.append(node.contact)
            if (node.nodes != {}):
                if (string_postion + 1 <= len(prefix)):
                    contact_list += node.search_contact(prefix, string_postion+1)
                else:
                    contact_list += node.search_contact(prefix, string_postion)

        return contact_list
