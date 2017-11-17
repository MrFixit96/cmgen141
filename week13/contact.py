#Program: Contact Manager
#File: contact.py
#Date: 16-Nov-2017
#Author: James Anderton
#Purpose: A class to instantiate a contact object for an address book

# #########################################################
# #
# #     CLASS: Contact
# #
# #########################################################

class Contact:
    #The __init__ method initializes the attributes
    def __init__(self, name, phone, email, dob):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__dob = dob
    # EndSub

    def set_name(self, name):
        self.__name = name
    # EndSub

    def get_name(self, name):
        return self.__name
    # EndSub

    def set_phone(self, phone):
        self.__phone = phone
    # EndSub

    def get_phone(self, phone):
        return self.__phone
    # EndSub

    def set_email(self, email):
        self.__email = email
    # EndSub

    def get_email(self, email):
        return self.__email
    # EndSub

    def set_dob(self, dob):
        self.__dob = dob
    # EndSub

    def get_dob(self, dob):
        return self.dob
    # EndSub

    #The __str__ method returns the object's state as a string
    def __str__method(self):
        return "Name:", self.__name, \
                "\nPhone:", self.__phone, \
               "\nEmail:", self.__email, \
               "\nDOB:", self.__dob

#  EndClass