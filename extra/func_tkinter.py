import tkinter as tk
import mysql.connector

mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql",
  database="bus_reservation")


window=tk.Tk()

title=tk.Label(text="NNK BUS SERVICE",fg="black",bg="light grey",pady=10,padx=10).pack()


def book_tickets():
    schedule_heading=tk.Label(text="BUS SCHEDULE",fg="white",bg="black").pack()
    journeydate=tk.Entry(window)

mybutton=tk.Button(window,command=book_tickets)
