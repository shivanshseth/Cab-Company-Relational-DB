import subprocess as sp
import pymysql
import pymysql.cursors
from datetime import datetime

#1
def addPerson(record):
    try:
        query = "INSERT INTO PERSON(SSN, First_name, Last_name, Year, Month, Day, Contact) VALUES(%s, %s, %s, %s, %s, %s, %s)" 
        record = tuple(record)
        # print(query)
        cur.execute(query, record)
        con.commit()

        print("Inserted Into Database")
        return 1

    except Exception as e:
        con.rollback()
        print("Failed to insert into database in addperson")
        print ("Error:", e)
        return -1
#1
def addDriver():
    try:
        record = [0]*7  
        print("Enter driver details:")
        record[0] = input('SSN: ')
        record[1:3] = input('Name(Firstname Lastname): ').split(' ')
        dob = input('DOB(In yyyy-mm-dd format): ').split('-')
        record[3] = int(dob[0])
        record[4] = int(dob[1])
        record[5] = int(dob[2])
        record[6] = int(input('Contact: '))
        print(record)
        flag = addPerson(record)
        if(flag == -1):
            print("Error")
            return
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
        print ("Error:", e)
        
    return
#2
def removePerson():
    try:
        ssn = input('SSN:')
        print(type(ssn))
        query1 = "SELECT * FROM DRIVER WHERE SSN = '%s'" %(ssn)
        row = cur.execute(query1)
        if(row == 1):
            query = "DELETE FROM PERSON WHERE SSN = '%s'"  % (ssn)
            print(query)
            cur.execute(query)
            con.commit()
        else:
            print('The driver does not exist in the database')

    except Exception as e:
        con.rollback()
        print("Failed to insert into database remo")
        print ("Error:", e)
        
    return
#3
def updateContact():
    try:
        ssn = input('Enter the SSN of the Person hose contact is to be changed: ')
        query1 = "SELECT * FROM PERSON WHERE SSN = '%s' " %(ssn)
        co = cur.execute(query1)
        if(co == 1):
            newcon = input('Enter the new contact details: ')
            query = "UPDATE PERSON SET Contact = %s WHERE SSN = '%s' "%(newcon,ssn)
            cur.execute(query)
            con.commit()
        else:
            print("Enter a Person whose details already exists")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print ("Error:", e)

    return
#4
def addCab():
    try:
        record = [0]*4
        print("Enter cab details:")
        record[0] = input('VRN: ')
        record[1] = int(input('Manufacture Year: '))
        record[2] = True
        record[3] = input('Model Id: ')
        query = "INSERT INTO CAB(VRN, Manufacture_Year, Availability, Model_Id) VALUES(%s, %s, %s, %s)" 
        record = tuple(record)
        print(query)
        cur.execute(query, record)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print ("Error:", e)
        
    return
#5
def removeCab():
    try:
        vrn = input('Enter the Cab VRN to be deleted from the database : ')
        query = "DELETE FROM CAB WHERE VRN = '%s'" %(vrn)
        cur.execute(query)
        con.commit()
    
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print ("Error:", e)
#6
def updateColorofCab():
    try:
        vrn = input('Enter the Cab VRN: ')
        record = [0]*10
        flag = 0
        i = 0
        query = 'DELETE FROM CAB_COLOR WHERE VRN = %d' %(vrn)
        cur.execute(query)
        while flag == 0:
            record[i] = input('Enter the color: ')
            query = "INSERT INTO CAB_COLOR(VRN, Color) VALUES('%d', '%s')"
            record = tuple(record)
            cur.execute(query,record)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print ("Error:", e)
#7
def addCarModel():
    try:
        record = [0]*3
        print("Enter Cab Model details:")
        record[0] = input('Model Id: ')
        record[1] = input('Company: ')
        record[2] = input('Class: ')
        query = "INSERT INTO CAR_MODEL(Model_Id, Company, Class) VALUES(%s, %s, %s)" 
        record = tuple(record)
        print(query)
        cur.execute(query, record)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print ("Error:", e)
        
    return
