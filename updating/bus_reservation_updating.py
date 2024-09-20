import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="mysql",database="bus_reservation")

  
mycursor = mydb.cursor()
print("------------------WELCOME TO------------------")
print("----------------NNK BUS SERVICE----------------")


def user():
        print('1. Customer')
        print('2. Administrator')
        us=int(input('Select:'))
        if us==2:
                pwd_re=validate_password()
                if pwd_re==0:
                        print("YOUR ADMINISTRATOR PASSWORD IS INCORRECT \n ~~~~~Contact NNK bus service~~~~~")
                        return
        menu(us)


def validate_password():
        password=input("Enter admin password:")
        if password=='nnkbus':
                return 1
        else:
                return 0

def menu(us_type=1):
        global chk
        if us_type==1:
                chk=1
        elif us_type==2:
                chk=2
        print('1. Book Tickets')
        print('2. Status')
        print('3. Bus Schedule')
        if us_type ==2:
                print('4. Report')
        print('0. Exit')
        choice=int(input('Choose:'))

        if choice==1:
                book_tickets()
        elif choice==2:
                status()
        elif choice==3:
                bus_schedule()
        elif choice==4 and  us_type==2 :
                bus_report()                
        else:
                pass


def book_tickets():
        print('BOOK TICKETS')
        journeyDate=input("Enter Journey Date .E.g: YYYY-MM-DD:")

        print('STARTING POINT')
        start="select distinct StartingPoint from bus_journey;"
        mycursor.execute(start)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        startp=input('select starting point:')
     
        print('ENDING POINT')
        end="select distinct endingPoint from bus_journey where endingpoint!=%s;"
        mycursor.execute(end,(startp,))
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        endp=input('select ending point:')
        print('')


        #printing the list of busses
        selstartend='''SELECT routeid,dateofjourney, startingpoint, endingpoint, StartTime,Endtime,Fare,busname,categoryname,No_of_seats,Contact FROM bus_journey 
                        INNER JOIN bus_master ON bus_journey.busid = bus_master.busid
                        INNER JOIN bus_category ON bus_category.buscategoryid=bus_master.categoryid
                        where StartingPoint=%s and endingPoint=%s and Dateofjourney=%s;'''
        mycursor.execute(selstartend,(startp,endp,journeyDate,))
        myresult = mycursor.fetchall()
        for x in myresult:
                print('ID',x[0])
                print('Date of journey:',x[1])
                print('Starting point:',x[2])
                print('Ending point:',x[3])
                print('StartTime:',x[4])
                print('Endtime:',x[5])
                print('Fare:',x[6])
                print('Busname:',x[7])
                print('Category:',x[8])
                print('No_of_seats:',x[9])
                print('Contact:',x[10],'\n')
        if myresult==[]:
                print("NO BUSES AVAILABLE IN THE PREFERRED DATE")
                return
        else:
                #selecting bus
                route=int(input("Select your bus by entering the id:"))
                selbookid='SELECT IFNULL((select max(bookingid)+1 from bus_booking),1);'
                mycursor.execute(selbookid)
                myresult = mycursor.fetchall()
                for x in myresult:
                        bookid=int(x[0])
                print('BOOKING_ID:',bookid)





                #inputing details of booking person
                print("-----ENTER YOUR DETAILS-----")
                confirm="no"
                while confirm=="no":
                        myinput=()
                        myinput=myinput + (route,)
                        myinput=myinput + (bookid,)
                        b_name=input("NAME:")
                        myinput=myinput + (b_name,)
                        no_of_seats=int(input("No of Seats:"))
                        myinput=myinput + (no_of_seats,)
                        b_contactphone=input("Contact:")
                        myinput=myinput + (b_contactphone,)
                        b_email=input("Email:")
                        myinput=myinput + (b_email,)



                        print("BookingID:",bookid)
                        print("RouteID:",route)
                        print("Name:",b_name)
                        print("Email:",b_email)
                        print("Contact:",b_contactphone)
                        print("No of Seats:",no_of_seats)
                        print("Do you Want to Confirm")
                        confirm=input("yes/no:")
                if confirm=='yes':
                        booking_input="insert into bus_booking (RouteId, BookingId, fullname, No_of_Seats, ContactPhone, Email) values(%s,%s,%s,%s,%s,%s)"
                        mycursor.execute(booking_input,myinput)


                        #inputing passenger details
                        print("-----ENTER PASSENGERS DETAILS-----")
                     
                        for i in range(0,no_of_seats):
                                con='no'
                                while con=='no':
                                        mypass=()
                                        mypass=mypass + (route,)
                                        #seat selection
                                        mycursor.execute('''select No_of_seats from bus_master
                                                                INNER JOIN bus_journey ON bus_master.BusId=bus_journey.BusId
                                                                where routeid=%s;''',(route,))
                                        myresult=mycursor.fetchall()
                                        print('CHOOSE YOUR SEAT')
                                        if myresult[0][0]==20:
                                                print('{D} {01}{05}{09}{13}{17}|\n    {02}{06}{10}{14}{18}|\n------------------------|\n    {03}{07}{11}{15}{19}|\n    {04}{08}{12}{16}{20}|')
                                        elif myresult[0][0]==25:
                                                print('{D} {01}{05}{09}{13}{17}{21}|\n    {02}{06}{10}{14}{18}{22}|\n------------------------{23}|\n    {03}{07}{11}{15}{19}{24}|\n    {04}{08}{12}{16}{20}{25}|')
                                        elif myresult[0][0]==30:
                                                print('{D} {01}{06}{11}{16}{21}{26}|\n    {02}{07}{12}{17}{22}{27}|\n    {03}{08}{13}{18}{23}{28}|\n----------------------------|\n    {04}{09}{14}{19}{24}{29}|\n    {05}{10}{15}{20}{25}{30}|')
                                        elif myresult[0][0]==35:
                                                print('{D} {01}{06}{11}{16}{21}{26}{31}|\n    {02}{07}{12}{17}{22}{27}{32}|\n    {03}{08}{13}{18}{23}{28}{33}|\n--------------------------------|\n    {04}{09}{14}{19}{24}{29}{34}|\n    {05}{10}{15}{20}{25}{30}{35}|')

                                        mycursor.execute('SELECT SeatNumber from route_passengers where routeid=%s;',(route,))
                                        booked=mycursor.fetchall()
                                        booked_seat=[]
                                        for t in booked: 
                                                for x in t: 
                                                        booked_seat.append(x)
                                        print('BOOKED SEATS:',booked_seat )
                                        

                                        p_seat=int(input("Seat No:"))
                                        if p_seat in booked_seat:
                                                print('SELECTED SEAT ALREADY BOOKED')
                                        else:
                                                if p_seat>myresult[0][0]:
                                                        print('ENTER VALID SEAT NO.')
                                                else:
                                                        mypass=mypass + (p_seat,)
                                                        mypass=mypass + (bookid,)
                                                        p_name=input("Full Name:")
                                                        mypass=mypass + (p_name,)
                                                        p_age=input("Age:")
                                                        mypass=mypass + (p_age,)
                                                        p_sex=input("Sex:(M/F)")
                                                        mypass=mypass + (p_sex,)
                                                


                                                        print("Name:",p_name)
                                                        print("Sex:",p_sex)
                                                        print("Age:",p_age)
                                                        print("Seats No:",p_seat)
                                                        print("Do you Want to Confirm")
                                                        con=input("yes/no:")
                                                        if con=='yes':
                                                                pass_input="insert into route_passengers values(%s,%s,%s,%s,%s,%s)"
                                                                mycursor.execute(pass_input,mypass)
                        mycursor.execute('SELECT Fare FROM bus_journey where RouteId=%s;',(route,))
                        fare= mycursor.fetchone()
                        amount=no_of_seats*fare[0]
                        mycursor.execute("update bus_booking set total_fare=%s where BookingId=%s;",(amount,bookid))
                        print("TOTAL AMOUNT:",amount)
                        bo=input('Book tickets(yes/no):')
                        if bo=='yes':
                                mydb.commit()
                                #FINAL DETAILS
                                print("-----TRAVEL DETAILS-----")
                                print('BOOKING_ID:',bookid,'\n')
                                mycursor.execute('''SELECT dateofjourney, startingpoint, endingpoint,StartTime,Endtime,busname,categoryname FROM bus_journey 
                                                        INNER JOIN bus_master ON bus_journey.busid = bus_master.busid
                                                        INNER JOIN bus_category ON bus_category.buscategoryid=bus_master.categoryid
                                                        inner join bus_booking ON bus_booking.RouteId=bus_journey.RouteId
                                                        where BookingId=%s;''',(bookid,))
                                myresult = mycursor.fetchall()
                                for x in myresult:
                                        print('Date of journey:',x[0])
                                        print('Starting point:',x[1])
                                        print('Ending point:',x[2])
                                        print('StartTime:',x[3])
                                        print('Endtime:',x[4])
                                        print('Busname:',x[5])
                                        print('Category:',x[6],'\n')

                                print('PASSENGERS')
                                mycursor.execute('SELECT FullName,Age,Sex FROM route_passengers where BookingId=%s;',(bookid,))
                                myresult = mycursor.fetchall()
                                for x in myresult:
                                        print('FullName:',x[0])
                                        print('Age:',x[1])
                                        print('Sex:',x[2],'\n')

                                print("TOTAL AMOUNT:",amount)
                                print('')
                                print('BOOKING SUCCESSFUL')
                                print('HAVE A SAFE AND HAPPY JOURNEY')
                        else:
                                menu(chk)


                
