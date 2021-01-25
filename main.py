from tkinter import *
import mysql.connector
from tkinter import messagebox as mb
import datetime
import os
import sys

#Connecting DB to python
mydb=mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                             host='localhost', database='lifechoicesonline',
                             auth_plugin='mysql_native_password')

mycursor=mydb.cursor()
mycursor.execute("create database if not exists lifechoicesonline")
mydb.commit()
mycursor.execute("use lifechoicesonline")
mydb.commit()
mycursor.execute("create table if not exists users(id integer(11) not null auto_increment, full_name varchar(60) default null, username varchar(50) default null, password varchar(20) default null,primary key(id))")
mydb.commit()
mycursor.execute("create table if not exists administration(full_name varchar(60) not null,username varchar(50) not null,password varchar(20) not null)")
mydb.commit()
mycursor.execute("create table if not exists logs(id integer(11) not null auto_increment,username varchar(50) default null,date varchar(20) not null,login_times varchar(50) not null,logout_times varchar(50) not null,primary key(id))")
mydb.commit()

#importing date and time
now = datetime.datetime.now()

#Registration window
def register():

    root.destroy()
    reg=Tk()
    reg.title("Registration")
    reg.geometry("400x250")
    reg.config(bg="blue")

    fullname=Label(reg,text="Enter Full Name",bg="black", fg="white")
    fullname.place(x=30,y=33)
    f_entry=Entry(reg,width=20)
    f_entry.place(x=165,y=30)

    username=Label(reg,text="Enter Username",bg="black", fg="white")
    username.place(x=30,y=93)
    user_entry=Entry(reg,width=20)
    user_entry.place(x=165,y=90)

    password=Label(reg,text="Enter Password",bg="black", fg="white")
    password.place(x=30,y=153)
    pass_entry=Entry(reg,width=20,show="*")
    pass_entry.place(x=165,y=150)

    #Sign up function
    def signup():
        fullname=f_entry.get()
        username=user_entry.get()
        password=pass_entry.get()

        if f_entry.get() == "" or user_entry.get() =="" or pass_entry.get() == "":
            mb.showerror("Error", "Please enter all the fields")

        else:
            sql="insert into users(full_name,username,password) values(%s,%s,%s) "
            mycursor.execute(sql,[(fullname),(username),(password)])
            mydb.commit()
            mb.showinfo("Success","You successfully registered")
            reg.destroy()


    sign_up=Button(reg, text="Register",command=signup)
    sign_up.place(x=30,y=200)
    def exit2():
        python = sys.executable
        os.execl(python, python, * sys.argv)
    extbtn=Button(reg, text="Return",command=exit2)
    extbtn.place(x=240,y=200)

#Admin window
def main1():
    main=Tk()
    main.title("Admin")
    main.geometry("480x440")
    main.config(bg="blue")


    #Insert Function
    def add():
        entry1=mainf_entry.get()
        entry2=m_userentry.get()
        entry3=m_pwdentry.get()

        if (entry1 ==''or entry2 =='' or entry3 ==''):
            mb.showerror("Error", "Empty Fields")

        else:
            sql="insert into users(full_name,username,password) values(%s,%s,%s) "
            mycursor.execute(sql,[(entry1),(entry2),(entry3)])
            mb.showinfo("Success","You successfully registered")
            mydb.commit()

    mainf_name=Label(main, text="Name",bg="black", fg="white")
    mainf_name.place(x=30,y=30)
    mainf_entry=Entry(main)
    mainf_entry.place(x=140,y=30)

    main_user=Label(main, text="Username",bg="black", fg="white")
    main_user.place(x=30,y=90)
    m_userentry=Entry(main)
    m_userentry.place(x=140,y=90)

    main_pwd=Label(main, text="Password",bg="black", fg="white")
    main_pwd.place(x=30,y=150)
    m_pwdentry=Entry(main)
    m_pwdentry.place(x=140,y=150)
    results=Listbox(main, width=52)
    results.place(x=30,y=200)

    #Selecting information
    def select():
        mycursor.execute('Select * from users')
        for i in mycursor:
            print(i)
            results.insert('end',str(i))
    #Deleting data
    def delete():
        a=m_userentry.get()

        if (m_userentry.get() ==""):
            mb.showwarning("Error","Empty Fields")
        else:
            sql="delete from users where username = %s "
            mycursor.execute(sql,[(a)])
            mydb.commit()
            mb.showinfo("Success","User Deleted")
    #Exit button
    def exit1():
        main.destroy()

    insertbtn=Button(main, text="Insert", width=10, command=add)
    insertbtn.place(x=340,y=28)
    selectbtn=Button(main, text="Search", width=10, command=select)
    selectbtn.place(x=340,y=88)
    deletebtn=Button(main, text="Delete", width=10, command=delete)
    deletebtn.place(x=340,y=148)
    exitbtn1=Button(main,text="Exit",command=exit1)
    exitbtn1.place(x=30,y=390)
