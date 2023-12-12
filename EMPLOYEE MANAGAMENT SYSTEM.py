from os import system
import re
import mysql.connector



con = mysql.connector.connect(host="localhost", user="root", password="", database="employee" )


#make a regular expression for validating an email 
regax = r'\b[A-Za-z0-8,_%+-]+@[A-za-z0-9,-]+\,[A-Z|a-z]{2,}\b'
#for validating a phone number 
pattern = re.compile(r"^(0|91)?[7-9][0-9]{9}$")

#Function to Add_Employ
def Add_Employ():
    global Name
    print("{:>60}".format(">>>> Add Employee Record <<<<"))
    Id = input("Enter Employee Id: ")
    #checking if employee Id is exist or not
    if (check_employee(Id) == True):
        print("Employee Id Already Exist\nTry Again...")
        press = input("Press Any Key to Continue...")
        Add_Employ()
    Name = input("Enter Employee Name: ")
    #checking if employee name is exist or not
    if (check_employee_name(Name) == True):
        print("Employee Name Already Exist\nTry Again...")
        press = input("Press Any Key to Continue...")
        Add_Employ()
    Email_Id = input("Enter Employee Email Id: ")
    if(re.fullmatch(regax, Email_Id)):
        print("Valid Email")
    else:
        print("Invalid Email")
        press = input("Press Any Key to Continue...")
        Add_Employ
    Phone_no = input("Enter Employee Phone No.: ")
    if(pattern.match(Phone_no)):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
        press = input("Press Any Key to Continue...")
        Add_Employ()
    
    Address = input("Enter Employee Address: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")
    data = (Id, Name, Email_Id, Phone_no, Address, Post, Salary)
    #Inserting Employee Details in the employee (empdata) table
    sql = 'insert into empdata values(%s,%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    
    #Executing the sql query
    c.execute(sql, data)
    
    #commit() method to make changes in the table
    con.commit()
    print("Successfully Added Employee Record")
    press = input("Press Any Key to Continue...")
    menu()
    
  #Function to check if Employee with given name if it is exists or not
  
def check_employee_name(employee_name):
      #query to select all rows from employee (empdata) table
      sql = 'select * from empdata where Name=%s'
      
      #making cursor buffered to make rowcount method work properly
      c = con.cursor(buffered=True)
      data = (employee_name,)
      
      #Execute the sql query
      c.execute(sql, data)
      
      #row method to find number of rows with given values 
      r = c.rowcount
      if r == 1:
          return True
      else:
          return False
           
     #Function to check if Employee with given ID if it is exists or not
def check_employee(employee_Id):
      #query to select all rows from employee (empdata) table
      sql = 'select * from empdata where Id=%s'
      
      #making cursor buffered to make rowcount method work properly
      c = con.cursor(buffered=True)
      data = (employee_Id,)
      
      #Execute the sql query
      c.execute(sql, data)
      
      #row method to find number of rows with given values 
      r = c.rowcount
      if r == 1:
          return True
      else:
          return False
      
      
    #function to display_employ
def Display_Employ():
    print("{:>60}".format("-->> Display Employee Record <<--"))
    #query to see all rows from Employee (empdata) table
    sql = 'select * from empdata'
    c = con.cursor()
    
    #executing the sql query
    c.execute(sql)
    
    #fetching all details of all employees
    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Email Id: ", i[2])
        print("Employee Phone No.: ", i[3])
        print("Employee Address: ", i[4])
        print("Employee Post: ", i[5])
        print("Employee Salary: ", i[6])
        print("\n")
    press = input("Press Any Key to Continue...")
    menu()
    
    #function for update_employ