#8
def removeCarModel():
    try:
        mod = input('Enter the Model Id to be deleted: ')
        query = "DELETE FROM CAR_MODEL WHERE Model_Id = '%s'" %(mod)
        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print ("Error:", e)
#9
def addShift():
    try:
        print("Enter the details for adding a new shift: ")
        st = input("Enter the start time(hh:mm format): ")
        et = input("Enter the end time(hh:mm) format: ")
        flag = 0
        query1 = "SELECT * FROM SHIFT as S WHERE S.Start_time < '%s' AND S.End_time < '%s'" %(st, et)
        co = cur.execute(query1)
        query1 = "SELECT * FROM SHIFT as S WHERE S.Start_time < '%s' AND S.End_time > '%s'" %(et, st)
        co += cur.execute(query1)
        if(co == 0):
            query = "SELECT * FROM SHIFT"
            co = cur.execute(query)
            query = "INSERT INTO SHIFT(Shift_Id,Start_time,End_time) VALUES(%s,'%s','%s')"%(co+1,st, et)
            cur.execute(query)
            con.commit()
        else:
            print("The shift overlaps with other shifts. Please give a valid shift")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database add shift")
        print ("Error:", e)
#10
def removeShift():
    try:
        shift_Id = int(input('Enter the Shift Id to be deleted from the database : '))
        query = "DELETE FROM SHIFT WHERE Shift_Id = '%s'" %(shift_Id)
        cur.execute(query)
        con.commit()
    
    except Exception as e:
        con.rollback()
        print("Failed to insert into database remove shift")
        print ("Error:", e)
#11
def assignShifttoDriver():
    try:
        ssn = input('Enter the SSN of the Cab Driver: ')
        shift_Id = input('Enter the Shift you want the driver to be assigned to: ')
        query = "INSERT INTO DRIVER_SHIFT(Driver_SSN,Shift_Id) VALUES(%s,%s)" %(ssn,shift_Id)
        cur.execute(query)
        con.commit()
    
    except Exception as e:
        con.rollback()
        print("Failed to insert into database assignShifttoDriver")
        print ("Error:", e)      
#12
def removeDriverfromShift():
    try:
        ssn = input('Enter the SSN of the Cab Driver: ')
        shift_Id = input('Enter the Shift you want the driver to be removed from: ')
        query = "DELETE FROM DRIVER_SHIFT WHERE Driver_SSN = '%s' AND Shift_Id = '%s' " %(ssn, shift_Id)
        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print ("Error:", e)      
#13
def assignShifttoCab():
    try:
        vrn = input('Enter the VRN of the Cab: ')
        shift_Id = input('Enter the Shift you want the cab to be added to: ')
        query = "INSERT INTO CAB_SHIFT(VRN,Shift_Id) VALUES('%s',%s)" %(vrn, shift_Id)
        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print ("Error:", e)   
#14
def removeCabfromShift():
    try:
        vrn = input('Enter the VRN of the Cab: ')
        shift_Id = input('Enter the Shift you want the cab to be removed from: ')
        query = "DELETE FROM CAB_SHIFT WHERE VRN = '%s' AND Shift_Id = '%s' " %(vrn, shift_Id)
        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeCabfromShift")
        print ("Error:", e)      
#15
def addRider():
    try:
        record = [0]*7  
        print("Enter Rider details:")
        record[0] = input('SSN: ')
        record[1:3] = input('Name: ').split(' ')
        dob = input('DOB: ').split('-')
        record[3] = int(dob[0])
        record[4] = int(dob[1])
        record[5] = int(dob[2])
        record[6] = int(input('Contact: '))
        # print(record)
        flag = addPerson(record)
        if(flag == -1):
            return
        query = "INSERT INTO RIDER(SSN) VALUES(%s)" 
        record = (record[0])
        # print(record)
        cur.execute(query, record)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database add rider")
        print ("Error:", e)
        
    return
