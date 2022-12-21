from PIL import Image
from tkinter import *  # whole tkinter
from tkinter import ttk  # widgets and attributes
from tkinter import messagebox  # windows prompt dialogue box
import pymysql  # connector
import string  # token gen use
import secrets  # special randomiser
import customtkinter as ct  # tkinter theme
import ssl  # service
import smtplib  # email service
import time  # for working with date and time
import random
import threading
from prettytable import PrettyTable  # formating table in terminal
from email.message import EmailMessage  # email service
from apscheduler.schedulers.background import BlockingScheduler  # scheduler
from simple_colors import *  # terminal print theme

# Setting the customtkinter's theme - system accessed
ct.set_appearance_mode("System")
# Setting the customtkinter's color theme
ct.set_default_color_theme("dark-blue")
img = Image.open("assets\\bg.png")


class App(ct.CTk):
    # Initialization
    def __init__(self):
        super().__init__()
        self.login()

# connect to the database
    def connectDB(self):
        global mycursor, con
        try:
            con = pymysql.connect(host="sql6.freesqldatabase.com", user="sql6584700",
                                  password="6qvANYE66Y", database="sql6584700",  port=3306)
            # con = pymysql.connect(host="localhost", user="root", password="lakshya5020")
            mycursor = con.cursor()
        except:
            messagebox.showerror(
                "Error", "Connection is not established. Try Aagin.")
            return

# query function for selecting all the fields in a table in the database
    def useTable(self):
        self.connectDB()
        # query = "GRANT ALL PRIVILEGES ON f_db.* TO 'sql6584700'@'%' identified by 'secret'"
        # mycursor.execute(query)
        query = 'use sql6584700'
        mycursor.execute(query)
        query = 'select * from data'
        mycursor.execute(query)

# get details of a account in the table to all specific variables
    def getAccount(self, var, varGet):
        global email, passw, user_name
        self.useTable()
        newVarGet = str(varGet)

        if var == "email":
            query = 'select * from data where email=%s'
            mycursor.execute(query, (newVarGet))

        if var == "username":
            query = 'select * from data where username=%s'
            mycursor.execute(query, (newVarGet))

        row = mycursor.fetchone()
        email = row[2]
        passw = row[3]
        user_name = row[1]

# get a formatted table from the online database to work locally
    def getData(self):
        global dbData, dbId, dbUsername, dbPassword, dbEmail, dbDate, dbTime
        self.useTable()

        query = 'select * from data'
        mycursor.execute(query)

        rows = mycursor.fetchall()
        dbData = list(rows)

        dbId = list()
        dbUsername = list()
        dbEmail = list()
        dbPassword = list()
        dbDate = list()
        dbTime = list()

        for i in dbData:
            dbId.append(i[0])
            dbUsername.append(i[1])
            dbEmail.append(i[2])
            dbPassword.append(i[3])
            dbDate.append(i[4])
            dbTime.append(i[5])

        dbTable = PrettyTable()
        col = ["id", "username", "email", "password", "date", "time"]
        dbTable.add_column(col[0], dbId)
        dbTable.add_column(col[1], dbUsername)
        dbTable.add_column(col[2], dbEmail)
        dbTable.add_column(col[3], dbPassword)
        dbTable.add_column(col[4], dbDate)
        dbTable.add_column(col[5], dbTime)

        print(f"\ndata table:\n{dbTable}")

# clear all the elements in the window # only elements
    def destroyWindow(self):
        for elements in self.winfo_children():
            elements.destroy()

# generate random 12 character token for changing password
    def tokenGen(self):
        global token
        chrs = string.ascii_letters + string.digits
        token = ''.join(secrets.choice(chrs) for i in range(12))

# title and geometry set
    def change_window_properties(self, title, sizeX, sizeY, positionX, positionY, changePositions):
        self.title(title)
        if changePositions == "y":
            self.geometry(f"{sizeX}x{sizeY}+{positionX}+{positionY}")
        else:
            self.geometry(f"{sizeX}x{sizeY}")

# redirect functionality for tkinter bug - label links
    def argumentFunc(self, function):
        if function == "login":  # * Send Mail Window
            self.login()
        if function == "register":  # * Login Window
            self.register()
        if function == "forgotPassword":  # * Token Window
            prompt = messagebox.askyesno(
                "Warning", "Are you sure you want to go back?\nThe provided token cannot be used again.", )
            if prompt:
                self.forgotPassword()

