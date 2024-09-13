'''
Author      : Sirawit Charoenpanich
Student ID  : 1640702369
Subject     : CS403
Section     : -
Description : JJ SHOP
'''

import re
from ctypes import wstring_at
from email.mime import image
from msilib.schema import ComboBox
from sys import stdin
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor
from PIL import ImageTk, Image
import sqlite3
from tkinter.ttk import Combobox
from tkinter import ttk
window = Tk()
window.geometry('1000x800+100+100')
window.option_add('*font','Tahoma 18')
window.resizable(False, False)
window.title('JJ SHOP')

# config database path here!
db_path = 'data.db'

def init_registration(parent):
    page = Frame(parent, width=1000, height=800, bg='#454545')

    v_empid = StringVar()
    v_firstname = StringVar()
    v_lastname = StringVar()
    v_password = StringVar()
    v_birthdate = StringVar()
    v_cardno = StringVar()
    v_phoneno = StringVar()
    v_gender = StringVar()
    v_address = StringVar()
    Label(page, bg='#454545', fg='#CDC673', text= 'สมัครบัญชี', font='Garamond 26 bold').place(x=460, y=50)
    Label(page, bg='#454545', fg='white', text= 'ชื่อ', font='Garamond 18 bold').place(x=50, y=120)
    Label(page, bg='#454545', fg='white', text= 'ว/ด/ป เกิด', font='Garamond 18 bold').place(x=50, y=180)
    Label(page, bg='#454545', fg='white', text= 'เลขบัตรปชช', font='Garamond 18 bold').place(x=50, y=240)
    Label(page, bg='#454545', fg='white', text= 'เพศ', font='Garamond 18 bold').place(x=50, y=300)
    Label(page, bg='#454545', fg='white', text= 'สกุล', font='Garamond 18 bold').place(x=580, y=120)
    Label(page, bg='#454545', fg='white', text= 'ชื่อบัญชี', font='Garamond 18 bold').place(x=580, y=180)
    Label(page, bg='#454545', fg='white', text= 'รหัสผ่าน', font='Garamond 18 bold').place(x=580, y=240)
    Label(page, bg='#454545', fg='white', text= 'เบอร์โทร', font='Garamond 18 bold').place(x=580, y=300)
    Label(page, bg='#454545', fg='white', text= 'ที่อยู่', font='Garamond 18 bold').place(x=50, y=380)

    

    Entry(page, bg='#00FA9A',fg='black', textvariable=v_firstname).place(x=220, y=120)
    Entry(page, bg='#00FA9A',fg='black', textvariable=v_birthdate).place(x=220, y=180)
    Entry(page, bg='#00FA9A',fg='black', textvariable=v_cardno).place(x=220, y=240)
    Entry(page, bg='#00FA9A',fg='black', textvariable=v_gender).place(x=220, y=300)

    Entry(page, bg='#00FA9A',fg='black', textvariable=v_lastname).place(x=700, y=120)
    w_empid = Entry(page, bg='#00FA9A',fg='black', textvariable=v_empid)
    w_empid.place(x=700, y=180)
    w_empid.focus()
    Entry(page, bg='#00FA9A',fg='black', textvariable=v_password).place(x=700, y=240)
    Entry(page, bg='#00FA9A',fg='black', textvariable=v_phoneno).place(x=700, y=300)

    Entry(page, bg='#00FA9A',fg='black', textvariable=v_address).place(x=220, y=380)

    def register(empid,password,firstname,lastname,birthdate,cardnum,phoneno,gender,address):
        print(empid,password,firstname,lastname,birthdate,cardnum,phoneno,gender,address)

        if empid == '':
            messagebox.showwarning('Opps!', 'Employee ID could not be empty')
            return
        if password == '':
            messagebox.showwarning('Opps!', 'Password could not be empty')
            return
        if firstname == '':
            messagebox.showwarning('Opps!', 'First Name could not be empty')
            return
        if lastname == '':
            messagebox.showwarning('Opps!', 'Last Name could not be empty')
            return
        if birthdate == '':
            messagebox.showwarning('Opps!', 'birthdate could not be empty')
            return
        if cardnum == '':
            messagebox.showwarning('Opps!', 'cardnum could not be empty')
            return
        if gender == '':
            messagebox.showwarning('Opps!', 'gender could not be empty')
            return
        if phoneno == '':
            messagebox.showwarning('Opps!', 'phoneno could not be empty')
            return
        if address == '':
            messagebox.showwarning('Opps!', 'address could not be empty')
            return
        
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        curr = conn.cursor()

        select_sql = 'SELECT * FROM EMPLOYEEDATA WHERE EMP_ID = ?'
        curr.execute(select_sql, [empid])
        employee = curr.fetchone()
        if employee is not None:
            messagebox.showwarning('Opps!', f'{empid} has already registered')
            return

        sql = '''INSERT INTO EMPLOYEEDATA 
                (EMP_ID,PASSWORD,FNAME, LNAME,BIRTHDATE,CARDNUM,PHONENO,GENDER,ADDRESS)
                VALUES
                (?,?,?,?,?,?,?,?,?)'''
        curr.execute(sql, [empid,password,firstname,lastname,birthdate,cardnum,phoneno,gender,address])
        conn.commit()
        conn.close()

        messagebox.showinfo('Information', 'Thank you for registration')

        page.destroy()

    Button(page, bg='#BBFFFF', text='Register',font="Garamond 20 bold",borderwidth=3, relief="raised", command = lambda:
    register(v_empid.get(),v_password.get(), v_firstname.get(), v_lastname.get(),v_birthdate.get(), v_cardno.get(), v_phoneno.get(),v_gender.get(),v_address.get())).place(x=400, y=500)
    Button(page, bg='#CD5555', text='Cancel',font="Garamond 20 bold",borderwidth=3, relief="raised", command = lambda:page.destroy()).place(x=550, y=500)


    page.place(x=0, y=0)

