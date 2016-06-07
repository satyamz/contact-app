# contact-app
contact application using Trie data structure

## Features:
  * Search using last name
  * Ranking based on first name and last name

Get source:
```
$ git clone https://github.com/satyamz/contact-app.git
```
Run application:
```
$ python main.py
```

Testing application:
```
$ python test_contact.py
```

Verbose testing output :
```
$ python test_contact.py -v
```

Sample usage:

```sh
satyam@satyamz:~/contact-app$ python main.py
1. Add Contact	2. Search Contact	3.Exit
1
Enter name: satyam zode
1. Add Contact	2. Search Contact	3.Exit
1
Enter name: gunjan zode
1. Add Contact	2. Search Contact	3.Exit
1
Enter name: satyam
1. Add Contact	2. Search Contact	3.Exit
1
Enter name: saanvi
1. Add Contact	2. Search Contact	3.Exit
1
Enter name: zode milan
1. Add Contact	2. Search Contact	3.Exit
2
Enter name: sa
saanvi
satyam
satyam zode
1. Add Contact	2. Search Contact	3.Exit
2
Enter name: zo
gunjan zode
satyam zode
zode milan
1. Add Contact	2. Search Contact	3.Exit
2
Enter name: g
gunjan zode
1. Add Contact	2. Search Contact	3.Exit
2
Enter name: fp
1. Add Contact	2. Search Contact	3.Exit
3
Happy Searching
```
