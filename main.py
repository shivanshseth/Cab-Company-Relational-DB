import subprocess as sp
import pymysql
import pymysql.cursors
from datetime import datetime
import texttable as tt

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
        record[2] = 'True';
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
        record[2] = 'True'
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
            query = "INSERT INTO SHIFT(Start_time,End_time) VALUES('%s','%s')"%(st, et)
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
        query = "INSERT INTO DRIVER_SHIFT(Driver_SSN,Shift_Id) VALUES('%s',%s)" %(ssn,shift_Id)
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
        ssn = input("Enter the Rider's ssn whose emergency contact is to be entered: ")
        record = [0]*2
        record[0] = input("Enter the Emergency Contact number: ")
        record[1] = ssn
        query = "INSERT INTO EMERGENCY_CONTACT(Contact,Rider_SSN) VALUES(%s,%s)"
        cur.execute(query,record)
        con.commit()
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
        record = [0]*3
        record[0] = request_id
        record[1] = curtime
        record[2] = ssn
        # print('yeet')
        cur.execute(query,record)
        query1 = "SELECT Shift_Id FROM SHIFT as S WHERE S.Start_time < '%s' AND S.End_time > '%s'" %(curtime, curtime)
        d = cur.execute(query1)
        shifts = []
        driverssn = None
        canvrn = None
        if d > 0:
            shifts = cur.fetchall()
        else:
            print('Service unavailable')
            return
        co = 0
        for shift in shifts:
            shiftid = shift["Shift_Id"]
            query = "SELECT Driver_SSN, c.VRN from DRIVER_SHIFT as ds, DRIVER as d, CAB as c, CAB_SHIFT as cs where ds.Shift_Id = '%s' AND d.Availability = 'True' AND d.SSN = ds.Driver_SSN and cs.Shift_Id = '%s' AND c.Availability = 'True' AND c.VRN = cs.VRN" %(shiftid, shiftid)
            d = cur.execute(query)
            # con.commit()
            # print('yeet2')
            if d >= 1:
                dic = cur.fetchall()
                # print(dic)
                driverssn = dic[0]["Driver_SSN"]
                cabvrn = dic[0]["VRN"]
                query = "UPDATE DRIVER SET Availability = 'False' where SSN = '%s'" %(driverssn)
                cur.execute(query)
                query = "UPDATE CAB SET Availability = 'False' where VRN = '%s'" %(cabvrn)
                cur.execute(query)
                co = 1
                query = "SELECT First_name, Last_name from PERSON as p, DRIVER as d where p.SSN = '%s' and d.SSN = '%s'" %(driverssn, driverssn)
                cur.execute(query)
                dic  = cur.fetchone()
                name = dic["First_name"] + ' ' + dic["Last_name"]
                print('Driver Assigned: ' + name)
                print('VRN of the Cab assigned: ' + cabvrn)
                break
        if co == 0: 
            print("No Drivers available right now. Please try again later.")
            return
        record = [0]*8
        record[0] = request_id
        record[1] = curtime
        record[2] = None
        record[3] = input('Enter starting position: ')
        record[4] = input('Enter end position: ')
        record[5] = shiftid
        record[6] = cabvrn
        record[7] = driverssn
        print
        query = "INSERT INTO RIDE(Request_id,Ride_start, Ride_end,Starting_pos,Ending_pos,Shift_id,Cab_VRN,Driver_SSN) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(query, tuple(record))
        query = "INSERT INTO RIDE_STATUS(Status_time,Rider_SSN,Status_details) VALUES(%s,%s,%s)"
        record = [0] * 3
        record[0] = curtime
        record[1] = ssn
        record[2] = 'Onroute'
        cur.execute(query, tuple(record))
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print ("Error:", e)  
#18
def addAccidentDetails():
    try:
        ssn = input("Enter the Driver SSN who met with an accident: ")
        query1 = "SELECT * FROM DRIVER WHERE SSN = '%s' "%(ssn)
        co = cur.execute(query1)
        if(co == 0):
            print("Driver doesnt exist.")
        else:
            record = [0]*3
            record[0] = input("Enter the time of the accident: ")
            record[1] = ssn
            record[2] = input("Enter the location of the accident: ")
            query = "INSERT INTO ACCIDENT(Accident_time,Driver_SSN,location) VALUES(%s,%s,%s)"
            cur.execute(query,record)
            con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print ("Error:", e)
