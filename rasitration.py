import tkinter
import sqlite3
from tkinter import messagebox
db=sqlite3.connect('loginsystem.db')
db.execute('''  CREATE TABLE IF NOT EXISTS login(name text NOT NULL
    ,
    password TEXT PRIMARY KEY,
    mobilenumber integer NOT NULL
    );''')

print("database connected")

def signup():

    # insert data calling function
    def insertdata(name, password, mobilenumber):
        query = "INSERT INTO login(name,password,mobilenumber) VALUES (?,?,?) ;"
        db.execute(query, (name, password, mobilenumber,))
        db.commit()
        print("database  data inserted")

    def show():
        query = 'SELECT * FROM login;'
        #return db.execute(query)
        for rows in db.execute(query):
            print(rows)

    def save():
        username=userinput.get()
        password = passinput.get()
        mobile = mobileinput.get()
        insertdata(username,password,mobile)

    updte = tkinter.Tk()
    updte.title("SIGNUP SYSTEM")
    updte.geometry("600x400")
    updte.config(bg='yellow')

    padd = 20
    #root['padx'] = padd
    user_input = tkinter.StringVar()
    pass_input = tkinter.StringVar()

    info = tkinter.Label(updte, text='SIGNUP  ',bg='#1d1d1d',fg='#eeeeee',font="Verdana 30 ")
    info.grid(row=0, column=0, pady=20)
    info_user = tkinter.Label(updte, text='Username',bg='#1d1d1d',fg='#eeeeee',font="Verdana 15 ")
    info_user.grid(row=1, column=0)
    userinput = tkinter.Entry(updte, textvariable=user_input,font='Vardana',bg='#eeeeee')
    userinput.grid(row=1, column=1)

    info_pass = tkinter.Label(updte, text='password',bg='#1d1d1d',fg='#eeeeee',font="Verdana 15 ")
    info_pass.grid(row=2, column=0, pady=20)
    passinput = tkinter.Entry(updte, textvariable=pass_input,font='Vardana',bg='#eeeeee')
    passinput.grid(row=2, column=1)

    infomobile = tkinter.Label(updte, text='mobile number ',bg='#1d1d1d',fg='#eeeeee',font="Verdana 15 ")
    infomobile.grid(row=3,column=0)
    mobileinput = tkinter.Entry(updte,font='Vardana',bg='#eeeeee' )
    mobileinput.grid(row=3, column=1)

    save_btn = tkinter.Button(updte,text='save',command=save,highlightcolor='#000000',activebackground='#1d1d1d',border=0,bg='#000000',fg='#eeeeee')
    save_btn.grid(row=8, column=1)
    show_btn = tkinter.Button(updte, text='show', command=show,highlightcolor='#000000',activebackground='#1d1d1d',border=0,bg='#000000',fg='#eeeeee')
    show_btn.grid(row=8, column=2)
    updte.mainloop()

def forget():
    def updatedata1(mobilenumber, newpassword):
        query = "UPDATE login SET password=? where mobilenumber =?;"
        db.execute(query, (newpassword, mobilenumber))
        db.commit()
    def change():
        mobilenumber = userinput.get()
        password = passinput.get()
        updatedata1(mobilenumber,password)
        print(" successfully password chage ")
    updte = tkinter.Tk()
    updte.title("CHAGE PASSWORD")
    updte.geometry("750x400")
    updte.config(bg='orange')

    padd = 20
    # root['padx'] = padd
    user_input = tkinter.StringVar()
    pass_input = tkinter.StringVar()

    info = tkinter.Label(updte, text='CHANGE PASSWORD  ', bg='#1d1d1d', fg='#eeeeee', font="Verdana 30 ")
    info.grid(row=0, column=0, pady=20)
    info_user = tkinter.Label(updte, text='mobile number', bg='#1d1d1d', fg='#eeeeee', font="Verdana 15 ")
    info_user.grid(row=1, column=0)
    userinput = tkinter.Entry(updte, textvariable=user_input, font='Vardana', bg='#eeeeee')
    userinput.grid(row=1, column=1)

    info_pass = tkinter.Label(updte, text='password', bg='#1d1d1d', fg='#eeeeee', font="Verdana 15 ")
    info_pass.grid(row=2, column=0, pady=20)
    passinput = tkinter.Entry(updte, textvariable=pass_input, font='Vardana', bg='#eeeeee')
    passinput.grid(row=2, column=1)



    save_btn = tkinter.Button(updte, text='change password', command=change, highlightcolor='#000000', activebackground='#1d1d1d',
                              border=0, bg='#000000', fg='#eeeeee')
    save_btn.grid(row=8, column=1)

def log():

    cursor=db.cursor()
    cursor.execute("SELECT * FROM login where name=? AND password=? ",(user_input.get(),pass_input.get()))
    row=cursor.fetchone()

    if  row:
        messagebox.showinfo('info','login success')

    else:
        messagebox.showinfo('info','login faild')



root=tkinter.Tk()
root.title("LOGIN APP")
root.geometry('800x400')
root.resizable(False,False)
root.config(bg='greenyellow')
padd=20
root['padx']=padd
user_input=tkinter.StringVar()
pass_input=tkinter.StringVar()
info=tkinter.Label(root,text='LOGIN SYSTEM',bg='#1d1d1d',fg='#eeeeee',font="Verdana 30 ")
info.grid(row=0,column=0,pady=20)
info_user=tkinter.Label(root,text='Username',bg='#1d1d1d',fg='#eeeeee',font="Verdana 20 ")
info_user.grid(row=2,column=0)
userinput=tkinter.Entry(root,textvariable=user_input,font='Vardana',bg='#eeeeee')
userinput.grid(row=2,column=1)

info_pass=tkinter.Label(root,text='password',bg='#1d1d1d',fg='#eeeeee',font="Verdana 20")
info_pass.grid(row=3,column=0,pady=20)
passinput=tkinter.Entry(root,textvariable=pass_input,font='Vardana',bg='#eeeeee')
passinput.grid(row=3,column=1)


login_btn=tkinter.Button(text='login',command=log,highlightcolor='#000000',activebackground='#1d1d1d',border=0,)
login_btn.grid(row=4,column=1)

# signup
signup_btn=tkinter.Button(text='signup',command=signup,highlightcolor='#000000',activebackground='#1d1d1d',border=0,)
signup_btn.grid(row=4,column=2)

signup_btn=tkinter.Button(text='forget password',command=forget,highlightcolor='#000000',activebackground='#1d1d1d',border=0)
signup_btn.grid(row=4,column=4,padx=30)
root.mainloop()