def status():
        print('BUS STATUS')
        bookid=int(input("Enter your booking_ID:"))

        print('~~~~~~~~~~~~~~~~~~BUS DETAILS~~~~~~~~~~~~~~~~~~')
        mycursor.execute('''SELECT dateofjourney, startingpoint, endingpoint,starttime,endtime,busname,categoryname,contact FROM bus_journey 
                                INNER JOIN bus_master ON bus_journey.busid = bus_master.busid
                                INNER JOIN bus_category ON bus_category.buscategoryid=bus_master.categoryid
                                INNER JOIN bus_booking ON bus_booking.routeid=bus_journey.routeid
                                where bookingid=%s;''',(bookid,))
        myresult=mycursor.fetchone()
        print('Date of journey:',myresult[0])
        print('Starting point:',myresult[1])
        print('Ending point:',myresult[2])
        print('StartTime:',myresult[3])
        print('Endtime:',myresult[4])
        print('Busname:',myresult[5])
        print('Category:',myresult[6])
        print('Contact of bus:',myresult[7])
        
        print('~~~~~~~~~~~~~~~PASSENGER DETAILS~~~~~~~~~~~~~~~')
        mycursor.execute('SELECT FullName, Age, Sex,SeatNumber FROM route_passengers WHERE bookingid=%s',(bookid,))
        myresult=mycursor.fetchall()
        for x in myresult:
                print('Name',x[0])
                print('Age',x[1])
                print('Sex',x[2])
                print('SeatNumber',x[3],'\n')

        mycursor.execute('SELECT total_fare FROM bus_booking WHERE bookingid=%s',(bookid,))
        myresult=mycursor.fetchone()
        print('TOTAL FARE:',myresult[0])


