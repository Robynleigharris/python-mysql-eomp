from tkinter import *
from datetime import *
import mysql.connector

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='lifechoicesonline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

root = Tk()
root.geometry("700x500")
root.title("admin")
root.configure(background="#346ab3")
regLb = Label(root, text="Users:", bg="#346ab3")
regLi = Listbox(root, width=60)
tmLb = Label(root, text="Time:", bg="#346ab3")
tmLi = Listbox(root, width=60)


#pulls data from users and displays it in listbox
def regSh():
    u = "SELECT * FROM users"
    mycursor.execute(u)
    x = mycursor.fetchall()
    for i in x:
        regLi.insert(END, i)

#pulls data from register and displays it in listbox
def tmSho():
    u = "SELECT * FROM register"
    mycursor.execute(u)
    x = mycursor.fetchall()
    for i in x:
        tmLi.insert(END, i)

#takes user to main page
def back():
    root.destroy()
    import log
    log()

btnSh = Button(root, text="Show users", command=regSh, bg="white")
btntm = Button(root, text="Show register", command=tmSho, bg="white")
bckbtn = Button(root, text="back", command=back, bg="white")
regLb.pack()
regLi.pack()
tmLb.pack()
tmLi.pack()
btnSh.pack()
btntm.pack()
bckbtn.pack()
root.mainloop()