#16
def addEmergencyContact():
    try:
        ssn = input("Enter the Rider's ssn whose emergency contact is to be entered")
        query1 = "SELECT * From Emergency_Contact WHERE Rider_SSN = '%s' " %(ssn)
        co = cur.execute(query1)
        if(co == 0):
            record = [0]*10
            record[0] = input("Enter the Emergency Contact number")
            record[1] = ssn
            query = "INSERT INTO Emergency_Contact(Contact,Rider_SSN) VALUES(%s,%s)"
            cur.execute(query,record)
            con.commit()
        else:
            print("already exists")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print ("Error:", e)         
#17 #fill this ride request
def requestARide():
    try:
        ssn = input("Enter your SSN: ")
        now = datetime.now()
        curtime = now.strftime("%H:%M")
        query = "SELECT * FROM REQUEST"
        request_id = cur.execute(query) + 1
        query = "INSERT INTO REQUEST(Request_id,Request_time,Rider_SSN) VALUES(%s,%s,%s)"
        record = [0]*10
        record[0] = request_id
        record[1] = curtime
        record[2] = ssn
        cur.execute(query,record)
        query = "SELECT * FROM DRIVER WHERE Availability = 0"
        co = cur.execute(query)
        if(co == 0):
            print("No Drivers available right now. Please try again later.")
        else:
            record = [0]*10

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print ("Error:", e)  
#18
def addAccidentDetails():
    try:
        ssn = input("Enter the Driver SSN who met with an accident: ")
        query1 = "SELECT * FROM Driver WHERE SSN = '%s' "%(ssn)
        co = cur.execute(query1)
        if(co == 0):
            print("Driver doesnt exist.")
        else:
            record = [0]*10
            record[0] = time(input("Enter the time of the accident: "))
            record[1] = ssn
            record[2] = input("Enter the location of the accident: ")
            query = "INSERT INTO ACCIDENT(Accident_time,Driver_ssn,location) VALUES(%s,%s,%s)"
            cur.execute(query,record)
            con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print ("Error:", e)
#19
def changeStatus():
    return
#20
def printDrivers():
    try:
        newcur = con.cursor()
        query = "SELECT * from DRIVER"
        newcur.execute(query)
        print(newcur.fetchall())

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print ("Error:", e)
#21
def printCabs():
    try:
        newcur = con.cursor()
        query = "SELECT * from CAB"
        newcur.execute(query)
        print(newcur.fetchall())

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print ("Error:", e)
#22

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch==1): 
        addDriver()
    elif(ch==2):
        removePerson()
    elif(ch==3):
        updateContact()
    elif(ch==4):
        addCab()
    elif(ch==5):
        removeCab()
    elif(ch==6):
        updateColorofCab()
    elif(ch==7):
        addCarModel()
    elif(ch==8):
        removeCarModel()
    elif(ch==9):
        addShift()
    elif(ch==10):
        removeShift()
    elif(ch==11):
        assignShifttoDriver()
    elif(ch==12):
        removeDriverfromShift()
    elif(ch==13):
        assignShifttoCab()
    elif(ch==14):
        removeCabfromShift()
    elif(ch==15):
        addRider()
    elif(ch==16):
        addEmergencyContact()
    elif(ch==17):
        removeShift()
    elif(ch==18):
        addAccidentDetails()
    elif(ch==19):
        changeStatus()
    elif(ch==20):
        printDrivers()
    elif(ch==21):
        printCabs()
    elif(ch==22):
        removeShift()
    elif(ch==23):
        removeShift()
    elif(ch==24):
        removeShift()
    elif(ch==25):
        removeShift()
    elif(ch==26):
        removeShift()
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
                print("9. Add shift")#mysql ke database main no overlap,handle with trigger
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
                print("22. Print All Drivers available at a given time")
                print("23. Print All Cabs available at a given time")
                print("24. Print All Requests available right now to be accepted by a driver")
                print("25. Print All Accidents a Driver has been part of")
                print("26. Print All Cabs of a certain type")
                print("27. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear',shell=True)
                if ch==27:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")


    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
    
   