def bus_schedule():
        print("Sort by:")
        print("1. BUS ROUTE")
        print("2. DATE")
        sch=int(input("Choose:"))
        if sch==1:
                print('STARTING POINT')
                start="select distinct StartingPoint from bus_journey;"
                mycursor.execute(start)
                myresult = mycursor.fetchall()
                for x in myresult:
                        print(x)
                startp=input('select starting point:')

                print('ENDING POINT')
                end="select distinct endingPoint from bus_journey where endingpoint!=%s;"
                mycursor.execute(end,(startp,))
                myresult = mycursor.fetchall()
                for x in myresult:
                        print(x)
                endp=input('select ending point:')
                print('')

                print('BUS SCHEDULE')
                print('--------------')
                schedule ='''SELECT dateofjourney, startingpoint, endingpoint, StartTime, Endtime, busname,categoryname FROM bus_journey
                                INNER JOIN bus_master ON bus_journey.busid = bus_master.busid
                                INNER JOIN bus_category ON bus_category.buscategoryid=bus_master.categoryid
                                WHERE startingpoint=%s and endingpoint=%s
                                ORDER BY dateofjourney;'''
                mycursor.execute(schedule,(startp,endp))
                myresult=mycursor.fetchall()
                if myresult==[]:
                        print("NO BUSES AVAILABLE")
                else:
                        print('%10s'%'date of journey','%18s'%'startingpoint','%20s'%'endingpoint','%18s'%'starttime','%19s'%'endtime','%20s'%'bsname','%20s'%'category')
                        print("****************************************************************************************************************************************")
                        Lengt =len(myresult[0])
                        for x in myresult:
                                print('%10s'%x[0],'%20s'%x[1],'%20s'%x[2],'%20s'%x[3],'%20s'%x[4],'%20s'%x[5],'%20s'%x[6])
                        print('\n') 	
        elif sch==2:
                journeyDate=input("Enter Journey Date .E.g: YYYY-MM-DD:")
                print('BUS SCHEDULE')
                schedule ='''SELECT dateofjourney, startingpoint, endingpoint, StartTime, Endtime, bus_master.busname,categoryname FROM bus_journey
                                INNER JOIN bus_master ON bus_journey.busid = bus_master.busid
                                INNER JOIN bus_category ON bus_category.buscategoryid=bus_master.categoryid
                                WHERE dateofjourney=%s;'''
                mycursor.execute(schedule,(journeyDate,))
                myresult = mycursor.fetchall()
                if myresult==[]:
                        print("NO BUSES AVAILABLE")
                else:
                        print('%10s'%'date of journey','%18s'%'startingpoint','%20s'%'endingpoint','%18s'%'starttime','%19s'%'endtime','%20s'%'bsname','%20s'%'category')
                        print("****************************************************************************************************************************************")
                        for x in myresult:
                                print('%10s'%x[0],'%20s'%x[1],'%20s'%x[2],'%20s'%x[3],'%20s'%x[4],'%20s'%x[5],'%20s'%x[6])
                        print('\n')

