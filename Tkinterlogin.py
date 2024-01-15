from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *

root=Tk()
root.title('Login-Page')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=user.get()
    password=Code.get()

    if username=='aadyaa' and password=='12345':
        screen=Toplevel(root)
        screen.title("Registration Form")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")
        heading=Label(screen,text='Registration Form', fg='#1CBFA8', bg='white',font=('Playfair Display', 23,'bold'))
        heading.place(x=180,y=50)
        menu=Menu(screen)
        screen.config(menu=menu)
        filemenu=Menu(menu)
        menu.add_cascade(label='File',menu=filemenu)
        filemenu.add_command(label='New')
        filemenu.add_command(label='Open')
        helpmenu=Menu(menu)
        menu.add_cascade(label='Help',menu=helpmenu)
        helpmenu.add_command(label='Help')
        helpmenu.add_command(label='About')
        frame=Frame(screen,width=600,height=800,bg="white")
        frame.place(x=100,y=100)
        frame2=Frame(screen,width=450,height=300,bg="white")
        frame2.place(x=450,y=100)
       
        a = Label(frame ,text = "First Name",font=('Playfair Display', 16)).grid(row =1,column = 0)
        b = Label(frame,text = "Last Name",font=('Playfair Display', 16)).grid(row = 2,column = 0)
        c = Label(frame ,text = "Email Id",font=('Playfair Display', 16)).grid(row = 3,column = 0)
        d = Label(frame,text = "Contact Number",font=('Playfair Display', 16)).grid(row =4 ,column = 0)
        v=IntVar()
        Radiobutton(frame,text='Male',variable=v,value=1,font=('Playfair Display', 16)).grid(row=5,column=0,sticky='w')
        Radiobutton(frame,text='Female',variable=v,value=2,font=('Playfair Display', 16)).grid(row=5,column=1,sticky='w')
        a1 = Entry(frame).grid(row = 1,column = 1, padx=10,pady=10)
        b1 = Entry(frame).grid(row = 2,column = 1, padx=10,pady=10)
        c1 = Entry(frame).grid(row = 3,column = 1, padx=10,pady=10)
        d1 = Entry(frame).grid(row = 4,column = 1, padx=10,pady=10)  
        chk_state = BooleanVar()
        chk_state.set(False)  
        checkbox =Checkbutton(frame, text="Would you like to receive emails and newsletter", variable=chk_state)
        checkbox.grid(row=6, columnspan=2, pady=20)

        age_label = Label(frame2, text="Age",font=('Playfair Display', 16))
        age_spinbox = Spinbox(frame2, from_=18, to=110)
        age_label.grid(row=2, column=0, padx=10,pady=10)
        age_spinbox.grid(row=2, column=1)
        nationality= Label(frame2, text="Nationality",font=('Playfair Display', 16))
        nationality_box = ttk.Combobox(frame2, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
        nationality.grid(row=3, column=0, padx=10,pady=10)
        nationality_box.grid(row=3, column=1)
        def pick_date(event):
            global cal,date_window

            date_window=Toplevel()
            date_window.grab_set()
            date_window.title('Select Date')
            date_window.geometry('250x220+690+370')
            cal=Calendar(date_window,selectmode="day",date_pattern="mm/dd/y")
            cal.grid(row=0,column=0)
            submit=Button(date_window,text="Submit",command=grab_date)
            submit.grid(row=1,column=0)
            
        def grab_date():
            dob_entry.delete(0,END)
            dob_entry.insert(0,cal.get_date())
            date_window.destroy()

        dob=Label(frame2,text='Date of Birth',font=('Playfair Display', 16),fg="black")
        dob.grid(row=4,column=0, padx=10,pady=10)
        dob_entry=Entry(frame2,highlightthickness=0, fg='black',font=('Playfair Display', 16),width=12)
        dob_entry.grid(row=4,column=1)
        dob_entry.insert(0,'dd/mm/yyyy')
        dob_entry.bind("<1>",pick_date)
        def submit():
            messagebox.showinfo("Submit", "Registration successful!")
      
        submit_button = Button(frame2, text="Submit", command=submit)
        submit_button.grid(row=5, column=0, columnspan=2, pady=10)     

    elif username!='aadyaa' and password!='12345':
        messagebox.showerror("Invalid","Invalid Username and Password")
    elif password!="12345":
        messagebox.showerror("Invalid","Invalid Password")
    elif username!='aadyaa':
        messagebox.showerror("Invalid","Invalid Username")

img=PhotoImage(file='login-bg.png')
Label(root,image=img,bg='white',width=350,height=350).place(x=80,y=50)

frame=Frame(root,width=400,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign In', fg='#1CBFA8', bg='white',font=('Playfair Display', 23,'bold'))
heading.place(x=120,y=5)
# 
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Lato', 11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
 
Frame(frame,width=295,height=2,bg='black').place (x=25,y=107)
# 
def on_enter(e):
    Code.delete(0,'end')

def on_leave(e):
    name=Code.get()
    if name=='':
        Code.insert(0,'Username')

Code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Lato', 11))
Code.place(x=30,y=150)
Code.insert(0,'Password')
Code.bind('<FocusIn>', on_enter)
Code.bind('<FocusOut>', on_leave)
 
Frame(frame,width=295,height=2,bg='black').place (x=25,y=177)

Button(frame,width=39,pady=7,text='Sign In', bg='#1CBFA8', fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?", fg='black', bg='white',font=('Lato',9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign Up', border=0,bg='white',cursor='hand2',fg='#7AB5B3',font=('Lato',9))
sign_up.place(x=215,y=270)

root.mainloop()
