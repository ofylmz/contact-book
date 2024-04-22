import sqlite3


def create_db():
    conn = sqlite3.connect('contact_database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
               (id INTEGER PRIMARY KEY,
               first_name TEXT,
               last_name TEXT,
               phone_number TEXT)''')
    conn.commit()
    conn.close()

def create_contact():
    first_name=(input("First Name:"))
    last_name = input("Last Name:")
    phone_number = input("Phone Number:")

    conn = sqlite3.connect('contact_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT*FROM contacts WHERE first_name = ? and last_name = ?',(first_name,last_name))
    result=cursor.fetchone()

    if result :
        print("Contact has been already created.")    
    else:
        cursor.execute("INSERT INTO contacts(first_name,last_name,phone_number) VALUES (?,?,?)",
                   (first_name,last_name,phone_number) )
        conn.commit()
        print("Contact created succesfully.")    
    conn.close
    

def search_contact():
    search=input("Search:")

    conn=sqlite3.connect('contact_database.db')
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM contacts WHERE first_name LIKE ? or last_name LIKE ? or phone_number LIKE ?',
                   ('%'+search+'%','%'+search+'%','%'+search+'%'))              
    results=cursor.fetchall()
    conn.close

    if results == []:
        print("Contact not found")
    else:
        print(results)




def edit_contact():
    print("---Edit Contact Menu---")
    print("---1.Edit First Name")
    print("---2.Edit Last Name")
    print("---3.Edit Phone Number")

    edit_selection=input("Choose what you want to edit:")
    if edit_selection == '1':
        edit_firstname()
    elif edit_selection == '2':
        edit_lastname()
    elif edit_selection == '3':
        edit_phonenumber()
    else:
        print("Invalid selection.")

def edit_firstname():
    firstname_selection = input("Enter the first name of the contact that you want to edit: ")
    lastname_selection = input("Enter the last name of the contact that you want to edit: ")
    new_firstname = input("Enter the new first name: ")

    conn = sqlite3.connect('contact_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT first_name FROM contacts WHERE first_name = ? and last_name = ?',
                   (firstname_selection, lastname_selection))
    row = cursor.fetchone()

    if row:
        cursor.execute('UPDATE contacts SET first_name = ? WHERE first_name = ? and last_name = ?',
                       (new_firstname, firstname_selection, lastname_selection))
        conn.commit()
        print("First name updated successfully.")
    else:
        print("Contact not found.")

    conn.close


def edit_lastname():
    firstname_selection = input("Enter the first name of the contact that you want to edit: ")
    lastname_selection = input("Enter the last name of the contact that you want to edit: ")
    new_lastname = input("Enter the new last name: ")

    conn = sqlite3.connect('contact_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT last_name FROM contacts WHERE first_name = ? and last_name = ?',
                   (firstname_selection, lastname_selection))
    row_lastname = cursor.fetchone()

    if row_lastname:
        cursor.execute('UPDATE contacts SET last_name = ? WHERE first_name = ? and last_name = ?',
                       (new_lastname, firstname_selection, lastname_selection))
        conn.commit()
        print("Last name updated successfully.")
    else:
        print("Contact not found.")

    conn.close

def edit_phonenumber():
    firstname_selection = input("Enter the first name of the contact that you want to edit: ")
    lastname_selection = input("Enter the last name of the contact that you want to edit: ")
    new_phonenumber = input("Enter the new phone number: ")

    conn = sqlite3.connect('contact_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT phone_number FROM contacts WHERE first_name = ? and last_name = ?',
                   (firstname_selection, lastname_selection))
    row_phonenumber = cursor.fetchone()

    if row_phonenumber:
        cursor.execute('UPDATE contacts SET phone_number = ? WHERE first_name = ? and last_name = ?',
                       (new_phonenumber, firstname_selection, lastname_selection))
        conn.commit()
        print("Phone number updated successfully.")
    else:
        print("Contact not found.")

    conn.close
    

def delete_contact():
    del1 = input("First Name:")
    del2 = input("Last Name:")

    conn=sqlite3.connect('contact_database.db')
    cursor=conn.cursor()
    cursor.execute('SELECT*FROM contacts WHERE first_name = ? and last_name = ?' , (del1, del2))
    result_del=cursor.fetchone()

    if result_del:
        cursor.execute('DELETE FROM contacts WHERE first_name = ? and last_name = ?' , (del1, del2))
        conn.commit()
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

    conn.close


    
def main_menu():
    while True:
        print("---Menu---")
        print("---Create new contact[c]")
        print("---Search Contact[s]")
        print("---Edit Contact[e]")
        print("---Delete Contact[d]")
        
        choice = input("Enter your choice: ")
        
        if choice == 'c':
            create_contact()
        elif choice == 's':
            search_contact()
        elif choice == 'e':
            edit_contact()
        elif choice == 'd':
            delete_contact()
        else:
            print("Invalid choice. Please enter a valid option.")

create_db()
main_menu()