# clear the field if the default text is present when focused in
    def focusIn_clear(self, entryVar, text):
        if entryVar.get() == text:
            entryVar.delete(0, END)
        if passwordEntry.get() == "":
            passwordEntry.configure(show="*", font=("", 20, ""))
        if confirmPassEntry.get() == '':
            confirmPassEntry.configure(show="*", font=("", 20, ""))

# reset the fields to default if the focused without without entering anything
    def focusOut_reset_login(self, user, text):
        if user.get() == "":
            user.insert(0, text)
            user.configure(show="", font=("", 13, "bold"))

# reset all entries after registering an account
    def reset_fields(self):
        emailEntry.insert(0, "Enter Email")
        userNameEntry.insert(0, "Enter Username")
        passwordEntry.insert(0, "Enter Password")
        confirmPassEntry.insert(0, "Re-Enter Password")

# Heading creator in GUI
    def heading_label_auth(self, text, size, positionX, positionY):
        heading = ct.CTkLabel(self, text=text, font=('', size, 'bold'))
        heading.place(x=positionX, y=positionY)

# Every attribute and widgets creator in GUI
    def createElements(self, user, email, password, confirmPass, checkBox, btnText, jumpText, jumpX, jumpY):
        global userNameEntry, emailEntry, passwordEntry, confirmPassEntry, btn, tokenEntry, check
        X = 18  # * fixed x position for every entries in frame

        frame = ct.CTkFrame(self, width=235)
        frame.place(x=22, y=70)

        userNameEntry = ct.CTkEntry(
            frame, width=200, height=31, font=("", 13, 'bold'))
        userNameEntry.insert(0, "Enter Username")

        userNameEntry.bind('<FocusIn>', lambda event, a=userNameEntry,
                           b="Enter Username": self.focusIn_clear(a, b))
        userNameEntry.bind('<FocusOut>', lambda event, a=userNameEntry,
                           b="Enter Username": self.focusOut_reset_login(a, b))

        emailEntry = ct.CTkEntry(
            frame, width=200, height=31, font=("", 13, 'bold'))
        emailEntry.insert(0, "Enter Email")
        emailEntry.bind('<FocusIn>', lambda event, a=emailEntry,
                        b="Enter Email": self.focusIn_clear(a, b))
        emailEntry.bind('<FocusOut>', lambda event, a=emailEntry,
                        b="Enter Email":  self.focusOut_reset_login(a, b))

        passwordEntry = ct.CTkEntry(
            frame, width=200, height=31, font=("", 13, 'bold'))
        passwordEntry.insert(0, "Enter Password")

        passwordEntry.bind('<FocusIn>', lambda event, a=passwordEntry,
                           b="Enter Password": self.focusIn_clear(a, b))
        passwordEntry.bind('<FocusOut>', lambda event, a=passwordEntry,
                           b="Enter Password": self.focusOut_reset_login(a, b))

        confirmPassEntry = ct.CTkEntry(
            frame, width=200, height=31, font=("", 13, 'bold'))
        confirmPassEntry.insert(0, "Re-Enter Password")

        confirmPassEntry.bind('<FocusIn>', lambda event, a=confirmPassEntry,
                              b="Re-Enter Password": self.focusIn_clear(a, b))
        confirmPassEntry.bind('<FocusOut>', lambda event, a=confirmPassEntry,
                              b="Re-Enter Password": self.focusOut_reset_login(a, b))

        # btn = ct.CTkButton(frame, text=btnText, width=120)

        jumpLink = ct.CTkLabel(frame, text=jumpText)
        jumpLink.place(x=jumpX, y=jumpY)
        # jumpLink.bind('<Button-1>', self.register)

        if btnText == "Register":  # * Register Window
            userNameEntry.place(x=X, y=14)
            emailEntry.place(x=X, y=50)
            passwordEntry.place(x=X, y=86)
            confirmPassEntry.place(x=X, y=122)
            frame.configure(height=260)

            btn = ct.CTkButton(frame, text="Register", width=120)
            btn.place(x=53, y=188)
            btn.configure(command=self.registerAccount)
            check = IntVar()
            checkbox = ct.CTkCheckBox(frame,  text="Agreed to all Terms & Conditions", variable=check,
                                      cursor='hand2', checkbox_width=18, checkbox_height=18, corner_radius=38, border_width=3)
            checkbox.place(x=10, y=160)

            jumpLink.bind('<Button-1>', lambda event,
                          a="login": self.argumentFunc(a))

        if btnText == "Login":  # * Login Window
            userNameEntry.place(x=X, y=14)
            passwordEntry.place(x=X, y=50)

            btn = ct.CTkButton(frame, text=btnText, width=64)
            btn.configure(command=self.loginDatbase)
            btn.place(x=20, y=90)

            forgotBtn = ct.CTkButton(
                frame, text="Forgot Password", width=80, fg_color="transparent", bg_color="transparent")
            forgotBtn.configure(command=self.forgotPassword)
            forgotBtn.place(x=90, y=90)

            # forgotLabel = ct.CTkLabel(frame, text="Forgot Password")
            # forgotLabel.place(x=96, y=89)
            # forgotLabel.bind("<Button-1>", lambda event, a="forgotPassword": self.argumentFunc(a))

            jumpLink.bind("<Button-1>", lambda event,
                          a="register": self.argumentFunc(a))

        if btnText == "Send Link":  # * Forgot Window
            emailEntry.place(x=X, y=14)

            btn = ct.CTkButton(frame, text=btnText, width=95)
            btn.configure(command=self.sendMail)
            btn.place(x=68, y=53)

            jumpLink.bind("<Button-1>", lambda event,
                          a="login": self.argumentFunc(a))

        if btnText == "Verify Token":  # * Token Window
            tokenEntry = ct.CTkEntry(
                frame, width=200, height=31, font=("", 13, "bold"))
            tokenEntry.place(x=X, y=14)
            tokenEntry.insert(0, "Enter Token")
            tokenEntry.bind('<FocusIn>', lambda event, a=tokenEntry,
                            b="Enter Token": self.focusIn_clear(a, b))
            tokenEntry.bind('<FocusOut>', lambda event, a=tokenEntry,
                            b="Enter Token": self.focusOut_reset_login(a, b))

            btn = ct.CTkButton(frame, text=btnText, width=100)
            btn.configure(command=self.verifyToken)
            btn.place(x=65, y=53)

            jumpLink.bind('<Button-1>', lambda event,
                          a="forgotPassword": self.argumentFunc(a))

        if btnText == "Submit":  # * Change Password Window
            passwordEntry.place(x=X, y=14)
            confirmPassEntry.place(x=X, y=50)

            btn = ct.CTkButton(frame, text=btnText, width=64)
            btn.configure(command=self.updatePassword)
            btn.place(x=82, y=90)

            jumpLink.bind('<Button-1>', lambda event,
                          a="forgotPassword": self.argumentFunc(a))

