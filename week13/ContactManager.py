#Program: Contact Manager
#File: ContactManager.py
#Date: 16-Nov-2017
#Author: James Anderton
#Purpose: A class to instantiate a contact object for an address book
import week13.contact
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'contacts.dat'



#########################################################
#
#   SUB: Main
#
#########################################################
def Main():
   #load the existing contact dictionary and assign it to myContacts
    myContacts = load_contacts()

    #variable for menu choice
    choice = 0
    while choice != QUIT:
       choice = get_menu_choice()

       if choice == LOOK_UP:
           look_up(myContacts)
       elif choice == ADD:
           #TODO:Make Sure to create and call validate_date()
           add(myContacts)
       elif choice == CHANGE:
           # TODO:Make Sure to create and call validate_date()
           pass
       elif choice == DELETE:
           delete(myContacts)
       elif choice == QUIT:
           print('Exiting Program...')
           quit(0)
       else:
           pass

       #eventually save the dictionary to a file
       save_contacts(myContacts)

# EndSub

def add(myContacts):
    name = input('Name: ')
    phone = input('Phone: ')
    email = input('Email: ')
    date = input('Enter the date of birth mm/dd/yyyy')
    mm,dd,yyyy = date.split('/')
    dd = int(dd)
    mm = int(mm)
    yyyy = int(yyyy)

    if (mm == 1 or mm ==3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm ==12_):
        max1 = 31
    elif (mm == 4 or mm == 6 or mm == 9 or mm == 11):
        max1 = 30
    elif (yyyy%4 == 0 and yyyy%100 != 0 or yyyy %400 == 0):
        max1 = 29
    else:
        max1 = 28

    if mm< 1 or mm > 12:
        print('Dat is not valid')
        dob = '00/00/0000'
    elif dd < 1 or dd > max1:
        print('Dat is not valid')
        dob = '00/00/0000'
    else:
        dob = date

    entry = week13.contact.Contact(name, phone, email, dob)

    if name not in myContacts:
        myContacts[name] = entry
        print('The entry was added.')
    else:
        print('The entry already exists.')

#########################################################
#
#   SUB: look_up
#
#########################################################
def look_up(myContacts):
    name = input('Enter a name: ')
    print(myContacts.get(name, 'That name is not found.'))
# EndSub

#########################################################
#
#   SUB: delete
#
#########################################################
def delete(myContacts):
    name = input('Enter a name to delete: ')
    if name in myContacts:
        del myContacts[name]
        print('Entry deleted.')
    else:
        print(myContacts.get(name, 'That name is not found.'))

# EndSub


#########################################################
#
#   SUB: save_contacts
#
#########################################################
def save_contacts(myContacts):
    output_file = open(FILENAME, 'wb')
    pickle.dump(myContacts, output_file)
    output_file.close()

# EndSub

#########################################################
#
#   SUB: get_menu_choice
#
#########################################################
def get_menu_choice():
    print()
    print('=== I Cheat Clients (ICC) Contacts ===')
    print('1. Look up a contact')
    print('2. Add a new contact')
    print('3. Change an existing contact')
    print('4. Delete a contact')
    print('5. Quit the program')
    print()

    goodInput = False
    while not goodInput:
        try:
            choice = int(input('Enter menu number'))
            if choice >= LOOK_UP and choice <= QUIT:
                goodInput = True
            else:
                print('Entry must be a number between 1 and 5.')
        except ValueError:
            print('That is not an integer. Try again.')

    return choice

# EndSub


#########################################################
#
#   SUB: load_contacts
#
#########################################################
def load_contacts():
    try:
        #open the contacts.dat file
        input_file = open(FILENAME, 'rb')
        #unpickle the dictionary
        contact_dct = pickle.load(input_file)
        #close the file
        input_file.close()
    except IOError:
        contact_dct = {}
    return contact_dct
# EndSub


#########################################################
#
#    RUNNER: MAIN
#
#########################################################

Main()
