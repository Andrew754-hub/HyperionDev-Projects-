#  task_manager.py 

#=====Pseudocode section============
'''This is the section where the logic for the code is explained'''

#  Define a function called users and declare users as a dictionary.
#  Open "user.txt" for reading as a file.
#  Argue that for each line in file split line by ", " into username and password.
#  Assign password to users[username]

#  Define a fucntion called login(users)
#  Argue that while true, user must enter a username and a password. 
#  If the enetered name and password is in usernames and passwords then retrun that entered name and password.
#  Else, print invlaid username or password. 

#  Define fucntion main as the two previous functions together.

#  Argue that while true a menu is presetned with options register user, show statistics, add task,
#  View all my tasks, view tasks and extis>
#  If user enters r they will be informed that this is 
#  An admin area and they will be prompted for the admin username and password. If they provide the admin 
#  Username and password then two empty lists for username and password are decalred. 
#  Open user.txt as file and argue that for line in file lines are stripped and split.
#  Appened usernames and passwords to their respecitive lists. 
#  Prompt users to enter their username or password and prompt for password confirmation.
#  User if else statements to confrim that password and usernames are valid and not alreay in use.
#  If valid, open user file in append mode and write the username and paasowrd to the file.

#  Else if the user enters st print "Admin area" and prompt for admin username and passworde.
#  if the admin usrname and password match with "admin" and "adm1n" then open task.txt.
#  Declare variable all_tasks as a readlines of the tasks file.
#  Declare variable all_users as a readlines of the user file.
#  print and f string stating that number of users is equal to lenght of all_tasks and lenmgth of all_users

#  Else if the user enters "a" open tasks file in append mode. 
#  Argue that for line in file user is prokpted for the relevatn information about task and import current date.
#  Write all this relavent information to the file. 

#  Else if the user enters "va" then the tasks file is opened and read and all its contents is printed. 

#  Else if the user enters "vm" then the task file is opened and only the line with the entered username is printed. 

#  Else if the user enters "e" then print Goodbye and exit the code

#  Else print "invalid input please try again"

#=====importing libraries===========lines 
'''This is the section where you will import libraries'''

from datetime import date  # I researched how to import date at 
                           # www.toppr.com/guides/python

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password 
'''
def users():
    users = {}

    with open("user.txt", "r") as file:  # open file to read out values 
    
        for line in file:
            username, password = line.strip().split(", ")
            users[username] = password
        return(users)

def login(users):
    
    while True:
        entered_name = input("enter your username ")
        entered_pass = input("enter your password ")
        
        if entered_name in users and users[entered_name] == entered_pass: 
            print("login succesful")
            return(entered_name)
            
        else:
            print("invalid username or password")

def main():
    user = users()
    login_user = login(user)

    while True:

# Present the menu to the user and make sure that the user input is converted to lower case.

        menu = input('''Select one of the following options: 
r - register a user 
st - view statistics
a - add task 
va - view all tasks 
vm - view my tasks 
e - exit \n''').lower()
        
        if menu == "r":
            print("Admin area")
            admin_user = input("enter admin username")
            admin_pass = input("enter admin password")
            if admin_user == "admin" and admin_pass == "adm1n":
            
                '''This code block will add a new user to the user.txt file
                - You can use the following steps:
                    - Request input of a new username
                    - Request input of a new password
                    - Request input of password confirmation.
                    - Check if the new password and confirmed password are the same
                    - If they are the same, add them to the user.txt file,
                    otherwise present a relevant message'''

                usernames = []
                passwords = []

                with open("user.txt", "r") as file:
                    for lines in file:
                    
                        temp = lines.strip()
                        temp = lines.split(", ")

                    usernames.append(temp[0])
                    passwords.append(temp[1])
                    
                    user_name = input(" Please enter a username")
                    pass_word = input( "Please enter a password")
                    confirm_pass = input(" Please re-enter your password") 

                    if user_name in usernames:
                        print("This username already exists")

                    elif pass_word in passwords:
                        print("This password already exists")

                    elif confirm_pass != pass_word:
                        print("passwords are not the same. Rerun the program.")

                    else:
                        if pass_word == confirm_pass:
                            with open("user.txt", "a") as file:
                                file.write(f"\n{user_name}, {pass_word} ")
                            print("user registered")
                            break
            else:
                     break

        elif menu == "st":
            print(" Admin area")
            admin_user = input("enter admin username")
            admin_pass = input("enter admin password")

            if admin_user == "admin" and admin_pass == "adm1n":
                with open("tasks.txt", "r") as file:
                    all_tasks = file.readlines()

                with open("user.txt", "r") as file:
                    all_users = file.readlines()
                    
                    print(f"Total number users is {len(all_users)}. Total number tasks is {len(all_tasks)}.")        

        elif menu == "a": 
            
            '''This code block will allow a user to add a new task to task.txt file
            -  You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''
            with open("tasks.txt", "a+") as file:
                file.seek(0)
                for lines in file:
                    
                    users_name_task = input("please enter your username")
                    task_title = input("enter title of your task")
                    description_task = input("enter task description")
                    due_date = input("enter the due date")
                    todays_date = date.today()
                    task_complete = "No"
                    
                    file.write(f"""\n{users_name_task}, {task_title}, {description_task}, {due_date}, {todays_date}, {task_complete}""")
                        

        elif menu == "va":
            '''This code block will read the task from task.txt file and
            print to the console in the format of Output 2 presented in the PDF
            You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''
        
            with open("tasks.txt", "r") as file:
                for lines in file:
                    temp = lines.strip().split(", ")
                    print(temp)
                    print(lines)

        elif menu == 'vm':
        
            '''This code block will read the task from task.txt file and
            print to the console in the format of Output 2 presented in the PDF
            You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
            username you have read from the file.
            - If they are the same you print the task in the format of Output 2
            shown in the PDF '''

            with open("tasks.txt", "r") as file:
                for lines in file:
                    temp = lines.strip().split(", ")
                        
                    if temp[0] == login_user:   
                
                        print(f"Task: {temp[1]}")
                        print(f"Assigned to: {temp[0]}")
                        print(f"Date assigned: {temp[4]}")
                        print(f"Due date: {temp[3]}")
                        print(f"Task complete?: {temp[5]}")
                        print(f"Task description: {temp[2]}")

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have entered an invalid input. Please try again")   
main()