import json
import os
from os import system


def __init__(self, n):
    name = f'{n} Library'
    password = 'admin'
def addperson(name, filename='people.json'):
    with open('people.json') as json_file:
        peoplee = json.load(json_file)
        dictionary_name = peoplee
        key = name
        value = 'nonadmin'
        dictionary_name[key] = value
        json_object = json.dumps(peoplee, indent=4)
        with open("people.json", "w") as outfile:
            outfile.write(json_object)
        Run(False, name, 1)
def displaybooks(isAdmin, name):
    if isAdmin == True:
        with open('books.json') as json_file:
            peoplee = json.load(json_file)
            print("Following is the list of books")
            for item, amount in peoplee.items():
                print("{} ({})".format(item, amount))
    else:
        with open('books.json') as json_file:
            peoplee = json.load(json_file)
            print("Following is the list of books")
            for item, amount in peoplee.items():
                if amount == "available":
                    print("{}".format(item))
        print(f'List of all books without details for customer')
    print('Press Enter to continue')
    aaa = input()
    Run(isAdmin, name, 2)
def lendbook(isAdmin, name):
    while True:
        print(f'Following is the List of Books you can lend:-')
        with open('books.json', 'r') as json_file:
            books = json.load(json_file)
            for key, value in books.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
                if value == 'available':
                    print("{}".format(key))
        print(f'Enter tne name if the book you want to lend')
        lend = input()
        with open('books.json') as json_file:
            books = json.load(json_file)
            if lend in books:
                books[lend] = f'with {name}'
                json_object = json.dumps(books, indent=4)
                with open("books.json", "w") as outfile:
                    outfile.write(json_object)
                print(f'Please Collect your book from the counter')
                print(f'Do you want to lend another book?(y/n)')
                c = input()
                if c == 'y':
                    continue
                else:
                    Run(isAdmin, name, 2)
            else:
                print(f"'{lend}' is not available with us \nDo You want to choose again(y/n)")
                choice = input()
                if choice == 'y':
                    continue
                else:
                    Run(isAdmin, name, 2)
def returnbook(isAdmin, name):
    with open('books.json', 'r') as json_file:
        books = json.load(json_file)
        if f'with {name}' in books.values():
            for key, value in books.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
                if value == f'with {name}':
                    print('Enter the name of the book you want ot return')
                    ret = input()
                    if ret==key:
                        books[ret] = 'available'
                        jsonString = json.dumps(books)
                        with open('books.json', 'w') as json_file:
                            json_file.write(jsonString)
                        print('ThankYou for returning the book')
                        print('Restarting........')
                        Run(isAdmin, name, 2)
                    else:
                        print("You have not lended any book like this")
                        Run(isAdmin, name, 2)
        

                

def addbook(args, isAdmin, name):
    with open('books.json', 'r') as json_file:
        books = json.load(json_file)
        print("Enter the name of the book")
        nnn = input()
        books[nnn]='available'
        jsonString = json.dumps(books)
        with open('books.json', 'w') as json_file:
            json_file.write(jsonString)
        print('Done')
        print('Restarting....')
        Run(isAdmin, name,2)
def removebook(self, isAdmin, name):
    with open('books.json', 'r') as json_file:
        books = json.load(json_file)
        print("Enter the name of the book")
        nnn = input()
        del books[nnn]
        jsonString = json.dumps(books)
        with open('books.json', 'w') as json_file:
            json_file.write(jsonString)
        print('Done')
        print('Restarting....', 'yellow')
        Run(isAdmin, name,2)

def blockperson(args, isAdmin, name,):
    with open('people.json', 'r') as json_file:
        people = json.load(json_file)
        print('Enter the name of the person you want to block')
        ret = input()
        people[ret] = 'blocked'
        print(people)
        jsonString = json.dumps(people)
        with open('people.json', 'w') as json_file:
            json_file.write(jsonString)
        print(f'You have successfully blocked{ret}')
        print('Restarting........')
        Run(isAdmin, name, 2)



# functions
def exists(a):
    with open('people.json', 'r+') as json_file:
        people = json.load(json_file)
        key_to_lookup = a
        if key_to_lookup in people:
            return True
        else:
            return False


def isAdmin(a):
    with open('people.json') as json_file:
        people = json.load(json_file)
        if people[a] == "admin":
            return True
        else:
            return False

def isNotBlocked(a):
    with open('people.json') as json_file:
        people = json.load(json_file)
        if people[a] != "blocked":
            return True
        else:
            return False

def Run(isAdmin, name, count):
    if isAdmin == True:
        os.system("clear")
        if count == 1:
            print(f'Welcome Admin {name}. Choose any options from below\n')
        else:
            print(f'Choose any options from below\n')
        print(f'\
d - for Displaying Books \n\
l - for Lending a Book\n\
r - for Returning a book\n\
a - for Adding a book\n\
rm - for Removing a book\n\
bl - for Blocking a Person\n\
lo - for logging out of the session')
        choice = input()
        if choice == 'd':
            displaybooks(isAdmin, name)
        elif choice == 'l':
            lendbook(isAdmin, name)
        elif choice == 'r':
            returnbook(isAdmin, name)
        elif choice == 'a':
            addbook(isAdmin, name)
        elif choice == 'rm':
            removebook(isAdmin, name)
        elif choice == 'bl':
            blockperson(isAdmin, name)
        elif choice == 'lo':
            Go()

    else:
        os.system("clear")
        if count == 1:
            print(f'Welcome {name}. Choose any options from below\n')
        else:
            print(f'Choose any options from below\n')
        print(f'\
d - for Displaying Books \n\
l - for Lending a Book\n\
r - for Returning a book\n\
lo - for Logging out')
        choice = input()
        if choice == 'd':
            displaybooks(isAdmin, name)
        elif choice == 'l':
            lendbook(isAdmin, name)
        elif choice == 'r':
            returnbook(isAdmin, name)
        elif choice == 'lo':
            Go()


        clear = lambda: system('clear')
def Go():
    print(f"Welcome to 'The Library Management System' \nEnter Your Name")
    n = input()
    if exists(n):
        print(f'Welcome {n}')
        if isAdmin(n):
            if isNotBlocked(n):
                print('You are an admin\n')
                while True:
                    print(f'Enter Your Password:')
                    p = input()
                    if p == "alpraj":
                        print("ThankYou for verfication")
                        Run(True, n, 1)
                    else:
                        print("Wrong password!!!! Try again")
                        continue
            else:
                print('You are blocked by admin. You cannot use the library')
                print('Restarting the program........')
        else:
            if isNotBlocked(n):
                Run(False, n, 1)
            else:
                print('You are blocked by admin. You cannot use the library')
                print('Restarting the program........')
    else:
        print("You doesn't exist in the customer list\nTo register yourself press Enter and for leaving type exit")
        newlogin = input()
        if newlogin == "":
            addperson(n)

# Logic
Go()
