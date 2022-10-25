from cProfile import label
import psycopg2
from tkinter import *
from tkinter import messagebox 
import ast
from traceback import format_exc
from turtle import heading

window=Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)

#########################Baza#############################
def signup():
    username=user.get()
    password=code.get()
    conform_password=conform_code.get()
    
    if password==conform_password:
        try:
            con = psycopg2.connect(database="signupdata",
                        user='postgres',
                        password='20032011',
                        host='localhost',
                        port= '5432')
            cur=con.cursor()
            cur.execute("""create table if not exists users(username text,
                                                        password text)""")
            cur.execute(f"""insert into users values ('{username}','{password}')""")
            con.commit()
            con.close()

#    if password==conform_password:
 #       try:
 #           file=open('datasheet.txt','r+')
 #           d=file.read()
 #           r=ast.literal_eval(d)

 #           dict2={username:password}
#            r.update(dict2)
#            file.truncate(0)
#           file.close()

#           file=open('datasheet.txt','w')
#           w=file.write(str(r))

            messagebox.showinfo('Signup',"Tabriklaymiz,siz omadli ro'yhatdan o'tdingiz!")

        except:
            file=open('datasheet.txt','w')
            pp=str({'Username':'password'})
            file.write(pp)
            file.close()

    else:
        messagebox.showerror('Invalid',"Ikkala parol ham mos bo'lishi kerak!")

##############################IMAGE##################################
img = PhotoImage(file='login.png')
Label(window,image=img,border=0,bg='white').place(x=50,y=90)

frame=Frame(window,width=350,height=390,bg='#fff')
frame.place(x=480,y=50)

heading=Label(frame,text='Sign up',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)

#############################FUNKSIYALAR###############################

#############################FUNKSIYA 1###############################
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    if code.get()=='':
        code.insert(0,'Password')

code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#############################FUNKSIYA 2###############################
def on_enter(e):
    conform_code.delete(0,'end')
def on_leave(e):
    if conform_code.get()=='':
        conform_code.insert(0,'Conform Password')

conform_code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
conform_code.place(x=30,y=220)
conform_code.insert(0, 'Conform Password')
conform_code.bind("<FocusIn>", on_enter)
conform_code.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

#############################FUNKSIYA 3###############################
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#############################BUTTON & LABEL###############################

Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
label=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=90,y=340)

signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8')
signin.place(x=200,y=340)



window.mainloop()