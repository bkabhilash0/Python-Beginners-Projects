import sys

contacts = {9384969837:{'Full Name': 'Abhilash BK', 'First Name': 'Abhilash', 'Last Name': 'BK', 'Age': '19', 'Email': '', 'Alt.Number': ''}}

def create_contact(number):
    details = {}
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    full_name = first_name+" "+last_name
    age = input("Age: ")
    email = input("Email: ")
    ph_no_2 = input("Alternative Number: ")

    details['Full Name'] = full_name
    details['First Name'] = first_name
    details['Last Name'] = last_name
    details['Age'] = age
    details['Email'] = email
    details['Alt.Number'] = ph_no_2

    contacts[number] = details
    print("Contact successfully Added !")
    print("******************************************Successful*********************************************")
    intro()

def view_all():
    print("    Number -------------> Details")
    for key,value in contacts.items():
        print(f'{key} -------------> {value}')
    print("******************************************Successful*********************************************")
    intro()

def search_by_number(number):
    try:
        print("    Number -------------> Details")
        print(f'{number} -------------> {contacts[number]}')
        print("******************************************Successful*********************************************")
    except:
        print("No such number found")
        print("******************************************Falied**************************************************")
    finally:
        intro()

def search_by_name(name):
    contact = {}
    for k,v in contacts.items():
        for k2,v2 in v.items():
            if name in str(v2):
                contact[k] = v
    if len(contact):
        print("The contacts that match your search are:")
        print("    Number -------------> Details")
        for key,value in contact.items():
            print(f'{key} -------------> {value}')
        print("******************************************Successful*********************************************")
    else:
        print("No contact found matching your search criteria!")
        print("******************************************Falied**************************************************")
    intro()

def update_contact(number):
    try:
        print("    Number -------------> Details")
        print(f'{number} -------------> {contacts[number]}')
        details = contacts[number]
        print("Select the filed to update:")
        print("1. First Name ")
        print("2. Last Name ")
        print("3. Age ")
        print("4. Email ID ")
        print("5. Alt.Number ")

        choice = input(">> ")
        if choice == '1':
            details['First Name'] = input("First Name: ")
        elif choice == '2':
            details['Last Name'] = input("Last Name: ")
        elif choice == '3':
            details['Age'] = input("Age: ")
        elif choice == '4':
            details['Email'] = input("Email: ")
        elif choice == '5':
            details['Alt.Number'] = input("Alt No: ")
        else:
            print("Enter a Valid Choice")
            update_contact(number)
        print("******************************************Successfully Updated!***********************************")
        print("    Number -------------> Details")
        print(f'{number} -------------> {contacts[number]}')
    except:
        print("No such number found")
        print("******************************************Falied**************************************************")
    finally:
        intro()

def delete_contact(number):
    try:
        del contacts[number]
        print("******************************************Successfully Deleted!***********************************")
    except:
        print("No such contact found!!!")
    finally:
        intro()

def intro():
    print("------------------------------------------Phone Book-------------------------------------------")
    print("1. Create Contact")
    print("2. View all Contacts")
    print("3. Search by Number")
    print("4. Search by Name")
    print("5. Update a Contact")
    print("6. Delete a Contact")
    print("0. Exit")

    n = input(">> ")
    if n == '1':
        num = input("Enter the contact number: ")
        create_contact(num)
    elif n == '2':
        view_all()
    elif n == '3':
        num =  input("Enter the contact number: ")
        try:
            search_by_number(int(num))
        except :
            print("Enter a Valid input!!!")
            intro()
    elif n == '4':
        name = input("Enter the name of the contact to search: ")
        search_by_name(name)
    elif n == '5':
        num =  input("Enter the contact number: ")
        try:
            update_contact(int(num))
        except :
            print("Enter a Valid input!!!")
            intro()
    elif n == '6':
        num =  input("Enter the contact number: ")
        try:
            delete_contact(int(num))
        except :
            print("Enter a Valid input!!!")
            intro()
    elif n == '0':
        print("Thank you for Using!")
        sys.exit()
    else:
        print("Enter a Valid input!")
        intro()

intro()
