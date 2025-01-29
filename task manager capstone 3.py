#  task_manager.py 

#=====Pseudocode section============
'''This is the section where the logic for the code is explained

Define a function called users and declare users as a dictionary.
Open "user.txt" for reading as a file.
Argue that for each line in file split line by ", " into username and password.
Assign password to users[username]

Define a fucntion called login(users)
Argue that while true, user must enter a username and a password. 
If the enetered name and password is in usernames and passwords then retrun that entered name and password.
Else, print invlaid username or password. 

Define fucntion main as the two previous functions together.

Argue that while true a menu is presetned with options register user, show statistics, add task,
view all my tasks, view tasks and exit.

If user enters r they will be informed that this is 
an admin area and they will be prompted for the admin username and password. 

If they provide the admin username and password then two empty lists for username and password are declared. 
 Open user.txt as file and argue that for line in file lines are stripped and split.
 Appened usernames and passwords to their respecitive lists. 
 Prompt users to enter their username or password and prompt for password confirmation.
 User if else statements to confrim that password and usernames are valid and not alreay in use.
 If valid, open user file in append mode and write the username and paasowrd to the file.

  Else if the user enters st print "Admin area" and prompt for admin username and passworde.
 if the admin usrname and password match with "admin" and "adm1n" then open task.txt.
 Declare variable all_tasks as a readlines of the tasks file.
  Declare variable all_users as a readlines of the user file.
 print and f string stating that number of users is equal to lenght of all_tasks and lenmgth of all_users

Else if the user enters "a" open tasks file in append mode. 
Argue that for line in file user is prokpted for the relevatn information about task and import current date.
Write all this relavent information to the file. 

Else if the user enters "va" then the tasks file is opened and read and all its contents is printed 
Using f string for formating.

Else if the user enters "vm" then the task file is opened and only the line with the entered username is printed
Using f string for formatting. 

 Else if the user enters "e" then print Goodbye and exit the code

 Else print "invalid input please try again" '''

#=====importing libraries===========lines 
'''This is the section where you will import libraries'''

from datetime import date  # I researched how to import date at 
                           # www.toppr.com/guides/python

from datetime import datetime

#====Login Section====
credentials_users = {}

def users():

    with open("user copy.txt", "r") as file:  # open file to read out values 
    
        for line in file:
            username, password = line.strip().split(", ")
            credentials_users[username] = password
        return(credentials_users)

def login():

    users()

    while True:
        entered_name = input("Enter your username ")
        entered_pass = input("Enter your password ")
        
        if entered_name in credentials_users and credentials_users[entered_name] == entered_pass: 
            print("login succesful")
            return(entered_name)
            
        else:
            print("invalid username or password")
        
def authentic_admin():

    admin_user = input("Enter admin username ")
    admin_pass = input("Enter admin password ") 
    if admin_user == "admin" and admin_pass == "adm1n":
        return admin_user == "admin" and admin_pass == "adm1n"

def reg_user():

            print("Admin area")
        
            usernames = []
            passwords = []

            with open("user copy.txt", "r") as file:
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

def display_statistics():

    print("Admin area")

    with open("tasks copy 2.txt", "r") as file:
            all_tasks = file.readlines()

    with open("user copy.txt", "r") as file:
        all_users = file.readlines()
        
        print(f"Total number users is {len(all_users)}. Total number tasks is {len(all_tasks)}.")  

def generate_reports():

    print("Admin area")

    number_overdue = 0 
    number_not_overdue = 0
    total_not_complete = 0
    total_complete_task = 0

    with open("tasks copy 2.txt", "r") as f:

        all_tasks = []

        for lines in f: 
            temp = lines.strip().split(", ")
            all_tasks.append(temp)

    for task in all_tasks:
        total_number_task = len(all_tasks)
        
        if task[5] == "No":
            total_not_complete += 1

        else: 
            total_complete_task += 1

        percetage_incomplete = (total_not_complete / total_number_task) * 100
        strip_time_today = datetime.today()
        date_time_date = datetime.strptime(task[4], "%d %b %Y")

        if date_time_date < strip_time_today:
            number_overdue += 1
        
        else:
            number_not_overdue += 1
        
        percentage_overdue = (number_overdue / total_number_task) * 100
        percentage_not_overdue = (number_not_overdue / total_number_task) * 100
        
    with open ("task_overview.txt", "w") as file:

        file.write(f'''
Task total: {total_number_task}
Task complete: {total_complete_task}
Task not complete: {total_not_complete}
Percentage incomplete: {percetage_incomplete}
Overdue tasks: {number_overdue}
Percentage of tasks overdue: {percentage_overdue}
Percentage of tasks not overdue: {percentage_not_overdue}''')

    with open("user copy.txt", "r") as f:

        total_users = 0

        for lines in f:
                temp = lines.strip().split(", ")
                total_users += 1

    selected_user = input("Please insert name of selected user to see report")
    count_not_complete = 0
    count_complete = 0 
    count_users_tasks = 0
    count_overdue_not_complete = 0

    for task in all_tasks:

        if selected_user == task[0]:
            strip_time_today = datetime.today()
            date_time_date = datetime.strptime(task[4], "%d %b %Y")
            count_users_tasks += 1
            percentage_user_tasks = (count_users_tasks / total_number_task) * 100
            
            if task[5] == "No":
                count_not_complete += 1

            else: 
                count_complete += 1

            percentage_complete = (count_complete / count_users_tasks) * 100
            percentage_not_complete = (count_not_complete / count_users_tasks) * 100
            
            if task[5] == "No" and date_time_date < strip_time_today:

                count_overdue_not_complete += 1
            
        percentage_overdue_not_complete = (count_overdue_not_complete / count_users_tasks) * 100

        with open("user_overview.txt", "w") as file:
    
                file.write(f'''
    Report for: {selected_user}
    Total users: {total_users})
    Total tasks: {total_number_task}
    Total number of tasks assigned to selected user: {count_users_tasks}
    Percentage of total number of tasks assigned to selected user: {percentage_user_tasks}
    Percentage of selected users tasks that have been completed: {percentage_complete}
    Percentage of the tasks assigned to selected user that must still be completed: {percentage_not_complete}
    Percentage of the tasks that have been assinged to selected user that user that is overdue and not complete: {percentage_overdue_not_complete}''')

    print("Reports generated")

