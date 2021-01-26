import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from datetime import *


mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='lifechoicesonline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


#sign in button
def verify():
    users = Username.get()
    passs = Password.get()
    sql = "select * from users where username = %s and password = %s"
    mycursor.execute(sql, [(users), (passs)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

#if log in details correct
def logged():
    #capture date and time
    d = datetime.now()
    dmy = d.strftime("%d/%m/%y")
    t = d.strftime("%H:%M")
    messagebox.showinfo('info', "You have successfully logged in")
    Username.delete(0, END)
    Password.delete(0, END)
    #open a new window
    outW = Tk()
    outW.title("login")
    outW.geometry("400x200")
    outW.configure(background="#346ab3")

    #function to print date time when logged out
    def out():
        d2 = datetime.now()
        t2 = d2.strftime("%H:%M")
        infoU2 = Username.get(), dmy, t, t2
        uCom2 = "INSERT INTO register(name, date, logged_in, logged_out) VALUES(%s,%s,%s,%s)"

        mycursor.execute(uCom2, infoU2)
        mydb.commit()
        messagebox.showinfo('info', "You have successfully logged out")
        outW.destroy()

    btnOut = Button(outW, text="sign out", command=out, bg="white")
    lglb =Label(outW, text="life choices", bg="#346ab3")
    lglb.place(x=177, y=80)
    btnOut.place(x=177, y=100)
    outW.mainloop()
    root.destroy()


# if login details are incorrect
def failed():
    messagebox.showinfo("Error", "try again")
    Username.delete(0, END)
    Password.delete(0, END)

#to register user
def reg():
    #open new window
    window = Tk()
    window.title("register")
    window.configure(background="#346ab3")
    window.geometry("200x200")
    unlb = Label(window, text="Name:", bg="#346ab3")
    ussrlb = Label(window, text="Username:", bg="#346ab3")
    psslb = Label(window, text="Password:", bg="#346ab3")
    un = Entry(window)
    usEnt = Entry(window)
    pssEnt = Entry(window)

    #capture data and place it into users table
    def parseUser():
        infoU = un.get(), usEnt.get(), pssEnt.get()
        uCom = "INSERT INTO users(full_name, username, password) VALUES(%s,%s,%s)"

        mycursor.execute(uCom, infoU)
        mydb.commit()
        messagebox.showinfo('info', "register successful")
        window.destroy()

    regBtn = Button(window, text="register", command=parseUser, bg="white")
    unlb.pack()
    un.pack()
    ussrlb.pack()
    usEnt.pack()
    psslb.pack()
    pssEnt.pack()
    regBtn.pack()
    window.mainloop()


def adminlog():
    #create new window
    root.destroy()
    tab = Tk()
    tab.title("admin")
    tab.configure(background="#346ab3")
    tab.geometry("200x200")
    ussrlb = Label(tab, text="admin-Username:", bg="#346ab3")
    usEnt = Entry(tab)
    psslb = Label(tab, text="Password", bg="#346ab3")
    pssEnt = Entry(tab)

    #capture data and put it into admin table
    def parseadmin():
        infoU = usEnt.get(), pssEnt.get()
        uCom = "INSERT INTO admin(username, password) VALUES(%s,%s)"

        mycursor.execute(uCom, infoU)
        mydb.commit()
        messagebox.showinfo('info', "there you go")

    btnadm=Button(tab, text="create admin", command=parseadmin, bg="white")

    #verify if user name and password work together
    def admin_user():
        myuser = usEnt.get()
        pas = pssEnt.get()
        sql = "select * from admin where username = %s and password = %s"
        mycursor.execute(sql, [(myuser), (pas)])
        results = mycursor.fetchall()
        if results:
            tab.withdraw()
            import myadmin
            myadmin()

        else:
            messagebox.showinfo("INFO", "incorrect username or password")
            usEnt.delete(0, END)
            pssEnt.delete(0, END)

    lgbtnad = Button(tab, text="sign in", command=admin_user, bg="white")
    ussrlb.pack()
    usEnt.pack()
    psslb.pack()
    pssEnt.pack()
    lgbtnad.pack()
    btnadm.pack()


# Design the login form
root = tk.Tk()
root.geometry("460x400")
root.title("Login Page")
root.configure(background="#346ab3")
photo = PhotoImage(file="image//banner.png")
img = Label(root, image=photo)
img.place(x=0, y=0)
lbluser = tk.Label(root, text="USERNAME:", bg="#346ab3" )
lbluser.place(x=177, y=150)
Username = tk.Entry(root, width=80)
Username.place(x=170, y=170, width=100)
lblpassword = tk.Label(root, text="PASSWORD :", bg="#346ab3")
lblpassword.place(x=177, y=210)
Password = tk.Entry(root, width=80)
Password.place(x=170, y=230, width=100)
Loginbtn = tk.Button(root, text="sign in", bg='white', command=verify)
Loginbtn.place(x=187, y=260, width=60)
Registerbtn = tk.Button(root, text="Register new user", bg='white', command=reg)
Registerbtn.place(x=150, y=300, width=150)
adminbtn = Button(root, text="admin", bg="white", command=adminlog)
adminbtn.place(x=189, y=340, width=55)

root.mainloop()
