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
        query = "INSERT INTO PERSON(SSN, First_name, Last_name, Year, Month, Day, Contact) VALUES(%s, %s, %s, %s, %s, %s, %s)" 
        record = tuple(record)
        # print(query)
        cur.execute(query, record)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database in addperson")
        print (">>>>>>>>>>>>>", e)
        
    return

def addDriver():
    try:
        record = [0]*7  
        print("Enter driver details:")
        record[0] = input('SSN: ')
        record[1:3] = input('Name: ').split(' ')
        dob = input('DOB: ').split('-')
        record[3] = int(dob[0])
        record[4] = int(dob[1])
        record[5] = int(dob[2])
        record[6] = int(input('Contact: '))
        print(record)
        addPerson(record)
        record[1:]=[0, 0]
        record[1] = input('License Number: ')
        record[2] = True;
        query = "INSERT INTO DRIVER(SSN, License_number, Availability) VALUES(%s, %s, %s)" 
        record = tuple(record)
        print(record)
        cur.execute(query, record)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database add driv")
        print (">>>>>>>>>>>>>", e)
        
    return

def removePerson():
    try:
        ssn = input('SSN:')
        print(type(ssn))
        query1 = "SELECT * FROM DRIVER WHERE SSN = %s" %(ssn)
        row = cur.execute(query1)
        if(row == 1):
            query = "DELETE FROM PERSON WHERE SSN = %s"  % (ssn)
            print(query)
            cur.execute(query)
            con.commit()
        else:
            print('The driver does not exist in the database')

    except Exception as e:
        con.rollback()
        print("Failed to insert into database remo")
        print (">>>>>>>>>>>>>", e)
        
    return

#4
def addCab():
    try:
        record = []
        print("Enter cab details:")
        record[0] = int(input('VRN: '))
        record[1] = int(input('Manufacture Year: '))
        record[2] = true
        record[3] = int(input('Model Id: '))
        query = "INSERT INTO Cab(VRN, Manufacture_Year, Availability, Model_Id) VALUES(%s, %s, %s, %s)" 
        record = tuple(record)
        print(query)
        cur.execute(query, record)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
        
    return
#5
def removeCab():
    try:
        vrn = int(input('Enter the Cab VRN to be deleted from the database : '))
        query = "DELETE FROM Cab WHERE VRN = %s" %(vrn)
        cur.execute(query)
        con.commit()
    
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)


#6
def updateColorofCab():
    try:
        vrn = int(input('Enter the Cab VRN: '))
        record = []
        flag = 0
        i = 0
        query = 'DELETE FROM Cab_Color WHERE VRN = %d' %(vrn)
        cur.execute(query)
        while flag == 0:
            record[i] = input('Enter the color: ')
            query = "INSERT INTO Cab_Color(VRN, Color) VALUES('%d', '%s')"
            record = tuple(record)
            cur.execute(query,record)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)

#7
def addCabModel():
    try:
        record = []
        print("Enter Cab Model details:")
        record[0] = int(input('Model Id: '))
        record[1] = input('Company: ')
        record[2] = input('Class: ')
        query = "INSERT INTO Car_Model(Model_Id, Company, Class) VALUES(%s, %s, %s)" 
        record = tuple(record)
        print(query)
        cur.execute(query, record)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
        
    return

#8
def removeCarModel():
    try:
        mod = int(input('Enter the Model Id to be deleted: '))
        query = "DELETE FROM Car_Model WHERE Model_Id = %d" %(mod)
        cur.execute(query)
        while flag == 0:
            record[i] = input('Enter the color: ')
            query = "INSERT INTO Cab_Color(VRN, Color) VALUES(%d, %s)"
            record = tuple(record)
            cur.execute(query,record)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch==1): 
        addDriver()
    elif(ch==2):
        removePerson()
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
                db='CAB_SERVICE',
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
                print("16. Add emergency contact")
                print("17. Request a ride")
                print("18. Enter details of an accident")
                print("19. Change ride status")
                print("20. Print Drivers")
                print("21. Print Cabs")
                print("22. Logout")
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
    
   


