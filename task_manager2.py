'''
Compulsory task.
This program will allow the admin to view stats from all the users and add new users and check if there is users
that has been added. It will check whether a task has been completed and allow the admin to mark or edit tasks.
'''
# Import datetime to use the current date in the program.
from datetime import datetime

# Defining my own function to recall later in the program.
def reg_user():

        # Use while loop to get info from the admin.
        while True:

                # Ask admin to enter the new username and password as well as to confirm password.               
                username = input("Enter new username here:\n")
                password = input("Enter password here:\n")
                password_check = input("Enter password again to confirm:\n")

                # Using isvaliduser as a flag.
                isvaliduser = True

                # Open and close the text file to read from it.
                with open("user.txt", "r") as users:

                        # Use for loop to iterate over each user entered.
                        for user in users:

                                # Split the username from the password at the comma and space.
                                get_user = user.split(", ")

                                # Get the username at index 0
                                new_user = get_user[0]

                                # Checking if the username entered already exists.
                                if username == new_user:

                                        # Will print if username already exists and then ask to enter a new username.
                                        print("Error! This user already exists, please enter a new user.")

                                        # If the isvaliduser is equal to false then the while loop will break.
                                        isvaliduser = False
                                        break

                                # Checking if the password is correct.
                                elif password != password_check:
                                        print("passwords dont match")

                                        # If the isvaliduser is equals to false then it will exit the while loop.
                                        isvaliduser = False
                                        break

                # If isvaliduser is true then it will update the text file.               
                if isvaliduser:
                        with open("user.txt", "a") as users:

                                # Write the new username and password into the user.txt file.
                                users.write(f"\n" + username + ", " + password)
                                break


# Defining my own function to recall later in the program.
def add_task():

        # Will ask the user to enter the username of the person whom they want to assign the task.
        username_person = input("Enter the username of the person whom the task will be assigned to:\n")

        # Ask user to enter the title and description of the task.
        task_title = input("Enter the title of the task here:\n")

        task_description = input("Add a description of the task here:\n")

        # Will ask user to enter the due date and the current date.
        due_date = input("Enter the due date here:\n")

        curr_date = datetime.today().strftime("%d %b %Y")

        # Open and close tasks.txt file to append extra info into the file.
        with open("tasks.txt", "a") as task_add:

                # This info will be appended to the tasks.txt file.
                task_add.write(f"\n" + username_person + ", " + task_title + ", " + task_description + ", " +
                curr_date + ", " + due_date + ", " + "No")


# Defining my own function to recall later in the program.
def view_all():

        # Open to read from tasks.txt and close the file.        
        with open("tasks.txt", "r") as task_add:

                # Use for loop to access each line in the text file.
                for lines in task_add:

                        # Making a string by splitting from the comma and space.
                        lines = lines.split(", ")

                        # Printing the outcome and use indexing to access different characters of the string.
                        print(f"""Task:\t {lines[1]}
Assigned to:\t{lines[0]}
Date assigned:\t{lines[3]}
Due date:\t{lines[4]}
Task complete?\t{lines[5]}
Task description:
{lines[2]}""")


# Defining my own function to recall later in the program.
def view_mine():

        # Use a counter to count all the tasks that has been added.
        counter = 1

        # Use an empty dictionary to add to.
        task_dict = {}

        # Open and close the text file after reading from it and give it a variable.
        with open("tasks.txt", "r") as task_add:

                # Use for loop to access each line in the text file.
                for lines1 in task_add:

                        # Split the string where there is a comma and space to isolate characters and removing the new line character.
                        lines1 = lines1.strip("\n").split(", ")

                        # Add all the tasks with their number as key to the dictionary.
                        task_dict[counter] = lines1
                        
                        # Use if statement to check if the user that is logged in is the same as the lines that is being read.
                        if validation == lines1[0]:

                                # If the user is the same then the program will print out all the user's tasks.
                                print(f"""Task Number:\t{counter}
Task:\t{lines1[1]}
Assigned to:\t{lines1[0]}
Date assigned:\t{lines1[3]}
Due date:\t{lines1[4]}
Task complete?\t{lines1[5]}
Task description:
{lines1[2]}\n""")         

                        # The counter will add 1 task to the total.        
                        counter += 1

        # Ask admin to enter the number of the task that they want to change. Change the input to int to access the dictionary.
        task_selection = int(input("Enter the number of the task that you would like to access here:\n"))

        # Ask admin if they want to mark or edit the task.
        menu2 = input("Enter 'm' if you want to mark the task as complete or 'e' if you want to edit the task:\n").lower()

        # Use if statements to help with decisions. If admin select "m" then they can mark the task from No to Yes.
        if menu2 == "m":

                # Accessing the index where the character "No" is stored and change it.
                task_dict[task_selection][-1] = "Yes"

        # If the task has not been edited then this statement will be allowed and allow the to edit the task.
        elif menu2 == "e" and task_dict[task_selection][-1] == "No":

                # Ask admin what they want to edit in the task.
                change = input("Enter 'user' if you want to change the username or 'date' if you want to change the due date:\n").lower()

                # Use nested if statement. This statement will execute when admin enters "user".
                if change == "user":

                        # Ask the admin to enter the name to whom they want to assign the task to.
                        new_name = input("Enter the name of the person here to assign the task to:\n").capitalize()

                        # This will change the name in the task to the name the admin entered.
                        task_dict[task_selection][0] = new_name

                # This statement will execute when admin enters "date".
                elif change == "date":

                        # Ask user to enter the new due date.
                        new_date = input("Enter the new due date here:\n")

                        # This will change the original due date to the due date that the admin has entered.
                        task_dict[task_selection][-2] = new_date

        # This will be executed when the task has been completed.               
        else:
                print("You cannot edit a task that has been completed!")
        
        task_dict2 = ""
        for values in task_dict.values():
                task_dict2 += ", ".join(values) + "\n"
        
        with open("tasks.txt", "w") as task_add:
                task_add.write(task_dict2)