#19
def changeStatus():
    try:
        now = datetime.now()
        curtime = now.strftime("%H:%M")
        ssn = input('Enter Rider SSN: ')
        request_id = input('Enter Request_ID: ')
        status = input('Enter Status(Onroute/Finished/Emergency/Failed): ')
        if not status == 'Onroute':
            query = "UPDATE RIDE SET Ride_end = '%s' where Request_id = '%s'" %(curtime, request_id)
            cur.execute(query)
            query = "UPDATE DRIVER SET Availability = 'True' where SSN = (SELECT Driver_SSN from RIDE where Request_id = '%s')" %(request_id)
            cur.execute(query)
            query = "UPDATE CAB SET Availability = 'True' where VRN = (SELECT Cab_VRN from RIDE where Request_id = '%s')" %(request_id)
            cur.execute(query)
        query = "INSERT INTO RIDE_STATUS(Status_time,Rider_SSN,Status_details) VALUES(%s,%s,%s)"
        record = [0] * 3
        record[0] = curtime
        record[1] = ssn
        record[2] = status
        cur.execute(query, tuple(record))
        con.commit()
        return

    except Exception as e:
        print('Error: ', e)
#20
def printDrivers():
    try:
        newcur = con.cursor()
        query = "SELECT * from DRIVER"
        newcur.execute(query)
        record = newcur.fetchall()
        tab = tt.Texttable()
        headings = ['SSN','Availability','License_number']
        tab.header(headings)
        ssn = []
        availability = []
        license = []
        for i in record:
            ssn.append(i['SSN'])
            availability.append(i['Availability'])
            license.append(i['License_number'])

        for row in zip(ssn,availability,license):
            tab.add_row(row)

        s = tab.draw()
        print (s)

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print (">>>>>>>>>>>>>", e)
#21
def printCabs():
    try:
        newcur = con.cursor()
        query = "SELECT * from CAB"
        newcur.execute(query)
        record = newcur.fetchall()
        tab = tt.Texttable()
        headings = ['VRN','Manufacture_Year','Availability','Model_id']
        tab.header(headings)
        vrn = []
        man_year = []
        availability = []
        mod = []
        for i in record:
            vrn.append(i['VRN'])
            man_year.append(i['Manufacture_Year'])
            availability.append(i['Availability'])
            mod.append(i['Model_id'])

        for row in zip(vrn,man_year,availability,mod):
            tab.add_row(row)

        s = tab.draw()
        print (s)

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print (">>>>>>>>>>>>>", e)
#22
def printAvailableDrivers():
    try:
        newcur = con.cursor()
        now = datetime.now()
        curtime = now.strftime("%H:%M")
        query = "SELECT p.First_name, p.Last_name, d.License_number from PERSON as p, DRIVER_SHIFT as ds, DRIVER as d, SHIFT as s where s.Start_time < '%s' and s.End_time> '%s' and ds.Shift_Id = s.Shift_Id AND d.Availability = 'True' AND d.SSN = ds.Driver_SSN AND p.SSN = ds.Driver_SSN" %(curtime, curtime)
        newcur.execute(query)
        record = newcur.fetchall()
        tab = tt.Texttable()
        headings = ['FName','LName','License_number']
        tab.header(headings)
        ssn = []
        availability = []
        license = []
        for i in record:
            ssn.append(i['First_name'])
            availability.append(i['Last_name'])
            license.append(i['License_number'])

        for row in zip(ssn,availability,license):
            tab.add_row(row)

        s = tab.draw()
        print (s)

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print ("Error: ", e)
#23
def printAvailableCabs():
    try:
        newcur = con.cursor()
        now = datetime.now()
        curtime = now.strftime("%H:%M")
        query = "SELECT c.VRN, c.Manufacture_Year, c.Availability, c.Model_id from CAB as c, CAB_SHIFT as cs, SHIFT as s where s.Start_time < '%s' and s.End_time> '%s' and cs.Shift_Id = s.Shift_Id AND c.Availability = 'True' AND c.VRN = cs.VRN" % (curtime, curtime)
        newcur.execute(query)
        record = newcur.fetchall()
        tab = tt.Texttable()
        headings = ['VRN','Manufacture_Year','Availability','Model_id']
        tab.header(headings)
        vrn = []
        man_year = []
        availability = []
        mod = []
        for i in record:
            vrn.append(i['VRN'])
            man_year.append(i['Manufacture_Year'])
            availability.append(i['Availability'])
            mod.append(i['Model_id'])

        for row in zip(vrn,man_year,availability,mod):
            tab.add_row(row)

        s = tab.draw()
        print (s)

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print ("Error: ", e)
#24
def printAvailableRequests():
    try:
        newcur = con.cursor()
        query = "SELECT * FROM REQUEST WHERE Request_id NOT IN(select Request_id from RIDE)"
        newcur.execute(query)
        record = newcur.fetchall()
        tab = tt.Texttable()
        headings = ['Request_id','Request_time','Rider_SSN']
        tab.header(headings)
        r_id = []
        r_time = []
        r_ssn = []
        for i in record:
            r_id.append(i['Request_id'])
            r_time.append(i['Request_time'])
            r_ssn.append(i['Rider_SSN'])

        for row in zip(r_id,r_time,r_ssn):
            tab.add_row(row)

        s = tab.draw()
        print (s)

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print (">>>>>>>>>>>>>", e)
#25
def printAccidentOfDrivers():
    try:
        newcur = con.cursor()
        query = "SELECT * from DRIVER inner join ACCIDENT where SSN = Driver_SSN"
        newcur.execute(query)
        record = newcur.fetchall()
        tab = tt.Texttable()
        headings = ['SSN','Availability','License_number','Accident_time','Location']
        tab.header(headings)
        ssn = []
        availability = []
        license = []
        acc_time = []
        location = []
        for i in record:
            ssn.append(i['SSN'])
            availability.append(i['Availability'])
            license.append(i['License_number'])
            acc_time.append(i['Accident_time'])
            location.append(i['Location'])

        for row in zip(ssn,availability,license,acc_time,location):
            tab.add_row(row)

        s = tab.draw()
        print (s)

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print (">>>>>>>>>>>>>", e)
#26
def printTypesOfCabs():
    try:
        newcur = con.cursor()
        query = "SELECT Class, Count(*) from CAB, CAR_MODEL as cm where cm.Model_id = CAB.Model_id group by cm.Class"
        newcur.execute(query)
        record = newcur.fetchall()
        tab = tt.Texttable()
        headings = ['Class','Count']
        tab.header(headings)
        cla = []
        co = []
        for i in record:
            cla.append(i['Class'])
            co.append(i['count(*)'])

        for row in zip(cla,co):
            tab.add_row(row)

        s = tab.draw()
        print (s)

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print (">>>>>>>>>>>>>", e)
#27
def printShifts():
    try:
        newcur = con.cursor()
        query = "SELECT * FROM SHIFT"
        newcur.execute(query)
        record = newcur.fetchall()
        tab = tt.Texttable()
        headings = ['Shift Id','Start time','End time']
        tab.header(headings)
        s_id = []
        s_t = []
        e_t = []
        for i in record:
            s_id.append(i['Shift_id'])
            s_t.append(i['Start_time'])
            e_t.append(i['End_time'])

        for row in zip(s_id,s_t,e_t):
            tab.add_row(row)

        s = tab.draw()
        print (s)

    except Exception as e:
        con.rollback()
        print("Failed to insert into database removeDriverfromShift")
        print (">>>>>>>>>>>>>", e)

