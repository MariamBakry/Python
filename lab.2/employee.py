from DBHandler import DBHandler
from config import db_config

db =DBHandler(db_config).connect()
class Employee:
   employees=[]  

   # --------------init and add employee------------------------
   def __init__(self, first_name,last_name,age,department,salary):
      self.first_name=first_name
      self.last_name =last_name
      self.age=age
      self.department=department
      self.salary=salary  
      Employee.employees.append(self)
      db.insert(
         f"insert into `employee` (`first_name`,`last_name`,`age`,`department`,`salary`) VALUES (%s, %s, %s, %s, %s)",
         (self.first_name, self.last_name,
         self.age, self.department, self.salary)
      ) 
      print("employee added")
      print("=============================")
   

   # --------------transfer employee------------------------
   def transfer(first_name, last_name, new_department):
      db.update(f"update `employee` set department =%s where first_name= %s and last_name = %s",(new_department, first_name, last_name))
      print("employee transferred")
      print("=============================")


   # --------------fire employee------------------------
   def fire(first_name, last_name):
      db.remove(f"delete from `employee` where first_name= %s and last_name = %s",
      (first_name, last_name))
      print("employee fired")
      print("=============================")
         

   # --------------show employee------------------------
   def show(self):
      print(f"first name is {self.first_name}")
      print(f"last name is {self.last_name}")
      print(f"age is {self.age}")
      print(f"department is {self.department}")
      print(f"salary is {self.salary}")
      print("=============================")


   # --------------list employees with null managed_department---------------------
   @staticmethod
   def list_employees():
      employees = db.fetch_all(
         query=f"select * from `employee` where `managed_department` is Null"
      )
      if(employees):
         for emp in employees:
            print(f"first name is {emp[0]}")
            print(f"last name is {emp[1]}")
            print(f"age is {emp[2]}")
            print(f"department is {emp[3]}")
            print(f"salary is {emp[4]}")
            print("=============================")
      else: 
         print("there is no employees")
         print("=============================")
















   