def init_login(parent):
    page = Frame(parent, width=1000, height=800, bg='#454545')
    Label(page, image = img,bg='#454545').place(x=200, y=250)

    Label(page, bg='#454545', fg='#CDC673', text= 'บัญชีผู้เข้าใช้งาน', font="Petchlamoon 26 bold").place(x=400, y=80)
    Label(page, bg='#454545', fg='white', text= 'ชื่อบัญชี', font="Petchlamoon 22 bold").place(x=460, y=250)
    Label(page, bg='#454545', fg='white',text= 'รหัสผ่าน', font="Petchlamoon 22 bold").place(x=460, y=340)

    str_username = StringVar()
    str_password = StringVar()

    w_username = Entry(page, bg='#00FA9A',fg='black', textvariable=str_username)
    w_username.place(x=460, y=300)
    w_username.focus()

    Entry(page, bg='#00FA9A',fg='black', textvariable=str_password, show="*").place(x=460, y=400)

    def authenticate(empid, password):
        conn = sqlite3.connect(db_path)
        # conn.row_factory = sqlite3.Row  
        cursor = conn.cursor()
        sql = 'SELECT * FROM EMPLOYEEDATA WHERE EMP_ID = ? AND PASSWORD = ?'
        cursor.execute(sql, (empid, password))
        item = cursor.fetchone()
        conn.close()
        if item is not None:
            # open new form
            print('ok')
            employee = item
            employeereport_page = init_employeereport(parent=parent, emp_id = employee[0],item_id=item[0])
            employeereport_page.place(x=0, y=0)
        else :
            # message '
            messagebox.showerror(title='Unauthorized', message='Username or Password is invalid.')
    Button(page, bg='#BBFFFF', activebackground='#FF6A6A',text='Login',font="Garamond 20 bold",borderwidth=3, relief="raised",command = lambda:authenticate(str_username.get(), str_password.get())).place(x=460, y=440)
    Button(page, bg='#00FA9A', activebackground='#FF6A6A',text='Registration',font="Garamond 20 bold",borderwidth=3, relief="raised",command = lambda:init_registration(parent)).place(x=560, y=440)
    return page

def init_employeereport(parent, emp_id,item_id):
    page = Frame(parent, width=1000, height=800, bg='#454545')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    sql = 'SELECT * FROM EMPLOYEEDATA WHERE EMP_ID = ?'
    cursor.execute(sql, [emp_id])
    item = cursor.fetchone()
    conn.close()

    EMP_data = item
    

    Label(page, bg='#454545', image = img).place(x=30, y = 240)
    Label(page, bg='#454545',fg='white', text=f'ID',font="Garamond 18 bold").place(x=700, y=20)
    Label(page, bg='#454545',fg='white', text=f'Name',font="Garamond 18 bold").place(x=700, y=50)
    Label(page, bg='#454545',fg='white', text=f'Phoneno.',font="Garamond 18 bold").place(x=700, y=80)
    

    Label(page, bg='#FFFFE0', text=f'{EMP_data[0]}',font="Garamond 18 bold").place(x=810, y=20)
    Label(page, bg='#FFFFE0', text=f'{EMP_data[2]} {EMP_data[3]}',font="Garamond 18 bold").place(x=810, y=50)
    Label(page, bg='#FFFFE0', text=f'{EMP_data[6]}',font="Garamond 18 bold").place(x=810, y=80)

    Label(page, bg='#454545',fg='#CDC673', text=f'Check for Stock list.',font="Garamond 24 bold").place(x=300, y=80)
    Label(page, bg='#454545',fg='#CDC673', text=f'Check for Warranty.',font="Garamond 24 bold").place(x=300, y=200)
    Label(page, bg='#454545',fg='#CDC673', text=f'Open Customer Window For register.',font="Garamond 24 bold").place(x=300, y=320)
    Label(page, bg='#454545',fg='#CDC673', text=f'Open Supplier Window',font="Garamond 24 bold").place(x=300,y=450)
    Label(page, bg='#454545',fg='#CDC673', text=f'Open Shipping Information',font="Garamond 24 bold").place(x=300,y=560)

    Button(page, bg='#CD5555',activebackground='#FF6A6A', text='Log Out',font="Garamond 20 bold",borderwidth=3, relief="raised", command=lambda:init_login(parent).place(x=0, y=0)).place(x=850, y=700)
    Button(page, bg='#00CD66',activebackground='#FF6A6A', text='Edit Profile Page',font="Garamond 20 bold",borderwidth=3, relief="raised", command=lambda:editProfile(parent, EMP_data).place(x=0, y=0)).place(x=700, y=120)
    Button(page,bg='#96CDCD',activebackground='#FF6A6A', text='STOCK',font="Garamond 20 bold",borderwidth=3, relief="raised", command=lambda:openStockWindow(parent)).place(x=300, y=120)
    Button(page,bg='#96CDCD',activebackground='#FF6A6A', text='WARRANTY',font="Garamond 20 bold",borderwidth=3, relief="raised", command=lambda:openWarrantyWindow(parent)).place(x=300, y=245)
    Button(page,bg='#96CDCD',activebackground='#FF6A6A', text='CUSTOMER',font="Garamond 20 bold",borderwidth=3, relief="raised", command=lambda:openWindowCustomer(parent)).place(x=300, y=380)
    Button(page,bg='#96CDCD',activebackground='#FF6A6A', text='SUPPLIER',font="Garamond 20 bold",borderwidth=3, relief="raised", command=lambda:openWindowSupplier(parent)).place(x=300, y=500)
    Button(page,bg='#96CDCD',activebackground='#FF6A6A', text='SHIPPING',font="Garamond 20 bold",borderwidth=3, relief="raised", command=lambda:openWindowShipping(parent)).place(x=300, y=620)
    Button(page,bg='red',activebackground='#FF6A6A', text='SHOP',font="Garamond 20 bold",borderwidth=3, relief="raised", command=lambda:openShopWindow(parent)).place(x=300, y=700)
    return page

