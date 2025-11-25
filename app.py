#Application to change various values in SQL Table
#With Combobox for the selection and button to execute in SP
#Author = Rikit Thapa
#Version 1.0 December 2,2024


#Import References
from tkinter import *
from tkinter import (messagebox, ttk)
from tkinter.ttk import Combobox
import pyodbc
from tkinter import simpledialog

# Establish Connection parameters for Database
#Driver, Server, Database, and Trusted Certificate
conn = pyodbc.connect(
    'DRIVER={SQL Server Native Client 11.0};'
    'SERVER=ACER_ASPIRE;'
    'DATABASE=AdventureWorkSLT2019;'
    'UID=sa;'
    'PWD=rikit123;'
)

#---------------------------------------------------------------------------------------------------------------------
# Connect to database for Testing
#cursor = coon.cursor()
#cursor.execute("SELECT [ProductCategoryID],[Name CategoryID]'
                          #From [Rikit_View] ORDER BY ProductCategoryID')
#row = cursor.fetchone()
#while row:
#print(row)
#row = cursor.fetchone()
#cursor.close()
#conn.close()
#-----------------------------------------------------------------------------------------------------------------
cursor = conn.cursor() #Build the dataset into a cursor

#Build the window
root = Tk()
USER_INP = 0
#USER_INP2 = ""

#THE TITLE Of THE WINDOW
root.title("Rikit Database Program")


#Size of the window
root.geometry("600x600")
root.configure(background="white")
root.attributes()


#center-window --- depending of this screen this may have to be changed
root.eval('tk::PlaceWindow . center')

#----------------------------------------------------------------------------------------------------------------
#Creating the combobox --Define the category option that will be  populated by the combobox
def Cat_opt():
    print(USER_INP)

#label for the combo box
    label1 = ttk.Label(text="Select Category Id to Change", font=("Calibri", 16 ,"bold"))
    label1.place(x=100, y=75)
    label1.config(foreground="Red")


#GET DATA FOR THE COMBOBOX FROM VIEW -- TESTED UNIQUE VALUES ONLY
    query = cursor.execute('SELECT [ProductCategoryID], [Name]'
    'From [Rikit_View1] ORDER BY ProductCategoryID')
    data = []
    for row in cursor.fetchall():
#row 0 is the first in column of the Array where values are going to be displayed
        data.append(row[0])
    return data
    print(USER_INP)

#-----------------------------------------------------------------------------------------------------------------------
# Set the Combo Box
Category_box=Combobox(width=30)
Category_box.columnconfigure

Category_box['value'] = Cat_opt()
Category_box.place(x=100, y=100)
Category_box.current(0)
#Display selection in the combo box to user

def display_selection():

    # Get the Selected value
    Selection = int(Category_box.get())
    print(Selection)

    cursor = conn.cursor()

    # SHOW VALUE OF SELECTED CATEGORY
    messagebox.showinfo(
        message=f"The category you have selected is: {Selection}",
        title="Selection"
    )
    print(Selection)
#-----------------------------------------------------------------------------------------------------------------------
    # ADD USER INPUT FOR THE INCREASE IN PERCENTAGE
    # TAKE INTO ACCOUNT THE VARIABLE IS STRING AND NEEDS TO BE CHANGED
    # FLOAT AND CREATE THE CALCULATION FOR THE SP TO ACCEPT

    USER_INP = simpledialog.askstring(title="PERCENTAGE TO INCREASE",
                                      prompt="Please enter a percentage to increase the values: ")
    # print(USER_INP)
    messagebox.showinfo("% ENTERED", "VALUE AMOUNT TO BE CHANGED %s" % USER_INP + "%")
    USER_INP = (float(USER_INP) / 100) + 1
    # print(USER_INP)
    USER_INP = "{:.3f}".format(USER_INP)
    print(USER_INP)
    params = (Selection, float(USER_INP))
    print(params)
    selection = params
    print(Selection)
#-----------------------------------------------------------------------------------------------------------------------
#PREPARE THE STORED PROCEDURE EXECUTION SCRIPT AND PARAMETER VALUES
    cursor=conn.cursor()
#SET STORED PROCEDURE WITH REQUIRED PARAMS IN REQUIRED VALUE AT
    storedProc = "exec PythonProject @ProductCategoryID = ?, @Percent = ?"
#EXECUTE STORED PROCEDURE WITH PARAMETERS
    cursor.execute(storedProc, params)
#CALL commit() METHOD TO SAVE CHANGED TO THE DATABASE
    conn.commit()

#-----------------------------------------------------------------------------------------------------------------------
#BUTTON TO SHOW VALUE
button = ttk.Button(text="SELECT CATEGORY",command=display_selection)
button.place(x=100, y=200)


#-----------------------------------------------------------------------------------------------------------------------
root.mainloop()