def bus_report():
        print('1. Passengers Report')
        print('2. Booking report')
        print('3. Bus Details')
        cho_re=int(input("Choose:"))
        if cho_re==1:
                passenger_report()
        elif cho_re==2:
                booking_report()
        elif cho_re==3:
                bus_details()
def passenger_report():
        mycursor.execute('''select BookingId,Dateofjourney,StartingPoint,EndingPoint,BusName,FullName,Age,Sex from bus_journey
                                inner join bus_master on bus_master.BusId=bus_journey.BusId
                                inner join route_passengers on route_passengers.RouteId=bus_journey.RouteId
                                order by BookingId;''')
        myresult = mycursor.fetchall()
        if myresult==[]:
                        print("NO DETAILS AVAILABLE")
        else:
                        print('%10s'%'Booking Id','%18s'%'Date of journey','%20s'%'Starting Point','%18s'%'Ending Point','%19s'%'Bus Name','%20s'%'Full Name','%10s'%'Age','%10s'%'Sex')
                        print("****************************************************************************************************************************************")
                        for x in myresult:
                                print('%5s'%x[0],'%20s'%x[1],'%20s'%x[2],'%20s'%x[3],'%20s'%x[4],'%20s'%x[5],'%10s'%x[6],'%10s'%x[7])
                        print('\n')
        
def bus_details():
        mycursor.execute('select * from bus_master;')
        myresult = mycursor.fetchall()
        if myresult==[]:
                        print("NO DETAILS AVAILABLE")
        else:
                        print('%10s'%'Bus Id','%18s'%'Bus Name','%20s'%'Category Id','%18s'%'No_of_seats','%19s'%'Contact')
                        print("****************************************************************************************************************************************")
                        for x in myresult:
                                print('%5s'%x[0],'%20s'%x[1],'%20s'%x[2],'%20s'%x[3],'%20s'%x[4])
                        print('\n')


def booking_report():
        mycursor.execute('select * from bus_booking ORDER BY BookingId;')
        myresult = mycursor.fetchall()
        if myresult==[]:
                        print("NO DETAILS AVAILABLE")
        else:
                        print('%7s'%'Route Id','%18s'%'Booking Id','%18s'%'full Name','%18s'%'No_of_seats','%17s'%'Contact','%24s'%'Email','%21s'%'Total Fare')
                        print("****************************************************************************************************************************************")
                        for x in myresult:
                                print('%7s'%x[0],'%17s'%x[1],'%23s'%x[2],'%14s'%x[3],'%20s'%x[4],'%25s'%x[5],'%20s'%x[6])
                        print('\n')
def addbus():
        

user()
while True:
        x=input("Do you want to continue:")
        if x.lower() in('yes','y'):
                menu(chk)
        else:
                print("~~~~~~THANK YOU FOR USING NNK BUS SERVICE~~~~~~")
                break