def editProfile(parent, EMP_data):
    page = Frame(parent, width=1000, height=800, bg='#808069')

    Label(page, bg='#808069', image = img).place(x=400, y = 0)
    
    Label(page, bg='#808069', fg='white',text=f'Employee ID',font="Garamond 18 bold").place(x=350, y=230)
    Label(page, bg='#808069', fg='white',text=f'First Name',font="Garamond 18 bold").place(x=350, y=280)
    Label(page, bg='#808069', fg='white',text=f'Last Name',font="Garamond 18 bold").place(x=350, y=330)
    Label(page, bg='#808069', fg='white',text=f'Phoneno',font="Garamond 18 bold").place(x=350, y=370)
    Label(page, bg='#808069', fg='white',text=f'Address',font="Garamond 18 bold").place(x=350, y=420)
    
    firstName = StringVar()
    lastName = StringVar()
    Phoneno = StringVar()
    Address = StringVar()

    firstName.set(EMP_data[2])
    lastName.set(EMP_data[3])
    Phoneno.set(EMP_data[6])
    Address.set(EMP_data[8])

    Label(page, bg='#D2B48C', text=f'{EMP_data[0]}',font="Garamond 18 bold").place(x=530, y=230)

    w_firstname = Entry(page,bg='#7EC0EE', textvariable=firstName,font="Garamond 18 bold")
    w_firstname.place(x=530, y=280)
    w_firstname.focus()

    Entry(page,bg='#7EC0EE', textvariable=lastName,font="Garamond 18 bold").place(x=530, y=330)
    Entry(page,bg='#7EC0EE', textvariable=Phoneno,font="Garamond 18 bold").place(x=530, y=375)
    Entry(page,bg='#7EC0EE', textvariable=Address,font="Garamond 18 bold").place(x=530, y=420)

    print(EMP_data)

    def updateProfile(parent, employeeId, firstName, lastName, phoneno, address):

        print(employeeId, firstName, lastName, phoneno,address)
        if firstName == '' :
            messagebox.showwarning(title='Please provide information',message='firstName could not be empty')
        if lastName == '' :
            messagebox.showwarning(title='Please provide information',message='lastName could not be empty')
        if phoneno == '' :
            messagebox.showwarning(title='Please provide information',message='phoneno could not be empty')
            return
        if address == '' :
            messagebox.showwarning(title='Please provide information',message='address could not be empty')
            return
        conn = sqlite3.connect(db_path)
        curr = conn.cursor()

        select_sql = 'SELECT * FROM EMPLOYEEDATA WHERE EMP_ID = ? AND FNAME = ? AND LNAME =? AND PHONENO =? AND ADDRESS =?'

        curr.execute(select_sql,[employeeId,firstName,lastName,phoneno,address])

        #set result as row object
        curr.row_factory = sqlite3.Row

        person = curr.fetchone()


        update_sql = 'UPDATE EMPLOYEEDATA SET FNAME = ? , LNAME =? , PHONENO =? ,ADDRESS =? where EMP_ID =?'

        curr.execute(update_sql,[firstName,lastName,phoneno,address,employeeId])
        conn.commit()

        affected_row = curr.rowcount


        conn.close()
        
        if affected_row > 0:
            messagebox.showinfo(title='Updating Information',message='Update Successfully')
        else:
            messagebox.showwarning(title='Updating Information',message='No row changed')
        
        page.destroy()
        employeereport_page = init_employeereport(parent=parent, emp_id = employeeId,item_id=employeeId)
        employeereport_page.place(x=0, y=0)

    Button(page, bg='#00FA9A',activebackground='#FF6A6A', text='Update',font="Garamond 20 bold",borderwidth=3, relief="raised", command=lambda:updateProfile(parent, EMP_data[0], firstName.get(), lastName.get(), Phoneno.get(),Address.get())).place(x=400, y=500)
    Button(page, bg='#CD5555',activebackground='#FF6A6A', text='Cancel',font="Garamond 20 bold",borderwidth=3, relief="raised", command=lambda:page.destroy()).place(x=550, y=500)

    return page