# Defining my own function to use later in the program.
def gen_reports():

        # Open and close the text file and read from it.
        with open("tasks.txt", "r") as task_add:

                # Create 4 variables to start a count from.
                gen_tasks = 0
                complete_tasks = 0
                uncomplete_tasks = 0
                overdue_uncomp_tasks = 0

                # Use for loop to access all the tasks.
                for line in task_add:

                        # Split where there is a comma and space to access characters easier.
                        line = line.split(", ")

                        # Use if statements to check the last index is completed or not and add it to the variable. Strip new line character.
                        if line[-1].strip("\n") == "Yes":
                                complete_tasks += 1

                        # Strip new line character and check if task is completed or not and add to the variable.
                        elif line[-1].strip("\n") == "No":
                                uncomplete_tasks += 1

                        # Get the current date. Convert to datetime object.
                        curr_date = datetime.today()

                        # Convert the due date into a datetime object.
                        due_date = datetime.strptime(line[-2], "%d %b %Y")

                        # Checking whether the task is overdue or not.
                        if curr_date > due_date:
                                overdue_uncomp_tasks +=1

                        # Each line that the for loop accesses will be added to the variable because each task is on a new line.
                        gen_tasks += 1

                # Calculating the percentage of all the uncomplete tasks.
                uncom_percentage = (uncomplete_tasks / gen_tasks) * 100

                # Storing the total of overdue tasks in a new variable.
                overdue_percentage = overdue_uncomp_tasks

                # Calculating the percentage of all the overdue tasks.
                overdue_task_percentage = (overdue_percentage / gen_tasks) * 100

        # Open and closing the text file to write into.
        with open("task_overview.txt", "w") as write_file:

                # Store the format in a new variable.
                statement = f"Total Tasks Generated : {gen_tasks}\n"\
                            f"Total Completed Tasks : {complete_tasks}\n"\
                            f"Total Uncompleted Tasks : {uncomplete_tasks}\n"\
                            f"Total Overdue Uncompleted Tasks : {overdue_uncomp_tasks}\n"\
                            f"Percentage Of Incomplete Tasks : {uncom_percentage} %\n"\
                            f"Percentage Of Overdue Tasks : {overdue_task_percentage} %"

                # Write the format that is user friendly to read into the file.
                write_file.write(statement)

        # Open and closing the text file to read from it.
        with open("user.txt", "r") as users:

                # Open and close the text file to write into it.
                with open("user_overview.txt", "w") as user_file:

                        # Use for loop to iterate over every username in the text file.
                        for user in users:

                                # Store the name only in a new variable name.
                                username = user.split(", ")[0]

                                # Start a counter from zero to add into the varaible to save the stats in.
                                tasks_total_assign = 0
                                tasks_assigned = 0
                                tasks_user_comp = 0
                                tasks_user_uncomp = 0
                                ovrdue_uncomp = 0
                                
                                # Split the list at a comma and space to access the names only.
                                user_list = user.split(", ")

                                # Open and close file to read from it.
                                with open("tasks.txt", "r") as task_add:

                                        # Use for loop to access all the tasks in the text fiel.
                                        for tasks in task_add:

                                                # Starting the counter at one and every time the for loop encounters a new line it will add 1 to the variable.
                                                tasks_total_assign += 1

                                                # Splitting at a comma and space to access all the names.
                                                user_names = tasks.split(", ")

                                                # Use if statement to check if the username is the same as the name that a task has been assigned to.
                                                if user_names[0] == user_list[0]:

                                                        # This will add the task to the username.
                                                        tasks_assigned += 1

                                                        # Converting the current date and due date to datetime object.
                                                        current_date = datetime.today()
                                                        task_duedate = datetime.strptime(user_names[-2], "%d %b %Y")

                                                        # Use if statements to check if the task is complete. If the task is complete it will add 1.
                                                        if user_names[-1].strip("\n") == "Yes":
                                                                tasks_user_comp += 1

                                                        # Check if the task is incomplete and if the statement is incomplete it will add 1.
                                                        if user_names[-1].strip("\n") == "No":
                                                                tasks_user_uncomp +=1

                                                        # Checking id the task is incomplete and overdue and it will add 1.
                                                        if user_names[-1].strip("\n") == "No" and current_date > task_duedate:
                                                             ovrdue_uncomp += 1

                                # If the task assigned to a user is equals to zero, the stats will be zero.
                                if tasks_assigned == 0:
                                        perc_tasks_assigned = 0
                                        perc_tasks_user_comp = 0
                                        perc_tasks_user_uncomp = 0
                                        perc_ovrdue_uncomp = 0

                                # If the task assigned has a value then the program will work out percentages.
                                else:
                                        # Calculate the percentages of tasks assigned to that user.
                                        perc_tasks_assigned = (tasks_assigned / tasks_total_assign) * 100

                                        # Calculate the percentage of tasks that has been completed.
                                        perc_tasks_user_comp = (tasks_user_comp / tasks_assigned) * 100

                                        # Calculate the percentage of tasks that is incomplete.
                                        perc_tasks_user_uncomp = (tasks_user_uncomp / tasks_assigned) * 100

                                        # Calculate the percentage of tasks that is overdue and incomplete.
                                        perc_ovrdue_uncomp = (ovrdue_uncomp / tasks_assigned) * 100

                                # Saving the format in a new varaible name to write into the file.                        
                                statement2 = f"\t\tUser {username}\nThe total tasks assigned to the user is : {tasks_assigned}\n"\
                                        f"The percentage of the total number of tasks assigned to the user is : {perc_tasks_assigned}%\n"\
                                        f"The percentage of the tasks completed is : {perc_tasks_user_comp}%\n"\
                                        f"The percentage of the tasks that is uncompleted is : {perc_tasks_user_uncomp}%\n"\
                                        f"The percentage of tasks that is uncompleted and overdue : {perc_ovrdue_uncomp}%\n\n"

                                # Writing into the file.
                                user_file.write(statement2)