# Register Account Functionality
    def registerAccount(self):
        if userNameEntry.get() == "" or passwordEntry.get() == "" or emailEntry.get() == "" or confirmPassEntry.get() == "" or userNameEntry.get() == "Enter Username" or passwordEntry.get() == "Enter Password" or confirmPassEntry.get() == "Re-Enter Password" or emailEntry.get() == 'Enter Email':
            messagebox.showerror("Error", "Please fill all the fields!")

        elif passwordEntry.get() != confirmPassEntry.get():
            messagebox.showerror("Error", "Passwords do not match!")

        elif check.get() == 0:
            messagebox.showerror("Error", "Please Accept Terms & Conditions")

        else:
            self.connectDB()
            try:
                query = 'use sql6584700'
                mycursor.execute(query)
                query = 'create table data(id int auto_increment primary key not null, username varchar(50), email varchar(100), password varchar(20), date varchar(30), time varchar(30))'
                mycursor.execute(query)
                messagebox.showinfo('Database', "added database")
            except:
                query = 'use sql6584700'
                mycursor.execute(query)

            query = 'select * from data where username=%s'
            mycursor.execute(query, (userNameEntry.get()))

            row = mycursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "Username already exists.")

            else:
                date = time.strftime('%d\%m\%Y')
                timeNow = time.strftime('%H:%M:%S')
                query = 'insert into data(username, email, password, date, time) values(%s,%s,%s,%s,%s)'
                mycursor.execute(query, (userNameEntry.get(
                ), emailEntry.get(), passwordEntry.get(), date, timeNow))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Account Added Successfully.")
                self.login()

