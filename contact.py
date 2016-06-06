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



# def main():
#     """
#     Driver method to create contact list, add contacts, search contacts
#     """
#     contact_app = Trie()
#
#     # map for storing different options
#     options = {
#             1 : contact_app.add_contact,
#             2 : contact_app.search_contact,
#             3 : contact_app.exit_app
#     }
#
#     while True:
#         try:
#             option = input("1. Add Contact\t2. Search Contact\t3.Exit\n")
#         except:
#             # Exception for invalid user input
#             raise TypeError("Expected an integer")
#
#         if option == 3:
#             options[3]()
#             break
#
#         elif option == 1:
#             contact_name = raw_input("Enter name: ")
#             options[option](contact_name)
#
#         elif option == 2:
#             contact_name = raw_input("Enter name: ")
#             matched_contacts = options[option](contact_name)
#             matched_contacts.sort(key=len, reverse=False) # Ranking contacts
#             for i in matched_contacts:
#                 if (len(contact_name) <= len(i)):
#                     print i
#
#         else:
#             print "Invalid option"
#
# if __name__ == '__main__':
#     main()
