#Door lock system Challenge – Task One (Day 3)

#1. Write a python program that simulates a door lock system such that:

#Password is set and stored in a variable,
#Commands to instruct the door are stored in variables.
#When a user enters the wrong password an error message is displayed and prompted to enter the password again.
#When a user enters “open” a “The door is now open” statement is displayed, when the “open” is entered more that once, a message is displayed saying, “the door is already open” 
#When a user enters “close” a “The door is now locked” statement is displayed, when the “open” is entered more that once, a message is displayed saying, “the door is already locked”
#When a user enters “quit” the process is terminated and message is displayed.
#When a wrong message is entered or invalid key pressed a “Invalid input” message is displayed. 
#When the door is locked or open, it prints out the last date/time the door was opened, eg “Door Last open  at 2022-07-05 08:46:20.535395”


import datetime

username = ""
password = ""
door_command = ""
door_last_opened = datetime.datetime.now()

if not username:
    print("No user registered, please register")
    print("Enter username")
    username = input()
    while username == "":
        print("Username cannot be empty")
        username = input()
    print("Enter password")
    password = input()
    while password == "":
        print("Password cannot be empty")
        password = input()
    print("Re-enter password")
    confirm_password = input()
    while password != confirm_password:
        print("Passwords do not match, please re-enter password")
        confirm_password = input()

while door_command != "quit":
    print("Enter door command eg Open, Close, Quit")
    command = input()
    if command == door_command and door_command == "open":
        print("The door is already open")
        continue
    elif command == door_command and door_command == "close":
        print("The door is already locked")
        continue
    if command == "open":
        print("The door was last opened " + str(door_last_opened))
        door_last_opened = datetime.datetime.now()
        door_command = command
        print("The door is now open")
    if command == "close":
        print("The door was last opened " + str(door_last_opened))
        door_command = command
        print("The door is now locked")
    if command == "quit":
        print("Goodbye")
        break
    if command != "open" and command != "close" and command != "quit":
        print("Invalid input")
        continue