def Update_Employ():
    print("{:>60}".format(">>>> Update Employee Record <<<<"))
    Id = input("Enter Employee Id: ")
    #checking if employee name is exist or not
    if (check_employee(Id) == False):
        print("Employee Id Already Exist\nTry Again...")
        press = input("Press Any Key to Continue...")
        menu()
    else:
       Email_Id = input("Enter Employee Email Id: ")
    if(re.fullmatch(regax, Email_Id)):
        print("Valid Email")
    else:
        print("Invalid Email")
        press = input("Press Any Key to Continue...")
        Update_Employ()
    Phone_no = input("Enter Employee Phone No.: ")
    if(pattern.match(Phone_no)):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
        press = input("Press Any Key to Continue...")
        Update_Employ()
    Address = input("Enter Employee Address: ")
    
       #updating employee details in the empdata table
    sql = 'UPDATE empdata set Email_Id = %s, Phone_no = %s, Address = %s where Id = %s'
    data = (Email_Id, Phone_no, Address, Id)
    c = con.cursor()
       
       #Executing the sql query
    c.execute(sql, data)
       
       #commit() method to make changes in the table
    con.commit()
    print("Updated Employee Record")
    press = input("Press Any Key to Continue...")
    menu()
     
     #Function for promote_employ
def Promote_Employ():
    print("{:>60}".format(">>>> Promote Employee Record <<<<"))
    Id = input("Enter Employee Id: ")
    #checking if employee name is exist or not
    if (check_employee(Id) == False):
        print("Employee Already Exist\nTry Again...")
        press = input("Press Any Key to Continue...")
        menu()
    else:
        Amount = int(input("Enter Increase Salary: "))
        #query to fetch salary of employee with given data
        sql = 'select Salary from empdata where Id=%s'
        data = (Id,)
        c = con.cursor()
        
        #executing the sql query
        c.execute(sql, data)
        
        #fetching salary of employee with given Id
        r = c.fetchone()
        t = r[0]+Amount
        
        #query to update salary of employee with given Id
        sql = 'update empdata set Salary = %s where Id = %s'
        d = (t, Id)
        
    #executing the salary
    c.execute(sql, d)
    
    #commit() method to make changes in the table
    con.commit()
    print("Employee Promoted")
    press = input("Press Any Key to Continue...")
    menu()
    
    #function for remove_employ
def Remove_Employ():
    print("{:>60}".format(">>>> Remove Employee Record <<<<"))
    Id = input("Enter Employee Id: ")
    #checking if employee name is exist or not
    if (check_employee(Id) == False):
        print("Employee Already Exist\nTry Again...")
        press = input("Press Any Key to Continue...")
        menu()
    else:
        #query to delete employee from empdata table
        sql = 'delete from empdata where Id = %s'
        data = (Id,)
        c = con.cursor()
        
    #executing the sql query 
    c.execute(sql, data)
    
    #commit () method to make changes in the empdata table
    con.commit()
    print("Employe Removed")
    press = input("Press Any Key to Continue")
    menu()

#function for search_employ
def Search_Employ():
    print("{:>60}".format(">>>> Search Employee Record <<<<"))
    Id = input("Enter Employee Id: ")
    #checking if employee name is exist or not
    if (check_employee(Id) == False):
        print("Employee Already Exist\nTry Again...")
        press = input("Press Any Key to Continue...")
        menu()
    else:
       #query to search employee from empdata table
       sql = 'select * from empdata where Id = %s'
       data = (Id,)
       c =con.cursor()
       
       #executing the sql query
       c.execute(sql, data)
       
       #fetching all details of all the employee
       r = c.fetchall()
       for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Email Id: ", i[2])
        print("Employee Phone No.: ", i[3])
        print("Employee Address: ", i[4])
        print("Employee Post: ", i[5])
        print("Employee Salary: ", i[6])
        print("\n")
    press = input("Press Any Key to Continue...")
    menu()
         
    
    
#menu function to display menu
def menu():
    system("cls")
    print("{:>60}".format("************************************"))
    print("{:>60}".format(">>>> EMPLOYEE MANAGEMENT SYSTEM <<<<"))
    print("{:>60}".format("************************************"))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Exit\n")
    print("{:>60}".format("-->> Choice Options: [1/2/3/4/5/6/7] <<--"))
      
    ch = int(input("Enter your choice: "))
    if ch == 1:
        system("cls")
        Add_Employ()
    elif ch == 2:
        system("cls")
        Display_Employ()
    elif ch == 3:
        system("cls")
        Update_Employ()
    elif ch == 4:
        system("cls")
        Promote_Employ()
    elif ch == 5:
        system("cls")
        Remove_Employ()
    elif ch == 6:
        system("cls")
        Search_Employ()
    elif ch == 7:
        system("cls")
        print("{:>60}".format("Have a Nice Day! :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any Key to Continue...")
menu()