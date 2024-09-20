import tkinter as tk
import mysql.connector
#import func_tkinter as fun

mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql",
  database="bus_reservation")



window=tk.Tk()

title=tk.Label(text="NNK BUS SERVICE",fg="black",bg="light grey").pack()


schedule_button=tk.Button(window,text='Bus Schedule',padx=25).pack()
booking_button=tk.Button(window,text='Book Tickets',padx=27).pack()
status_button=tk.Button(window,text='Status',padx=44).pack()
exit_button=tk.Button(window,text='Exit',padx=51).pack()



#def book_tickets():
   # schedule_heading=tk.Label(text="BUS SCHEDULE",fg="white",bg="black").pack()
   # journeydate=tk.Entry(window,width=25,borderwidth=50).pack()

#mybutton=tk.Button(window,command=book_tickets)


#label = tk.Label(text="Name").pack()    ,command=fun.book_tickets
#entry = tk.Entry()
#entry.pack()
#name=entry.get()
#print(name)
#window.mainloop()
