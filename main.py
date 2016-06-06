#!/usr/bin/env python

from contact import Trie
from collections import defaultdict

def main():
    """
    Driver method to create contact list, add contacts, search contacts
    """
    contact_app = Trie()
    last_name_trie = Trie()
    # map for storing different options
    options_for_full_name = {
            1 : contact_app.add_contact,
            2 : contact_app.search_contact,
            3 : contact_app.exit_app
    }

    options_for_last_name = {
            1 : last_name_trie.add_contact,
            2 : last_name_trie.search_contact,
            3 : last_name_trie.exit_app
    }

    last_name_dict = defaultdict(list)
    last_name_list = []


    while True:
        list_of_first_names = []
        list_of_final_full_names = []
        final_search_result = []

        try:
            option = input("1. Add Contact\t2. Search Contact\t3.Exit\n")
        except:
            # Exception for invalid user input
            raise TypeError("Expected an integer")

        if option == 3:
            options_for_full_name[3]()
            break

        elif option == 1:
            contact_name = raw_input("Enter name: ")
            contact_name = contact_name.strip()
            options_for_full_name[option](contact_name)
            if ' ' in contact_name:
                last_name = contact_name.split(' ')[1]
                last_name_dict[last_name].append(contact_name)
                options_for_last_name[option](last_name)

        elif option == 2:
            list_of_final_full_names = []
            search_string = raw_input("Enter name: ").strip()
            matched_full_name = options_for_full_name[option](search_string)
            matched_last_name = options_for_last_name[option](search_string)
            matched_full_name.sort(key=len, reverse=False) # Ranking contact name

            for i in matched_full_name:
                if (len(search_string) <= len(i)):
                    list_of_first_names.append(i)

            for j in matched_last_name:
                for k in range(0, len(last_name_dict[j])):
                    list_of_final_full_names.append(last_name_dict[j][k])

            final_search_result = list(set(list_of_first_names) | set(list_of_final_full_names))
            final_search_result.sort(key=len, reverse=False)

            for name in final_search_result:
                print name

        else:
            print "Invalid option"

if __name__ == '__main__':
    main()
