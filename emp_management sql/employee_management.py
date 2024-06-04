import mysql.connector
from os import system
import pandas as pd

con=mysql.connector.connect(host="localhost", user="root", password=" ", database="employee")
mycursor=con.cursor()



def Display_Employee():
    print("\n"," "*20,'Displaying Employee Records')
    print("*"*80)
    print()
    sql = 'select * from empdata'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    df=pd.DataFrame(r,columns=["Employee Id", "Employee Name", "Employee Email Id", "Employee Phone No", "Employee Address", "Employee Salary"])
    print(df)
    press = input("Press Any key To Continue..")
    menu()



def Add_Employee():
    print("\n"," "*20,'Adding a New Employee')
    print("*"*80)
    print()
    Id = input("Enter Employee Id: ")
    Name = input("Enter Employee Name: ")
    Email_Id = input("Enter Employee Email ID: ")
    Phone_no = input("Enter Employee Phone No.: ")
    Address = input("Enter Employee Address: ")
    Salary = input("Enter Employee Salary: ")
    data = (Id, Name, Email_Id, Phone_no, Address, Salary)
    sql = 'INSERT INTO empdata VALUES(%s,%s,%s,%s,%s,%s);'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Successfully Added Employee Record")
    press = input("Press Any Key To Continue..")
    menu()



def Update_Employee():
    print("\n"," "*20,'UPDATING AN EMPLOYEE RECORD')
    print("*"*80)
    print()
    Id = input("Enter Employee Id: ")
    # Checking If Employee Id is Exists Or Not
    if(check_employee(Id) == True):
        print("Choose information to be updated")
        print("a.Email \t b.Phone No. \t c.Address \t d.Salary")
        ch = input("Enter your Choice: ")
        if ch == 'a':
            system("cls")
            Email_Id = input("Enter Employee Email ID: ")
            sql = 'UPDATE empdata SET Email_Id = %s WHERE Id = %s'
            c = con.cursor()
            c.execute(sql, (Email_Id,Id))
            con.commit()
            print("Updated Employee Record")
            press = input("Press Any Key To Continue..")
            menu()
        elif ch == 'b':
            system("cls")
            Phone_no = input("Enter new phone no.: ")
            sql = 'UPDATE empdata SET Phone_no = %s WHERE Id = %s'
            c = con.cursor()
            c.execute(sql, (Phone_no,Id))
            con.commit()
            print("Updated Employee Record")
            press = input("Press Any Key To Continue..")
            menu()
        elif ch == 'c':
            system("cls")
            Address = input("Enter new Address: ")
            sql = 'UPDATE empdata SET Address=%s WHERE Id = %s'
            c = con.cursor()
            c.execute(sql, (Address,Id))
            con.commit()
            print("Updated Employee Record")
            press = input("Press Any Key To Continue..")
            menu()
        elif ch == 'd':
            system("cls")
            Salary = input("Enter updated Salary: ")
            sql = 'UPDATE empdata SET Salary=%s WHERE Id = %s'
            c = con.cursor()
            c.execute(sql, (Salary,Id))
            con.commit()
            print("Updated Employee Record")
            press = input("Press Any Key To Continue..")
            menu()
        else:
            print("Invalid Choice!")
            press = input("Press Any key To Continue..")
            menu()
    else:
        print("Employee Record Does Not Exist\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
        


def Promote_Employee():
    print("\n"," "*20,'PROMOTING AN EMPLOYEE')
    print("*"*80)
    print()
    Id = input("Enter Employee Id: ")
    # Checking If Employee Id is Exists Or Not
    if(check_employee(Id) == False):
        print("Employee Record Not Found\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Amount  = int(input("Enter Incremented Salary Amount: "))
        #query to fetch salary of Employee with given data
        sql = 'SELECT Salary FROM empdata WHERE Id=%s;'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchone()
        t = r[0]+Amount
        sql = 'UPDATE empdata SET Salary = %s WHERE Id = %s;'
        d = (t, Id)
        c.execute(sql, d)
        con.commit()
        print("Employee Promoted")
        press = input("Press Any key To Continue..")
        menu()

        

def Remove_Employee():
    print("\n"," "*20,'REMOVING AN EMPLOYEE')
    print("*"*80)
    print()
    Id = input("Enter Employee Id: ")
    # checking If Employee Id Exists Or Not
    if(check_employee(Id) == False):
        print("Employee Record Not Found\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        sql = 'DELETE FROM empdata WHERE Id = %s;'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Employee Removed")
        press = input("Press Any key To Continue..")
        menu()



def Search_Employee():
    print("\n"," "*20,'SEARCHING FOR AN EMPLOYEE')
    print("*"*80)
    print()
    Id = input("Enter Employee Id: ")
    # Checking If Employee Id Exists Or Not
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        sql = 'SELECT * FROM empdata WHERE Id = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Email Id: ", i[2])
            print("Employee Phone No.: ", i[3])
            print("Employee Address: ", i[4])
            print("Employee Salary: ", i[5])
            print("\n")
        press = input("Press Any key To Continue..")
        menu()

        
def Top_5():
    sql = 'SELECT * FROM empdata order by Salary DESC LIMIT 5;'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Email Id: ", i[2])
        print("Employee Phone No.: ", i[3])
        print("Employee Address: ", i[4])
        print("Employee Salary: ", i[5])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()



def Sorted_list():
    sql = 'SELECT Id,Name FROM empdata order by Name;'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    df=pd.DataFrame(r,columns=["Id", "Emp_Name"])
    print(df)
    press = input("Press Any key To Continue..")
    menu()



def Salaries_dist():
    sql = 'SELECT DISTINCT Salary FROM empdata;'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    df=pd.DataFrame(r,columns=["Distinct Salaries"])
    print(df)
    press = input("Press Any key To Continue..")
    menu()
    

    
def check_employee(employee_id):
    sql = 'SELECT * FROM empdata WHERE Id=%s;'
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


    
def menu():
    system("cls")
    print("\n"," "*25,'EMPLOYEE MANAGEMENT SYSTEM')
    print("*"*80)
    print()
    print("1. Display Employee Record")
    print("2. Add Employee Record")
    print("3. Update Employee Record")
    print("4. Remove Employee Record")
    print("5. Promote Employee Record")
    print("6. Search Employee Record")
    print("7. Show the Top 5 Highest Paid Employee")
    print("8. Show the Employee Names Alphabetically")
    print("9. Show Distinct Salaries")
    print("10. Exit\n")

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        Display_Employee()
    elif ch == 2:
        system("cls")
        Add_Employee()
    elif ch == 3:
        system("cls")
        Update_Employee()
    elif ch == 4:
        system("cls")
        Remove_Employee()
    elif ch == 5:
        system("cls")
        Promote_Employee()
    elif ch == 6:
        system("cls")
        Search_Employee()
    elif ch == 7:
        system("cls")
        Top_5()
    elif ch == 8:
        system("cls")
        Sorted_list()
    elif ch == 9:
        system("cls")
        Salaries_dist()
    elif ch == 10:
        system("cls")
        print("*"*80)
        print(" "*30,"THANK YOU!")
        print("*"*80)
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        menu()
        
#CALLING THE MAIN MENU FUNCTION
menu()
