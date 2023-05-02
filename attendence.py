from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# import MySQLdb
import pymysql
# import mysql.connector


class Student_Attendence:      
     def __init__(self, root):
         print('here')
         self.root = root
         self.root.geometry("1580x800")
         self.root.title("Take Attendence")

         # Create labels
         id_label = Label(root, text="Student ID:")
         id_label.grid(row=0, column=0)

         name_label = Label(root, text="Student Name:")
         name_label.grid(row=1, column=0)

         roll_label = Label(root, text="Student Roll No:")
         roll_label.grid(row=2, column=0)

         division_label = Label(root, text="Division:")
         division_label.grid(row=3, column=0)

         # Create entry fields
         self.id_entry = Entry(root)
         self.id_entry.grid(row=0, column=1)

         self.name_entry = Entry(root)
         self.name_entry.grid(row=1, column=1)

         self.roll_entry = Entry(root)
         self.roll_entry.grid(row=2, column=1)

         self.division_entry = Entry(root)
         self.division_entry.grid(row=3, column=1)

         # Create submit button
         submit_button = Button(root, text="Submit", command=self.submit)
         submit_button.grid(row=4, column=1)

         # Connect to database
         self.db = pymysql.connect(host="127.0.0.1", user="root", password='', database="student_attendence")
         self.cursor = self.db.cursor()


     def submit(self):
         # Retrieve data from entry fields
         student_id = self.id_entry.get()
         student_name = self.name_entry.get()
         student_roll = self.roll_entry.get()
         student_division = self.division_entry.get()

         # Insert data into database
         sql = "INSERT INTO attendence (student_id, student_name, student_roll, student_division) VALUES (%s, %s, %s, %s)"
         values = (student_id, student_name, student_roll, student_division)
         self.cursor.execute(sql, values)
         self.db.commit()

     def __del__(self):
         # Close cursor and database connection
         self.cursor.close()
         self.db.close()

if __name__ == "__main__":
    root = Tk()        
    obj = Student_Attendence(root)
    root.mainloop()





# Copy code
# pip install mysqlclient

# Copy code
# pip install pymysql
# pip install mysql-connector-python


# Copy code
# import pymysql
# import mysql.connector






# Regenerate response