# Register Account GUI
    def register(self):
        self.destroyWindow()
        self.change_window_properties(
            "Register Account", 280, 340, 0, 0, False)
        self.heading_label_auth("Register", 24, 91, 30)
        self.createElements(True, True, True, True, True,
                            "Register", "Have an account? Login", 47, 220)

# Change Password into current accountn functionality
    def updatePassword(self):
        if passwordEntry.get() == "" or confirmPassEntry.get() == "" or passwordEntry.get() == "Enter Password" or confirmPassEntry.get() == "Re-Enter Password":
            messagebox.showerror("Error", "All Fields are Required")
        else:
            try:
                self.useTable()
                query = 'select * from data where username=%s'
                mycursor.execute(query, (user_name))
                row = mycursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Username does not exist.")
                else:
                    query = 'update data set password=%s where username=%s'
                    mycursor.execute(query, (passwordEntry.get(), user_name))
                    con.commit()
                    con.close()
                    messagebox.showinfo(
                        "Success", "Password is reset.\nLogin with new password")
                    self.login()

            except:
                messagebox.showerror(
                    "Error", "Something went wrong. Please try again.")
                self.forgotPassword()

# Change Password GUI
    def changePassword(self):
        self.destroyWindow()
        self.title("Reset Password")
        self.heading_label_auth("Reset Your Password", 20, 37, 30)
        self.createElements(False, False, True, True, False,
                            "Submit", "Go Back", 90, 118)

# Verify Token Window Functionality
    def verifyToken(self):
        # try:
        #     messagebox.showinfo("Success", "Token ent. to change password.")
        if tokenEntry.get() == token:
            messagebox.showinfo(
                "Success", "Token entered successfully.\nProceed to change password.")
            self.changePassword()
        else:
            messagebox.showerror("Error", "Invalid Token")
        # except:
            messagebox.showerror(
                "Error", "Something went wrong. Please Try Again")

# Token Window GUI
    def verifyTokenWindow(self):
        self.destroyWindow()
        self.title("Token Window")
        self.heading_label_auth("Enter Token Password", 20, 35, 30)
        self.createElements(True, False, False, False, False,
                            "Verify Token", "Go Back", 90, 81)

# Online Email Sender Functionality - token sender online
    def sendMail(self):
        self.getAccount("email", emailEntry.get())
        self.tokenGen()

        try:
            email_sender = "lakshyaworkacc07@gmail.com"
            sender_password = "iwygigxwblwusylc"
            receiver_mail = str(emailEntry.get())
            # s = red(f'{token}', ['bold', 'underlined', 'italic'])
            subject = f"Token for resetting password for User: {user_name}"
            body = f"""You can reset your password with the help of the following token:\n \n{token} \n \nThis token will be expired within 10 minutes.\nYou can request for another token from the app."""

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = receiver_mail
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, sender_password)
                smtp.sendmail(email_sender, receiver_mail, em.as_string())
                messagebox.showinfo(
                    "Success", "TOken for password change sent to user email successfully.")
            self.verifyTokenWindow()
        except:
            messagebox.showerror("Error", "Failed to send email.")

# Forgot Window GUI - Send Mail GUI
    def forgotPassword(self):
        self.destroyWindow()
        self.title("Request Token")
        self.heading_label_auth("Reset Your Password", 20, 35, 30)
        self.createElements(False, True, False, False, False,
                            "Send Link", "Go Back To Login", 64, 80)

# Login Functionality
    def loginDatbase(self):
        if userNameEntry.get() == "" or passwordEntry.get() == "" or userNameEntry.get() == "Enter Username" or passwordEntry.get() == "Enter Password":
            messagebox.showerror("Error", "All Fields are required.")
        else:
            self.connectDB()

        self.useTable()

        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (userNameEntry.get(), passwordEntry.get()))

        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror("Error", "Username or password is incorrect.")
        else:
            messagebox.showinfo("Success", 'Login is successfull')
            loggedAccount_userName = str(userNameEntry.get())
            self.destroy()

# Creation of Login Window GUI
    def login(self):
        self.getData()
        self.destroyWindow()
        self.change_window_properties("Login", 280, 290, 750, 270, "y")
        self.resizable(False, False)
        self.heading_label_auth("User Login", 24, 77, 30)
        self.createElements(True, False, True, False, False,
                            "Login", "Create a New Account", 52, 133)


if __name__ == "__main__":
    app = App()
    app.mainloop()
