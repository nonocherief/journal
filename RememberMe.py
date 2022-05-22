#import mysql.connector
from getpass import getpass
from mysql.connector import connect,Error

a=connect(
    host="localhost",
    user="root",
    password="",
    database="notes")


# mycursor=a.cursor()

# mycursor.execute("SELECT * From Journal")

# myresult=mycursor.fetchall()

# for x in myresult:
#     print(str(x[0])+" "+x[1])

def c():
    mycursor=a.cursor()
    mycursor.execute("SELECT * From Journal")
    myresult=mycursor.fetchall()
    for x in myresult:
        print(str(x[0])+" "+x[1])
    mycursor.close()

while True:
    c()
    print("")
    print("0 New note")
    print("1 Note delete")
    print("2 Exit")
    d=input("Which? ")
    if d=="0":
        e=input("New note: ")
        mycursor=a.cursor()
        try:
            mycursor.execute("INSERT INTO Journal(Content, Created) VALUES(%s,NOW())", (e))
            a.commit()
            mycursor.close()
        except Error as err:
            print(err)
            print("It is not possible.")
    elif d=="1":
        f=input("NoteID: ")
        mycursor=a.cursor()
        try:
            mycursor.execute("DELETE From Journal Where NoteID=%s", (f))
            a.commit()
            mycursor.close()
        except Error as err:
            print(err)
            print("It is not possible. Please select one of the number.")
    elif d=="2":
        break
    else:
        print("Please choose from the menu.")


    
