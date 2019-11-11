import subprocess as sp
import pymysql
import pymysql.cursors

def fireAnEmployee():
    """
    Function to fire an employee
    """
    print("Not implemented")

def promoteEmployee():
    """
    Function performs one of three jobs
    1. Increases salary
    2. Makes employee a supervisor
    3. Makes employee a manager
    """
    print("Not implemented")


def employeeStatistics():
    """
    Function prints a report containing 
    the number of hours per week the employee works,
    hourly pay, projects employee works on and so on
    """
    print("Not implemented")


def addPerson(record):
    try:
        query = "INSERT INTO PERSON(SSN, First_name, Last_name, Year, Month, Day, Contact) VALUES('%d', '%s', '%s', '%d', '%d', '%d', '%d')" 
        record = tuple(record)
        print(query)
        cur.execute(query, record)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
        
    return

def addDriver():
    try:
        record = []
        print("Enter driver details:")
        record[0] = int(input('SSN: '))
        record[1:3] = input('Name: ').split(' ')
        record[3:6] = list(map(int, input('DOB (in yyyy-mm-dd format): ').split('-')))
        record[6] = int(input('Contact: '))
        addPerson(record)
        record[1:]=[]
        record[1] = input('License Number: ')
        record[2] = True;
        query = "INSERT INTO DRIVER(SSN, Availability, License_number) VALUES('%d', '%b', '%s')" 
        record = tuple(record)
        print(query)
        cur.execute(query, record)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
        
    return

def removePerson():
    try:
        ssn = int(input('SSN:'))
        query = "DELETE * FROM PERSON WHERE SSN = %s"  % (ssn)
        print(query)
        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
        
    return

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch==1): 
        hireAnEmployee()
    elif(ch==2):
        fireAnEmployee()
    elif(ch==3):
        promoteEmployee()
    elif(ch==4):
        employeeStatistics()
    else:
        print("Error: Invalid Option")

# Global
while(1):
    tmp = sp.call('clear',shell=True)
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='COMPANY',
                cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear',shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
        tmp = input("Enter any key to CONTINUE>")

        with con:
            cur = con.cursor()
            while(1):
                tmp = sp.call('clear',shell=True)
                print("1. Hire a new driver")
                print("2. Fire a driver")
                print("3. Update contact")
                print("4. Add a cab")
                print("5. Remove a cab")
                print("6. Update color of a cab")
                print("7. Add car model")
                print("8. Remove car model")
                print("9. Add shift")
                print("10. Remove shift")
                print("11. Assign driver a shift")
                print("12. Remove driver from a shift")
                print("13. Add cab to a shift")
                print("14. Remove cab from a shift")
                print("15. Add a rider")
                print("16. Request a ride")
                print("17. Enter details of an accident")
                print("18. Change ride status")
                print("19. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear',shell=True)
                if ch==20:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")


    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
    
   