def dispatch_admin(ch):
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
        requestARide()
    elif(ch==18):
        addAccidentDetails()
    elif(ch==19):
        changeStatus()
    elif(ch==20):
        printDrivers()
    elif(ch==21):
        printCabs()
    elif(ch==22):
        printAvailableDrivers()
    elif(ch==23):
        printAvailableCabs()
    elif(ch==24):
        printAvailableRequests()
    elif(ch==25):
        printAccidentOfDrivers()
    elif(ch==26):
        printTypesOfCabs()
    elif(ch==27):
        printShifts()
    else:
        print("Error: Invalid Option")

def dispatch_rider(ch):
    """
    Function that maps helper functions to option entered for rider
    """
    if(ch==1):
        updateContact()
    elif(ch==2):
        addRider()
    elif(ch==3):
        addEmergencyContact()
    elif(ch==4):
        requestARide()   
    elif(ch==5):
        printAvailableDrivers()
    elif(ch==6):
        printAccidentOfDrivers()
    elif(ch==7):
        changeStatus()
    elif(ch==8):
        printTypesOfCabs()
    else:
        print("Error: Invalid Option")

def dispatch_driver(ch):
    """
    Function that maps helper functions to option entered for rider
    """
    if(ch==1):
        updateContact()
    elif(ch==2):
        printCabs()
    elif(ch==3):
        printAvailableCabs()
    elif(ch==4):
        printAvailableRequests()
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
                if username=="admin":
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
                    print("27. Print Shifts")
                    print("28. Logout")
                    ch = int(input("Enter choice> "))
                    tmp = sp.call('clear',shell=True)
                    if ch==28:
                        break
                    else:
                        dispatch_admin(ch)
                    tmp = input("Enter any key to CONTINUE>")
                
                elif username=="rider":
                    print("1. Update contact")
                    print("2. Add a rider")
                    print("3. Add emergency contact")
                    print("4. Request a ride")
                    print("5. Print All Drivers available at a given time")
                    print("6. Print All Accidents a Driver has been part of")
                    print("7. Change ride status")
                    print("8. Check Availability of cab")
                    print("9. Logout")
                    ch = int(input("Enter choice> "))
                    tmp= sp.call('clear',shell=True)
                    if ch==9:
                        break
                    else:
                        dispatch_rider(ch)
                    tmp = input("Enter any key to CONTINUE>")

                elif username=="driver":
                    print("1. Update contact")
                    print("2. Print Cabs")
                    print("3. Print All Cabs available at a given time")
                    print("4. Print All Requests available right now to be accepted by a driver")
                    print("5. Logout")
                    ch = int(input("Enter choice> "))
                    tmp= sp.call('clear',shell=True)
                    if ch==5:
                        break
                    else:
                        dispatch_driver(ch)
                    tmp = input("Enter any key to CONTINUE>")



    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")

