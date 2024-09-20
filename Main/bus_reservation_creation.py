import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="mysql")

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE bus_reservation")
mydb=mysql.connector.connect(host="localhost",user="root",password="mysql",database='bus_reservation')
mycursor = mydb.cursor()
#bus_category 
mycursor.execute('''CREATE TABLE Bus_Category(
                BusCategoryId 	int(5),
                CategoryName	Varchar(50),
                CONSTRAINT primary key PK_Bus_Category (BusCategoryId ASC));''')
#Bus_Master 
mycursor.execute('''CREATE TABLE Bus_Master(
	BusId		Int(10) ,
	BusName 	varchar(100),
	CategoryId  	int(5) References  Bus_Category(BusCategoryId ),
	No_of_seats	int(5),
	Contact 	varchar(15),
	CONSTRAINT primary key PK_Bus_Master (BusId ASC));''')
#Bus_Journey 
mycursor.execute('''CREATE TABLE Bus_Journey(
        RouteId		Int(10) ,
        Dateofjourney   date,
	StartingPoint 	varchar(100),
	EndingPoint	varchar(100),
	StartTime	time,
	Endtime		time,
	BusId		int References  Bus_Master(BusId),
	Fare		decimal,
        CONSTRAINT primary key PK_Bus_Journey (RouteId ASC));''')
#Bus_Booking 
mycursor.execute('''CREATE TABLE Bus_Booking(
	RouteId		Int(10) NOT NULL,
	BookingId	int(10) NOT NULL ,
        fullname    varchar(25) NOT NULL,
	No_of_Seats	Int		NOT NULL,
	ContactPhone    varchar(15) 	NOT NULL,
	Email		varchar(128)	NOT NULL,
        CONSTRAINT primary key PK_Bus_Booking (RouteId ASC,BookingId ASC));''')
#Route_Passengers 
mycursor.execute('''CREATE TABLE Route_Passengers(
	RouteId		Int(10) ,
	SeatNumber	Int(5)  ,	
	BookingId	int(10) ,
	FullName	varchar(100),
	Age		int,
	Sex		Char(1),
        CONSTRAINT primary key PK_Route_Passengers (RouteId ASC,SeatNumber ASC));''')