def openStockWindow(parent):
    # Create the select window
    global items
    selectWindow = Toplevel(parent)
    selectWindow.title("STOCK")
    selectWindow.geometry('1000x800')
    selectWindow.configure(bg='#548B54')
    # Create the style object and customize the appearance
    style = ttk.Style(selectWindow)
    style.configure("Treeview", background="gray")
    style.map("Treeview", background=[("selected", "red")])
    
 
    # Connect to the database and execute the query
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()    
    sql = 'SELECT * FROM STOCKDATA'
    cursor.execute(sql)
    
    items = cursor.fetchall()
    
    # Close the database connection
    conn.close()
    
    # Create the treeview with four columns
    tree = ttk.Treeview(selectWindow, columns=("item_id", "name", "quantity", "price"), show="headings")
 
    # Add column headings
    tree.heading("item_id", text="รหัสสินค้า")
    tree.heading("name", text="ชื่อสินค้า")
    tree.heading("quantity", text="จำนวน")
    tree.heading("price", text="ราคาต่อหน่วย")

    # Add data to the treeview
    for item in items:
        tree.insert("", "end", values=(item[0], item[1], item[2], item[3]))
    scrollbar = ttk.Scrollbar(selectWindow, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    # Pack the treeview
    TitleLabel = Label(selectWindow,bg='#548B54',fg='#CDC673', text="STOCK",font="Garamond 30 bold")
    TitleLabel.pack(side=TOP ,padx=10,pady=20)
    tree.pack(side=TOP,pady=150)
      # Create the search bar and button
    
    



    def performSearch():
        # Clear the treeview
        tree.delete(*tree.get_children())

        # Connect to the database and execute the query
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql = 'SELECT * FROM STOCKDATA WHERE ITEM_NAME like ?'
        data = ('%' + searchEntry.get() + '%',)
        cursor.execute(sql, data)

        items = cursor.fetchall()

        # Close the database connection
        conn.close()
         # Add data to the treeview
        for item in items:
            tree.insert("", "end", values=(item[0], item[1], item[2], item[3]))


    def addItem():
        # Open a new window to add an item
        newItemWindow = Toplevel(selectWindow)
        newItemWindow.title("Add New Item")
        newItemWindow.geometry('300x300')

        # Create the style object and customize the appearance
        style = ttk.Style(newItemWindow)
        style.configure("Treeview", background="#548B54")
        style.map("Treeview", background=[("selected", "red")])
    

        # Create the input fields for the new item data
        nameLabel = Label(newItemWindow, text="Name:",font="Garamond 24 bold")
        nameLabel.pack()
        nameEntry = Entry(newItemWindow,bg='#7EC0EE')
        nameEntry.pack()

        quantityLabel = Label(newItemWindow, text="Quantity:",font="Garamond 24 bold")
        quantityLabel.pack()
        quantityEntry = Entry(newItemWindow,bg='#7EC0EE')
        quantityEntry.pack()

        priceLabel = Label(newItemWindow, text="Price:",font="Garamond 24 bold")
        priceLabel.pack()
        priceEntry = Entry(newItemWindow,bg='#7EC0EE')
        priceEntry.pack()
        
        def addNewItem():
            # Check if the name entry field is empty
            if not nameEntry.get():
                messagebox.showerror("Error", "Name cannot be empty.")
                return

            # Validate the input for quantity and price
            try:
                quantity = int(quantityEntry.get())
                price = float(priceEntry.get())
                if quantity < 0 or price < 0:
                    messagebox.showerror("Error", "Quantity and price cannot be negative.")
                    return
            except ValueError:
                messagebox.showerror("Error", "Invalid input for quantity or price.")
                return
            # Validate the input for quantity and price
            try:
                quantity = int(quantityEntry.get())
                price = float(priceEntry.get())
                if quantity < 0 or price < 0:
                    messagebox.showerror("Error", "Quantity and price cannot be negative.")
                    return
            except ValueError:
                messagebox.showerror("Error", "Invalid input for quantity or price.")
                return

            # Add the new item to the database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            sql = '''INSERT INTO STOCKDATA (ITEM_NAME, ITEM_AMT, ITEM_PRICE) VALUES (?, ?, ?)'''
            data = (nameEntry.get(), quantity, price)
            cursor.execute(sql, data)
            conn.commit()
            conn.close()

            # Add the new item to the treeview
            item_id = cursor.lastrowid
            tree.insert("", "end", values=(item_id, nameEntry.get(), quantity, price))


            # Create the "Add Item" button and bind the addNewItem function to it
        addButton = Button(newItemWindow,bg='#548B54',activebackground='#FF6A6A',text="Add Item",font="Garamond 20 bold",borderwidth=3, relief="raised", command=addNewItem)
        addButton.pack()

    def removeItem():
        # Remove the selected item from the database and treeview
        selection = tree.selection()
        for item in selection:
                item_id = tree.item(item)['values'][0]
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                sql = "DELETE FROM STOCKDATA WHERE ITEM_ID = ?"
                data = (item_id,)
                cursor.execute(sql, data)
                conn.commit()
                conn.close()
                tree.delete(item)
    def set_row_text():
            # Get the selected row
            selected_row = tree.selection()[0]
            
            # Get the value of the 1st column (Customer_id) of the selected row
            customer_id = tree.item(selected_row, "values")[0]
            
            # Get the new text from the Entry widget
            new_text = entry.get()
            
            # Set the text of the 4th column of the selected row
            tree.set(selected_row, 2, new_text)
            
            # Update the database with the new text
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("UPDATE STOCKDATA SET ITEM_AMT = ? WHERE ITEM_ID = ?", (new_text, customer_id))
            conn.commit()
            conn.close()




    # Create the "Add Item" button and bind the addItem function to it
    
    
    set_text_button = Button(selectWindow,bg='#96CDCD',activebackground='#FF6A6A',text="SET STOCK AMOUNT ",font="Garamond 15 bold",borderwidth=3, relief="raised", command=set_row_text)
    set_text_button.place(x=742,y=615)

            # Create an Entry widget
    entry = Entry(selectWindow,bg='#7EC0EE')
    entry.place(x=450,y=618)

    searchButton = Button(selectWindow,bg='#96CDCD',activebackground='#FF6A6A', text="Search",font="Garamond 20 bold",borderwidth=3, relief="raised", command=performSearch)
    searchButton.pack(side=RIGHT,pady=5,padx=10)

    searchEntry = Entry(selectWindow,bg='#7EC0EE')
    searchEntry.pack(side=RIGHT,padx=10)

    searchLabel = Label(selectWindow,bg='#548B54',text="Search Name:",font="Garamond 24 bold",)
    searchLabel.pack(side=RIGHT ,padx=10)
    
    addButton = Button(selectWindow,bg='#96CDCD',activebackground='#FF6A6A',text="Add Item",font="Garamond 20 bold",borderwidth=3, relief="raised", command=addItem)
    addButton.pack(side=LEFT,pady=10,padx=10)

    # Create the "Remove Item" button and bind the removeItem function to it
    removeButton = Button(selectWindow,bg='#CD5555',activebackground='#FF6A6A', text="Remove Item",font="Garamond 20 bold",borderwidth=3, relief="raised",command=removeItem)
    removeButton.pack(side=LEFT,pady=10,padx=10)


def openWarrantyWindow(parent):
    
    selectWindow2 = Toplevel(parent)
    selectWindow2.title("WARRANTY")
    selectWindow2.geometry('1000x800')
    selectWindow2.configure(bg='#548B54')
    # Create the style object and customize the appearance
    style = ttk.Style(selectWindow2)
    style.configure("Treeview", background="gray")
    style.map("Treeview", background=[("selected", "red")])
    
     # Connect to the database and execute the query
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()    
    sql = 'SELECT * FROM WARRANTYDATA'
    cursor.execute(sql)
    
    items = cursor.fetchall()
    
    # Close the database connection
    conn.close()
    
    # Create the treeview with four columns
    tree = ttk.Treeview(selectWindow2, columns=("item_id", "item_name", "item_type", "datestr","dateend","emp_id"), show="headings")
    
    # Add column headings
    tree.heading("item_id", text="รหัสสินค้า")
    tree.heading("item_name", text="ชื่อสินค้า")
    tree.heading("item_type", text="ประเภทสินค้า")
    tree.heading("datestr", text="วันที่เริ่มประกัน")
    tree.heading("dateend", text="วันที่สิ้นสุดประกัน")
    tree.heading("emp_id", text="Employee ID")
    
    # Add data to the treeview
    for item in items:
        tree.insert("", "end", values=(item[0], item[1], item[2], item[3], item[4], item[5]))
    scrollbar = ttk.Scrollbar(selectWindow2, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
     
    TitleLabel = Label(selectWindow2,bg='#548B54',fg='#CDC673',text="Warannty",font="Garamond 30 bold")
    TitleLabel.pack(side=TOP ,padx=20,pady=20)
    tree.pack(side=TOP,padx=10)

    def performSearch():
        # Clear the treeview
        tree.delete(*tree.get_children())

        # Connect to the database and execute the query
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql = 'SELECT * FROM WARRANTYDATA WHERE ITEM_ID like ?'
        data = ('%' + searchEntry.get() + '%',)
        cursor.execute(sql, data)

        items = cursor.fetchall()

        # Close the database connection
        conn.close()
         # Add data to the treeview
        for item in items:
            tree.insert("", "end", values=(item[0], item[1], item[2], item[3], item[4], item[5]))

    
    
    def addItem():
        # Open a new window to add an item
        newItemWindow = Toplevel(selectWindow2)
        newItemWindow.title("Add New Item")
        newItemWindow.geometry('300x600')

        # Create the style object and customize the appearance
        style = ttk.Style(newItemWindow)
        style.configure("Treeview", background="grey")
        style.map("Treeview", background=[("selected", "red")])
    

        # Create the input fields for the new item data
        nameLabel = Label(newItemWindow, text="ชื่อสินค้า:")
        nameLabel.pack()
        nameEntry = Entry(newItemWindow,bg='#7EC0EE')
        nameEntry.pack()

        typeLabel = Label(newItemWindow, text="ประเภทสินค้า:")
        typeLabel.pack()
        typeEntry = Entry(newItemWindow,bg='#7EC0EE')
        typeEntry.pack()

        datestrLabel = Label(newItemWindow, text="วันที่เริ่มประกัน (dd/mm/yy):")
        datestrLabel.pack()
        datestrEntry = Entry(newItemWindow, bg='#7EC0EE')
        datestrEntry.pack()

        dateendLabel = Label(newItemWindow, text="วันที่สิ้นสุด (dd/mm/yy):")
        dateendLabel.pack()
        dateendEntry = Entry(newItemWindow,bg='#7EC0EE')
        dateendEntry.pack()

        empidLabel = Label(newItemWindow, text="EMP_ID:")
        empidLabel.pack()
        empidEntry = Entry(newItemWindow,bg='#7EC0EE')
        empidEntry.pack()
        

        def addNewItem():
            # Get the data entered by the user
            item_name = nameEntry.get()
            item_type = typeEntry.get()
            date_start = datestrEntry.get()
            date_end = dateendEntry.get()
            emp_id = empidEntry.get()
            # Validate the input
            if not nameEntry.get():
                messagebox.showerror("Error", "Name cannot be empty.")
                return
            if not typeEntry.get().isalpha():
                messagebox.showerror("Error", "Type can only contain alphabetic characters.")
                return
            # Validate the start and end dates
            if not validate_date(datestrEntry.get()):
                messagebox.showerror("Error", "Please enter a valid start date in the format XX/XX/XX")
                return

            if not validate_date(dateendEntry.get()):
                messagebox.showerror("Error", "Please enter a valid end date in the format XX/XX/XX")
                return
            
            # Check if EMP_ID is empty
            if empidEntry.get() == "":
                messagebox.showerror("Error", "EMP_ID cannot be empty")
                return
            
            # Check if all the required fields are filled
            if not item_name or not item_type or not date_start or not date_end or not emp_id:
                messagebox.showerror("Error", "Please fill in all the required fields")
                return

            # Check if the entered emp_id exists in the EMPLOYEE table
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT emp_id FROM EMPLOYEEDATA")
            emp_ids = cursor.fetchall()
            if (emp_id,) not in emp_ids:
                messagebox.showerror("Error", f"EMP_ID {emp_id} does not exist in the EMPLOYEE table")
                conn.close()
                return

            # Add the new item to the database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            sql = '''INSERT INTO WARRANTYDATA ( ITEM_NAME,ITEM_TYPE,DATE_START,DATE_END,EMP_ID) VALUES ( ?, ?,?,?,?)'''
            data = (nameEntry.get(), typeEntry.get(), datestrEntry.get(), dateendEntry.get(), empidEntry.get())
            cursor.execute(sql, data)
            conn.commit()
            conn.close()

            # Add the new item to the treeview
            item_id = cursor.lastrowid
            tree.insert("", "end", values=(item_id, nameEntry.get(), typeEntry.get(), datestrEntry.get(), dateendEntry.get(), empidEntry.get()))

            # Close the new item window
            newItemWindow.destroy()

        # Create the "Add Item" button and bind the addNewItem function to it
        addButton = Button(newItemWindow,bg='#548B54',activebackground='#FF6A6A',text="Add Item",font="Garamond 20 bold",borderwidth=3, relief="raised",command=addNewItem)
        addButton.pack()
        
    def validate_date(date):
        # Use a regular expression to check if the date is in the format XX/XX/XX
        pattern = r'\d{2}/\d{2}/\d{2}'
        match = re.match(pattern, date)

        if not match:
            return False

        # Split the date into day, month, and year components
        day, month, year = date.split('/')

        # Check that the day, month, and year are valid
        if int(day) > 31 or int(month) > 12 or int(year) > 99:
            return False

        return True    

    def removeItem():
        # Remove the selected item from the database and treeview
        selection = tree.selection()
        for item in selection:
                item_id = tree.item(item)['values'][0]
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                sql = "DELETE FROM WARRANTYDATA WHERE ITEM_ID = ?"
                data = (item_id,)
                cursor.execute(sql, data)
                conn.commit()
                conn.close()
                tree.delete(item)


    # Create the "Add Item" button and bind the addItem function to it
    

    searchButton = Button(selectWindow2,bg='#96CDCD',activebackground='#FF6A6A', text="Search",font="Garamond 20 bold",borderwidth=3, relief="raised", command=performSearch)
    searchButton.pack(side = RIGHT,padx=10)

    searchEntry = Entry(selectWindow2,bg='#7EC0EE')
    searchEntry.pack(side=RIGHT,padx=10)

    searchLabel = Label(selectWindow2,bg='#548B54',text="Search รหัสสินค้า:",font="Garamond 24 bold",)
    searchLabel.pack(side=RIGHT ,padx=10)
    
    addButton = Button(selectWindow2,bg='#96CDCD',activebackground='#FF6A6A',text="Add Item",font="Garamond 20 bold",borderwidth=3, relief="raised", command=addItem)
    addButton.pack(side=LEFT,pady=10,padx=10)

    # Create the "Remove Item" button and bind the removeItem function to it
    removeButton = Button(selectWindow2,bg='#CD5555',activebackground='#FF6A6A', text="   Remove Item   ",font="Garamond 16 bold",borderwidth=5, relief="raised",command=removeItem)
    removeButton.pack(side=LEFT,pady=10,padx=10)


    
def openWindowCustomer(parent):
    
    selectWindow3 = Toplevel(parent)
    selectWindow3.title("WARRANTY")
    selectWindow3.geometry('1000x800')
    selectWindow3.configure(bg='#548B54')

    # Create the style object and customize the appearance
    style = ttk.Style(selectWindow3)
    style.configure("Treeview", background="gray")
    style.map("Treeview", background=[("selected", "red")])
    
     # Connect to the database and execute the query
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()    
    sql = 'SELECT * FROM CUSTOMERDATA'
    cursor.execute(sql)
    
    items = cursor.fetchall()
    
    # Close the database connection
    conn.close()
    
    # Create the treeview with four columns
    tree = ttk.Treeview(selectWindow3, columns=("Customer_id", "Customer_name", "Customer_ads", "Customer_phoneno"), show="headings")
    
    # Add column headings
    tree.heading("Customer_id", text="ชื่อผู้ใช้ลูกค้า")
    tree.heading("Customer_name", text="ชื่อ-สกุล")
    tree.heading("Customer_ads", text="ที่อยู่")
    tree.heading("Customer_phoneno", text="เบอร์โทรศัพท์")

    
    # Add data to the treeview
    for item in items:
        tree.insert("", "end", values=(item[0], item[1], item[2], item[3]))
    scrollbar = ttk.Scrollbar(selectWindow3, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    TitleLabel = Label(selectWindow3,bg='#548B54',fg='#CDC673', text="Customer",font="Garamond 30 bold")
    TitleLabel.pack(side=TOP ,padx=10,pady=20)
    tree.pack(side=TOP)

    def performSearch():
        # Clear the treeview
        tree.delete(*tree.get_children())

        # Connect to the database and execute the query
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql = 'SELECT * FROM CUSTOMERDATA WHERE CUS_NAME like ?'
        data = ('%' + searchEntry.get() + '%',)
        cursor.execute(sql, data)

        items = cursor.fetchall()

        # Close the database connection
        conn.close()
         # Add data to the treeview
        for item in items:
            tree.insert("", "end", values=(item[0], item[1], item[2], item[3], item[4], item[5]))

    
    
    def addItem():
        # Open a new window to add an item
        newItemWindow = Toplevel(selectWindow3)
        newItemWindow.title("Add New Item")
        newItemWindow.geometry('300x600')

        # Create the style object and customize the appearance
        style = ttk.Style(newItemWindow)
        style.configure("Treeview", background="gray")
        style.map("Treeview", background=[("selected", "red")])
    

        # Create the input fields for the new item data
        nameLabel = Label(newItemWindow, text="ชื่อ-สกุล:")
        nameLabel.pack()
        nameEntry = Entry(newItemWindow, bg='#7EC0EE')
        nameEntry.pack()

        addressLabel = Label(newItemWindow, text="ที่อยู่:")
        addressLabel.pack()
        addressEntry = Entry(newItemWindow,bg='#7EC0EE')
        addressEntry.pack()

        phonenostrLabel = Label(newItemWindow, text="เบอร์โทรศัพท์:")
        phonenostrLabel.pack()
        phonenostrEntry = Entry(newItemWindow,bg='#7EC0EE')
        phonenostrEntry.pack()


        def addNewItem():
            # Get the values from the input fields
            name = nameEntry.get()
            address = addressEntry.get()
            phoneno = phonenostrEntry.get()

            # Validate the name field
            if not name:
                messagebox.showerror("Error", "ชื่อ-สกุลต้องไม่ว่างเปล่า")
                return
            elif not name.isalpha():
                messagebox.showerror("Error", "ชื่อ-สกุลต้องเป็นตัวอักษรเท่านั้น")
                nameEntry.delete(0, END)
                return
            # Validate the address field
            address = addressEntry.get()
            if not address:
                messagebox.showerror("Error", "ที่อยู่ต้องไม่ว่างเปล่า")
                return
            # Validate phone number
            phone = phonenostrEntry.get()
            if not phone:
                messagebox.showerror("Error", "เบอร์โทรศัพท์ต้องไม่ว่างเปล่า")
                return

            if not phone.isdigit():
                messagebox.showerror("Error", "เบอร์โทรศัพท์ต้องเป็นตัวเลขเท่านั้น")
                phonenostrEntry.delete(0, END)
                return
            # Add the new item to the database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            sql = '''INSERT INTO CUSTOMERDATA ( CUS_NAME,CUS_ADDRESS,CUS_PHONENO) VALUES ( ?, ?,?)'''
            data = (nameEntry.get(), addressEntry.get(), phonenostrEntry.get())
            cursor.execute(sql, data)
            conn.commit()
            conn.close()

            # Add the new item to the treeview
            item_id = cursor.lastrowid
            tree.insert("", "end", values=(item_id, nameEntry.get(), addressEntry.get(), phonenostrEntry.get()))

            # Close the new item window
            newItemWindow.destroy()

        # Create the "Add Item" button and bind the addNewItem function to it
        addButton = Button(newItemWindow,bg='#548B54',activebackground='#FF6A6A',text="Add Item",font="Garamond 20 bold",borderwidth=3, relief="raised",command=addNewItem)
        addButton.pack()

    def removeItem():
        # Remove the selected item from the database and treeview
        selection = tree.selection()
        for item in selection:
                item_id = tree.item(item)['values'][0]
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                sql = "DELETE FROM CUSTOMERDATA WHERE CUS_ID = ?"
                data = (item_id,)
                cursor.execute(sql, data)
                conn.commit()
                conn.close()
                tree.delete(item)

    # Create the "Add Item" button and bind the addItem function to it
    

    searchButton = Button(selectWindow3,bg='#96CDCD',activebackground='#FF6A6A', text="Search",font="Garamond 20 bold",borderwidth=3, relief="raised",command=performSearch)
    searchButton.pack(side = RIGHT,padx=10)

    searchEntry = Entry(selectWindow3,bg='#7EC0EE')
    searchEntry.pack(side=RIGHT,padx=10)

    searchLabel = Label(selectWindow3,bg='#548B54',text="Search Customer:",font="Garamond 20 bold",)
    searchLabel.pack(side=RIGHT ,padx=10)
    
    addButton = Button(selectWindow3,bg='#96CDCD',activebackground='#FF6A6A',text="Add Customer",font="Garamond 16 bold",borderwidth=3, relief="raised", command=addItem)
    addButton.pack(side=LEFT,pady=10,padx=10)

    # Create the "Remove Item" button and bind the removeItem function to it
    removeButton = Button(selectWindow3,bg='#CD5555',activebackground='#FF6A6A', text="Remove Customer",font="Garamond 14 bold",borderwidth=3, relief="raised",command=removeItem)
    removeButton.pack(side=LEFT,pady=10,padx=10)


def openWindowSupplier(parent):
    
    selectWindow4 = Toplevel(parent)
    selectWindow4.title("SUPPLIER")
    selectWindow4.geometry('1000x800')
    selectWindow4.configure(bg='#548B54')

    # Create the style object and customize the appearance
    style = ttk.Style(selectWindow4)
    style.configure("Treeview", background="gray")
    style.map("Treeview", background=[("selected", "red")])
    
     # Connect to the database and execute the query
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()    
    sql = 'SELECT * FROM SUPPLIERDATA'
    cursor.execute(sql)
    
    items = cursor.fetchall()
    
    # Close the database connection
    conn.close()
    
    # Create the treeview with four columns
    tree = ttk.Treeview(selectWindow4, columns=("Supplier_id", "Supplier_type", "Supplier_name", "Supplier_contact"), show="headings")
    
    # Add column headings
    tree.heading("Supplier_id", text="ไอดีบริษัท")
    tree.heading("Supplier_type", text="ประเภทบริษัท/ตัวแทนจำหน่าย")
    tree.heading("Supplier_name", text="ชื่อบริษัท/ตัวแทนจำหน่าย")
    tree.heading("Supplier_contact", text="เบอร์โทรศัพท์ติดต่อ")

    
    # Add data to the treeview
    for item in items:
        tree.insert("", "end", values=(item[0], item[1], item[2], item[3]))
    scrollbar = ttk.Scrollbar(selectWindow4, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    TitleLabel = Label(selectWindow4,bg='#548B54',fg='#CDC673',text="Supplier",font="Garamond 30 bold")
    TitleLabel.pack(side=TOP ,padx=10,pady=20)
    tree.pack(side=TOP)
      # Create the search bar and button

    def performSearch():
        # Clear the treeview
        tree.delete(*tree.get_children())

        # Connect to the database and execute the query
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql = 'SELECT * FROM SUPPLIERDATA WHERE SUP_NAME like ?'
        data = ('%' + searchEntry.get() + '%',)
        cursor.execute(sql, data)

        items = cursor.fetchall()

        # Close the database connection
        conn.close()
         # Add data to the treeview
        for item in items:
            tree.insert("", "end", values=(item[0], item[1], item[2], item[3]))

    
    
    def addItem():
        # Open a new window to add an item
        newItemWindow = Toplevel(selectWindow4)
        newItemWindow.title("Add New Item")
        newItemWindow.geometry('300x600')
    

        # Create the input fields for the new item data
        typeLabel = Label(newItemWindow, text="ประเภท:")
        typeLabel.pack()
        typeEntry = Entry(newItemWindow,bg='#7EC0EE')
        typeEntry.pack()

        nameLabel = Label(newItemWindow, text="ชื่อบริษัท/ตัวแทนจำหน่าย:")
        nameLabel.pack()
        nameEntry = Entry(newItemWindow,bg='#7EC0EE')
        nameEntry.pack()

        contactstrLabel = Label(newItemWindow, text="ช่องทางการติดต่อ:")
        contactstrLabel.pack()
        contactstrEntry = Entry(newItemWindow,bg='#7EC0EE')
        contactstrEntry.pack()


        def addNewItem():
            # Validate the input fields
            if not typeEntry.get():
                messagebox.showerror("Error", "กรุณากรอกประเภท")
                return

            if not nameEntry.get():
                messagebox.showerror("Error", "กรุณากรอกชื่อบริษัท/ตัวแทนจำหน่าย")
                return

            if not contactstrEntry.get():
                messagebox.showerror("Error", "กรุณากรอกช่องทางการติดต่อ")
                return

            if not typeEntry.get().isalpha():
                messagebox.showerror("Error", "ประเภทต้องเป็นตัวอักษรเท่านั้น")
                return
            # Add the new item to the database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            sql = '''INSERT INTO SUPPLIERDATA (SUP_TYPE,SUP_NAME,SUP_CONTACT) VALUES ( ?, ?,?)'''
            data = (typeEntry.get(), nameEntry.get(), contactstrEntry.get())
            cursor.execute(sql, data)
            conn.commit()
            conn.close()

            # Add the new item to the treeview
            item_id = cursor.lastrowid
            tree.insert("", "end", values=(item_id, typeEntry.get(), nameEntry.get(), contactstrEntry.get()))

            # Close the new item window
            newItemWindow.destroy()

        # Create the "Add Item" button and bind the addNewItem function to it
        addButton = Button(newItemWindow,bg='#548B54',activebackground='#FF6A6A',text="Add Supplier",font="Garamond 20 bold",borderwidth=3, relief="raised", command=addNewItem)
        addButton.pack()

    def removeItem():
        # Remove the selected item from the database and treeview
        selection = tree.selection()
        for item in selection:
                item_id = tree.item(item)['values'][0]
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                sql = "DELETE FROM SUPPLIERDATA WHERE SUP_ID = ?"
                data = (item_id,)
                cursor.execute(sql, data)
                conn.commit()
                conn.close()
                tree.delete(item)

    # Create the "Add Item" button and bind the addItem function to it
    

    searchButton = Button(selectWindow4,bg='#96CDCD',activebackground='#FF6A6A', text="Search",font="Garamond 20 bold",borderwidth=3, relief="raised",command=performSearch)
    searchButton.pack(side = RIGHT,padx=10)

    searchEntry = Entry(selectWindow4,bg='#7EC0EE')
    searchEntry.pack(side=RIGHT,padx=10)

    searchLabel = Label(selectWindow4,bg='#548B54',text="Search Supplier:",font="Garamond 20 bold",)
    searchLabel.pack(side=RIGHT ,padx=10)
    
    addButton = Button(selectWindow4,bg='#96CDCD',activebackground='#FF6A6A',text="Add Supplier",font="Garamond 15 bold",borderwidth=3, relief="raised", command=addItem)
    addButton.pack(side=LEFT,pady=10,padx=10)

    # Create the "Remove Item" button and bind the removeItem function to it
    removeButton = Button(selectWindow4,bg='#CD5555',activebackground='#FF6A6A', text="Remove Supplier",font="Garamond 15 bold",borderwidth=3, relief="raised",command=removeItem)
    removeButton.pack(side=LEFT,pady=10,padx=10)


    
def openWindowShipping(parent):
    
    selectWindow5 = Toplevel(parent)
    selectWindow5.title("SHIPPING")
    selectWindow5.geometry('1200x800')
    selectWindow5.configure(bg='#548B54')

    # Create the style object and customize the appearance
    style = ttk.Style(selectWindow5)
    style.configure("Treeview", background="gray")
    style.map("Treeview", background=[("selected", "red")])
    
     # Connect to the database and execute the query
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()    
    sql = 'SELECT * FROM CUSTOMERDATA'
    cursor.execute(sql)
    
    items = cursor.fetchall()
    
    # Close the database connection
    conn.close()
    
    # Create the treeview with four columns
    tree = ttk.Treeview(selectWindow5, columns=("Customer_id", "Customer_name", "Customer_ads", "Customer_phoneno","Customer_ship","Customer_shipnum"), show="headings")
    
    # Add column headings
    tree.heading("Customer_id", text="ชื่อผู้ใช้ลูกค้า")
    tree.heading("Customer_name", text="ชื่อ-สกุล")
    tree.heading("Customer_ads", text="ที่อยู่")
    tree.heading("Customer_phoneno", text="เบอร์โทรศัพท์")
    tree.heading("Customer_ship", text="สถานะ")
    tree.heading("Customer_shipnum", text="เลขพัสดุ")

    
    # Add data to the treeview
    for item in items:
        tree.insert("", "end", values=(item[0], item[1], item[2], item[3],item[4],item[5]))
    scrollbar = ttk.Scrollbar(selectWindow5, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    TitleLabel = Label(selectWindow5,bg='#548B54',fg='#CDC673', text="Shipping",font="Garamond 30 bold")
    TitleLabel.pack(side=TOP ,padx=10,pady=20)
    tree.pack(side=TOP)
    # Define a function to set the text of the selected row in the treeview and update the database
    def set_row_text():
        # Get the selected row
        selected_row = tree.selection()[0]
        
        # Get the value of the 1st column (Customer_id) of the selected row
        customer_id = tree.item(selected_row, "values")[0]
        
        # Set the text of the 4th column of the selected row
        tree.set(selected_row, 4, "IN PROGRESS")
        
        # Update the database with the new text
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE CUSTOMERDATA SET CUS_SHIP = ? WHERE CUS_ID = ?", ("IN PROGRESS", customer_id))
        conn.commit()
        conn.close()

    # Create a button that calls the set_row_text() function
    set_text_button = Button(selectWindow5,bg='#96CDCD',activebackground='#FF6A6A', text="SET STATUS TO IN PROGRESS",font="Garamond 15 bold",borderwidth=3, relief="raised",command=set_row_text)
    set_text_button.pack(side=LEFT,pady=10,padx=10)
    def set_row_text2():
        # Get the selected row
        selected_row = tree.selection()[0]
        
        # Get the value of the 1st column (Customer_id) of the selected row
        customer_id = tree.item(selected_row, "values")[0]
        
        # Set the text of the 4th column of the selected row
        tree.set(selected_row, 4, "DONE")
        
        # Update the database with the new text
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE CUSTOMERDATA SET CUS_SHIP = ? WHERE CUS_ID = ?", ("DONE", customer_id))
        conn.commit()
        conn.close()

    # Create a button that calls the set_row_text() function
    set_text_button = Button(selectWindow5,bg='#96CDCD',activebackground='#FF6A6A', text="SET STATUS TO DONE",font="Garamond 15 bold",borderwidth=3, relief="raised", command=set_row_text2)
    set_text_button.pack(side=LEFT,pady=10,padx=10)
    def set_row_text():
        # Get the selected row
        selected_row = tree.selection()[0]
        
        # Get the value of the 1st column (Customer_id) of the selected row
        customer_id = tree.item(selected_row, "values")[0]
        
        # Get the new text from the Entry widget
        new_text = entry.get()
        
        # Set the text of the 4th column of the selected row
        tree.set(selected_row, 5, new_text)
        
        # Update the database with the new text
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE CUSTOMERDATA SET CUS_SHIPNUM = ? WHERE CUS_ID = ?", (new_text, customer_id))
        conn.commit()
        conn.close()

    set_text_button = Button(selectWindow5,bg='#96CDCD',activebackground='#FF6A6A',text="SET SHIPPING NUMBER ",font="Garamond 15 bold",borderwidth=3, relief="raised", command=set_row_text)
    set_text_button.pack(side=RIGHT,padx=10)

    # Create an Entry widget
    entry = Entry(selectWindow5,bg='#7EC0EE')
    entry.pack(side=RIGHT,padx=10)

def openShopWindow(parent):
    # Create the shop window
    global items
    shopWindow = Toplevel(parent)
    shopWindow.title("SHOP")
    shopWindow.geometry('1000x800')
    shopWindow.configure(bg='#D9D9D9')

    # Create the style object and customize the appearance
    style = ttk.Style(shopWindow)
    style.configure("Treeview", background="gray")
    style.map("Treeview", background=[("selected", "red")])

    # Connect to the database and execute the query
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = 'SELECT * FROM STOCKDATA'
    cursor.execute(sql)

    items = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Create the treeview with four columns
    tree = ttk.Treeview(shopWindow, columns=("item_id", "name", "quantity", "price"), show="headings")

    # Add column headings
    tree.heading("item_id", text="รหัสสินค้า")
    tree.heading("name", text="ชื่อสินค้า")
    tree.heading("quantity", text="จำนวน")
    tree.heading("price", text="ราคาต่อหน่วย")

    # Add data to the treeview
    for item in items:
        tree.insert("", "end", values=(item[0], item[1], item[2], item[3]))
    # Create a label for the customer selection
    customerLabel = Label(shopWindow, text="Select Customer:", font="Garamond 16 bold")
    customerLabel.pack(pady=20)

    # Create the customer combobox and populate it with data from the database
    customerBox = ttk.Combobox(shopWindow, state="readonly", font="Garamond 14")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = 'SELECT CUS_NAME FROM CUSTOMERDATA'
    cursor.execute(sql)
    customerData = cursor.fetchall()
    customers = [data[0] for data in customerData]
    customerBox['values'] = customers
    customerBox.pack(pady=10)

    # Create a label for the customer cart
    cartLabel = Label(shopWindow, text="Customer Cart:", font="Garamond 16 bold")
    cartLabel.pack(pady=20)

    # Create the customer cart treeview
    cartTree = ttk.Treeview(shopWindow, columns=("item_id", "name", "quantity", "price"), show="headings")
    cartTree.heading("item_id", text="รหัสสินค้า")
    cartTree.heading("name", text="ชื่อสินค้า")
    cartTree.heading("quantity", text="จำนวน")
    cartTree.heading("price", text="ราคาต่อหน่วย")

    # Create the "Add to Cart" button and bind the addToCart function to it
    def addToCart():
        selection = tree.selection()
        for item in selection:
            item_id = tree.item(item)['values'][0]
            name = tree.item(item)['values'][1]
            price = tree.item(item)['values'][3]
            stock = tree.item(item)['values'][2]
            quantity = 1
            # check if the selected item's stock is enough for the desired quantity
            if quantity <= stock:
                cartTree.insert("", "end", values=(item_id, name, quantity, price))
                # update the stock in the stock treeview
                tree.set(item, column=2, value=stock-quantity)
            else:
                messagebox.showerror("Error", f"Not enough stock for {name}")


    addButton = Button(shopWindow, text="Add to Cart", font="Garamond 16 bold", command=addToCart)
    addButton.pack(pady=10)

    # Create the "Remove from Cart" button and bind the removeFromCart function to it
    def removeFromCart():
        selection = cartTree.selection()
        for item in selection:
            cartTree.delete(item)

    removeButton = Button(shopWindow, text="Remove from Cart", font="Garamond 16 bold", command=removeFromCart)
    removeButton.pack(pady=10)

    # Pack the treeview and customer cart treeview
    tree.pack(side=LEFT, padx=10)
    cartTree.pack(side=LEFT, padx=10)

    # Create the checkout button and bind the checkout function to it
    def checkout():
        total_price = 0
        cart_items = []
        selection = cartTree.get_children()
        for item in selection:
            item_id = cartTree.item(item)['values'][0]
            name = cartTree.item(item)['values'][1]
            quantity = cartTree.item(item)['values'][2]
            price = cartTree.item(item)['values'][3]
            total_price += (quantity * price)
            cart_items.append((item_id, name, quantity, price))
            # Update the stock in the database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute('SELECT ITEM_AMT FROM STOCKDATA WHERE item_id = ?', (item_id,))
            current_quantity = cursor.fetchone()[0]
            new_quantity = current_quantity - quantity
            cursor.execute('UPDATE STOCKDATA SET ITEM_AMT = ? WHERE item_id = ?', (new_quantity, item_id))
            conn.commit()
            conn.close()
            # Remove the item from the cart
            cartTree.delete(item)
        
        # Get the selected customer name from the combobox
        customer_name = customerBox.get()

        # Show the total price and customer name in a message box
        messagebox.showinfo("Purchase Complete", f"Customer: {customer_name}\nTotal Price: {total_price} บาท")

    checkoutButton = Button(shopWindow, text="Checkout", font="Garamond 16 bold", command=checkout)
    checkoutButton.pack(pady=10)

        # Center the shop window on the screen
    shopWindow.update_idletasks()
    width = shopWindow.winfo_width()
    height = shopWindow.winfo_height()
    x = (shopWindow.winfo_screenwidth() // 2) - (width // 2)
    y = (shopWindow.winfo_screenheight() // 2) - (height // 2)
    shopWindow.geometry('{}x{}+{}+{}'.format(width, height, x, y))

img = PhotoImage(file='images/Logo.png').subsample(2)
fm_login = init_login(window)
fm_login.place(x=0, y=0)

window.mainloop()