# This code will check whether the person can login or not by using a while loop. It will read the data from
# user.txt file and store the information in a dictionary.
# Creating an empty dictionary.
user_names = {}

# Open and close user.txt file to read from and giving it a variable name.
with open("user.txt", "r") as users:

        # Use for loop to access each name and password in the user.txt file.
    for user in users:

        # Giving the username and password new variables and creating a list.
        usr, pswd = user.split(", ")

        # Adding the username and password into the dictionary and stripping the new line character.
        user_names[usr] = pswd.strip("\n")

# This will allow the program to ask for login details.
# validation = None

# Use while loop to ask and validate the username and password entered.
while True:
    validation = input("Enter username here:\n")

    pswd_validation = input("Enter password here:\n")

        # Checking whether the name and password entered are from the dictionary. Then break the while loop.
    if pswd_validation == user_names[validation] and validation in user_names.keys():
        break

# Use while loop to present the menu to the user. Input will be lower case.
while True:

        # Use if statement to seperate "admin" from normal users.
        if validation == "admin":

                # This will show the menu to the admin.
                menu = input("""Select one of the following options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my tasks
vs - View statistics
gr - Generate reports
e - Exit
: """).lower()

        # This statement will execute if it is not "admin"
        else:

                # This will print the menu that the user will be able to see.
                menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

        # Use elif statements to help with decision making in the program.
        # This statement will be executed if the user chooses the option "r".
        if menu == "r":
                reg_user()

        # This statement will be executed if the user or admin chooses the option "a".      
        elif menu == "a":
                add_task()

        # This statement will be executed if the user or admin chooses the option "va".
        elif menu == 'va':
                view_all()

        # This statement will be executed if the user or admin chooses the option "vm".
        elif menu == 'vm':
                view_mine()

        # This statement will execute when the admin chooses option "vs".
        elif menu == 'vs':

                # Open and close the text file after reading from it. Store the total lines in a variable as it is equals to the
                # amount of users. 
                with open("user.txt", "r") as users:
                        tot_users = len(users.readlines())

                # Open and close the text file after reading from it. Store the total lines in a variable as it is equals to the
                # amount of tasks.                
                with open("tasks.txt", "r") as task_add:
                        tot_tasks = len(task_add.readlines())

                        # Will print the results in a user friendly manner.
                        print(f"""Total users:\t{tot_users}
Total tasks:\t{tot_tasks}""")

                # Open and close the text file to read from it and display it to the console in a user friendly manner.
                with open("user_overview.txt", "r") as user_file:
                        print(user_file.read())

                # Open and close the file to read from it and display it to the console in a user friendly manner.
                with open("task_overview", "r") as task_file:
                        print(user_file.read())

        # This statement will execute when the admin chooses "gr".
        elif menu == "gr":
                gen_reports()

        # This statement will execute if the user wants to exit. Will display a message as well.
        elif menu == 'e':
                print('Goodbye!!!')
                exit()

        # This statement will execute when the user enters an invalid choice.
        else:
                print("You have made a wrong choice, Please Try again")