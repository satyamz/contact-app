from contact import Trie

def main():
    """
    Driver method to create contact list, add contacts, search contacts
    """
    contact_app = Trie()
    last_name_trie = Trie()
    # map for storing different options
    options = {
            1 : contact_app.add_contact,
            2 : contact_app.search_contact,
            3 : contact_app.exit_app
    }

    last_name_dict = {}
    last_name_list = []


    while True:
        try:
            option = input("1. Add Contact\t2. Search Contact\t3.Exit\n")
        except:
            # Exception for invalid user input
            raise TypeError("Expected an integer")

        if option == 3:
            options[3]()
            break

        elif option == 1:
            contact_name = raw_input("Enter name: ")
            contact_name.strip()
            options[option](contact_name)
            if ' ' in contact_name:
				last_name = contact_name.split(' ')[1]
				print last_name
				last_name_list.append(last_name)

        elif option == 2:
            search_string = raw_input("Enter name: ")
            matched_contacts = options[option](search_string)
            matched_contacts.sort(key=len, reverse=False) # Ranking contacts
            for i in matched_contacts:
                if (len(search_string) <= len(i)):
                    print i

        else:
            print "Invalid option"

if __name__ == '__main__':
    main()
