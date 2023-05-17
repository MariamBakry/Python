from employee import Employee
from manager import Manager

while True:
    action= input(""" welcome to our company
            to add employee type 'add'
            to show all employees 'show_all'
            to exit press q
            """)
    if action=='add':
        manager=input("If you are manager press “m” || if you are employee press ‘e’")
        if manager=="m":
            first_name=input('please enter the first name: ')
            last_name=input('please enter the last name: ')
            age=int(input('please enter the age: '))
            department=input('please enter the department: ')
            salary=int(input('please enter the salary: '))
            e=Employee(first_name,last_name,age,department,salary)
        else:
            print("you can not add employee")

            
    if action=='show_all':
        Employee.list_employees()
    
    if action=='q':
        break