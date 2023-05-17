
from employee import Employee
from manager import Manager

while True:
    # ----------------------the list of choices------------------- 
    action= input(""" welcome to our company
            to add employee type 'add'
            to show all employees 'show_all'
            to fire an employee 'fire'
            to transfer an employee 'transfer'
            to exit press q
            """)
    

    # ----------------------add employee---------------------
    if action=='add':
        manager=input("If you are manager press “m” || if you are employee press ‘e’")
        if manager=="m":
            first_name=input('please enter the first name: ')
            last_name=input('please enter the last name: ')
            age=int(input('please enter the age: '))
            department=input('please enter the department: ')
            salary=int(input('please enter the salary: '))
            managed_department = input('please enter the managed_department: ')
            if(len(managed_department) == 0): managed_department = None
            e=Manager(first_name,last_name,age,department,salary, managed_department)
        else:
            print("you can not add employee")
            print("=============================")


    # ----------------------show all employees---------------------  
    if action=='show_all':
        manager=input("If you are manager press “m” || if you are employee press ‘e’")
        if manager=="m":
            Manager.list_employees()
        else:
            Employee.list_employees()
        

    # ----------------------quit---------------------
    if action=='q':
        break
    

    # ----------------------fire employee---------------------
    if action=='fire':
        manager=input("If you are manager press “m” || if you are employee press ‘e’")
        if manager=="m":
            first_name=input('please enter the first name: ')
            last_name=input('please enter the last name: ')
            Employee.fire(first_name, last_name)
        else:
            print("you can not fire employee")
            print("=============================")


    # ----------------------transfer employee---------------------
    if action=='transfer':
        manager=input("If you are manager press “m” || if you are employee press ‘e’")
        if manager=="m":
            first_name=input('please enter the first name: ')
            last_name=input('please enter the last name: ')
            new_department=input('please enter the department: ')
            Employee.transfer(first_name, last_name, new_department)
        else:
            print("you can not transfer employee")