#Admin login
def admin():
    root.destroy()
    root1=Tk()
    root1.title("Administration")
    root1.geometry("400x200")
    root1.config(bg="blue")

    lbladmin=Label(root1, text="Enter Username",bg="black", fg="white")
    lbladmin.place(x=30,y=30)
    admin_ent = Entry(root1)
    admin_ent.place(x=160,y=30)

    lbladmnpwd = Label(root1, text="Enter Password",bg="black", fg="white")
    lbladmnpwd.place(x=30,y=90)
    adminpwd_ent = Entry(root1)
    adminpwd_ent.place(x=160,y=90)
    def back():
        python = sys.executable
        os.execl(python, python, * sys.argv)
    returnbtn=Button(root1, text="Return",command=back)
    returnbtn.place(x=180,y=150)
    #Login function
    def adminlog():
        a_fulname=admin_ent.get()
        a_pwd=adminpwd_ent.get()

        sql="select * from administration where username = %s and password = %s"
        mycursor.execute(sql,[(a_fulname),(a_pwd)])
        data = mycursor.fetchall()

        if admin_ent.get() =='' or adminpwd_ent.get() == "":
            mb.showerror("Error","Please enter all the fields")

        else:
            if data:
                for i in data:
                    mb.showinfo("Successful","Welcome " + "" + admin_ent.get())
                    main1()
                    root1.destroy()
                    break

    admnbtn=Button(root1, text="Login", command=adminlog)
    admnbtn.place(x=70,y=150)
#Verifying users
def verify():
    users=entuser.get()
    passwords=entpassword.get()
    sql="select * from users where username = %s and password = %s"
    mycursor.execute(sql,[(users),(passwords)])
    results = mycursor.fetchall()

    x = datetime.datetime.now()
    l = x.strftime("%H:%M:%S")
    b = x.strftime("%d/%m/%y")

    if entuser.get() =="" or entpassword.get()=="":
        mb.showerror("Error","Empty Fields")

    else:

        if results:
            for i in results:
                mb.showinfo("Login Successful","Enjoy your day")
                root.destroy()

                sign_out_window = Tk()
                sign_out_window.title("Sign out")
                sign_out_window.geometry("200x200")

                def log_out():

                    t = datetime.datetime.now()
                    log_out = t.strftime("%H:%M:%S")
                    sql = "insert into logs(username,date,login_times,logout_times) values (%s,%s,%s,%s)"
                    mycursor.execute(sql,[(users),(b),(l),(log_out)])
                    mydb.commit()

                    mb.showinfo("Successful","Logged out")
                    sign_out_window.destroy()

                lgoutbtn=Button(sign_out_window, text="Sign Out",command=log_out)
                lgoutbtn.place(x=100,y=100)

                break
            else:
                mb.showerror("Login unsuccessful","Try again")

def exit():
    root.destroy()

#Login in interface
root =Tk()
root.title("Login")
root.geometry("400x400")
root.config(bg="blue")
root.bind("<Control-z>", lambda z: admin())

lbluser=Label(root, text="Username", bg="black", fg="white")
lbluser.place(x=30,y=33)
entuser=Entry(root, width=20)
entuser.place(x=140,y=30)

lblpassword=Label(root, text="Password", bg="black", fg="white")
lblpassword.place(x=30,y=103)
entpassword=Entry(root, width=20,show="*")
entpassword.place(x=140,y=100)
lgnbutton = Button(root, text='Login', width=8, command=verify)
lgnbutton.place(x=30,y=160)

lblframe=LabelFrame(root, text="Registration",bg="black", fg="white",padx=80,pady=20)
lblframe.place(x=47,y=220)
regbutton = Button(lblframe, text='Sign Up', width=10,font=("Arial","15","bold"),command=register)
regbutton.pack()

adminbtn=Button(root,text="Admin",width=8, command=admin)
adminbtn.place(x=30,y=350)

exitbtn=Button(root,text="Exit",width=8,command=exit)
exitbtn.place(x=270,y=350)

root.mainloop()