def add_task():
            
    with open("tasks copy 2.txt", "a+") as file:
        file.seek(0)
        for lines in file:
            
            users_name_task = input("please enter your username")
            task_title = input("enter title of your task")
            description_task = input("enter task description")
            due_date = input("enter the due date in format 15 Oct 2024")
            strptime_date = datetime.strptime(due_date, "%d %b %Y")
            todays_date = date.today().strftime("%d %b %Y")
            task_complete = "No"
            
            file.write(f"\n{users_name_task}, {task_title}, {description_task}, {strptime_date}, {todays_date}, {task_complete}")
                        
def view_all():
        
    with open("tasks copy 2.txt", "r") as file:
        for lines in file:
            temp = lines.strip().split(", ")
            
            print(f" Task: {temp[1]}")
            print(f" Assingned to: {temp[0]}")
            print(f" Date assigned: {temp[4]}")
            print(f" Due date: {temp[3]}")
            print(f" Task complete {temp[5]}")
            print(f" Task description: {temp[2]}")
            
def view_mine(users):
        
    current_task = [] 

    with open("tasks copy 2.txt", "r+") as file:
        
        for lines in file:
            temp = lines.strip().split(", ")

            if temp[0] == users:   

                current_task.append(temp)
    
    for i, task in enumerate(current_task, 1):

        print(f" Task number: {i} \n")
        print(f" Task: {task[1]}")
        print(f" Assingned to: {task[0]}")
        print(f" Date assigned: {task[4]}")
        print(f" Due date: {task[3]}")
        print(f" Task complete {task[5]}")
        print(f" Task description: {task[2]}\n")

    task_request =  input('''
\nEnter:
c for complete
e for edit
-1 for menu \n''')

    if task_request == "-1":
                main()

    elif task_request == "c":

        task_number = int(input("Enter a task number."))
        new_task = current_task[task_number - 1]

        new_task[5] = "yes"

        current_task [task_number - 1] = new_task

        with open("tasks copy 2.txt", "w") as file:

            for task in current_task:

                file.write(','.join(task) + "\n")

    elif task_request == "e" and task[5].lower() == "no":

        task_number = int(input("Enter a task number."))

        date_or_username = int(input("Enter 1 to change date or 2 to change assigned user"))

        new_task = current_task[task_number -1]

        if date_or_username == 1: 

            new_task[3] = input("Enter new due date" + "\n")
            current_task [task_number - 1] = new_task

            with open("tasks copy 2.txt", "w") as file:

                for task in current_task:

                    file.write(', '.join(task) + "\n")

            print("Date change succesful")

        elif date_or_username == 2:

            new_task[0] = input("Enter new user"+ "\n")
            current_task [task_number - 1] = new_task

            with open("tasks copy 2.txt", "w") as file:

                for task in current_task:

                    file.write(', '.join(task) + "\n")

            print("New user changed succesfully")

        else:

            print("invlaid input. Enter 1 or 2")

    else:
        
        print("invlaid entry. try again")

def exit():

    print('Goodbye!!!')
    exit()
    

def invalid():

    print("You have entered an invalid input. Please try again")   

def main():  
    
    current_user = login()

    while True:

        menu = input('''Select one of the following options:
r - register user
ds - display statistics
gr - generate reports
a - add task
va - view all
vm - view mine
e - exit \n''') 

        if menu == "r":
            print("Admin area")
            if authentic_admin():
                reg_user()
            
            else:
                print("admin credentials not entetred")
        
        elif menu == "ds":
            print("Admin area")
            if authentic_admin():
                display_statistics()

            else: 
                print("admin credentials not entetred")

        elif menu == "gr":
            print("Admin area")
            if authentic_admin():
                generate_reports()

            else: 
                print("admin credentials not entetred")
        
        elif menu == "a":
            add_task()
        
        elif menu == "va":
            view_all()

        elif menu == "vm":
            view_mine(current_user)
             
        elif menu == "e":
            exit()
            break

        else:
            invalid()
main()