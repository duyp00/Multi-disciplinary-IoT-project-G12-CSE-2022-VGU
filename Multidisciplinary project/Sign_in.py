from tkinter import* 
from tkinter import messagebox 
from PIL import Image, ImageTk
import ast  
import Sign_up
import Home_menu
def log_in(root): 
    root.withdraw()
    window=Toplevel(root)
    window.title("Python virtual helper")
    window.geometry('900x600+300+70')
    window.configure(bg="#fff")
    window.resizable(False,False)
    image= Image.open("neondarkbg3.png")
    framebg= ImageTk.PhotoImage(image)
    background_label = Label(window, image=framebg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    frame=Frame(window,width=480,height=425)
    frame.pack(fill=None,expand=True)
    frame_label=Label(frame,bg='#3A1584')
    frame_label.place(x=0,y=0, relwidth=1,relheight=1)
    Text1=Label(frame,text="Sign in",bg= '#3A1584',fg='#FFFFFF')
    Text1.config(font=('Helvetica bold', 26))
    Text1.place(x=170,y=20)

    
    def Signin(): 
        
        username=user.get()
        code=password.get()
        file=open('database.txt','r')
        d=file.read()
        r=ast.literal_eval(d)
        file.close()
        if username in r.keys() and code==r[username]:
            window.destroy()
            Home_menu.Home(root)
        else:
            messagebox.showerror('Invalid','Username or password incorrect')
   
    
    
    def signup():
        window.destroy()
        Sign_up.register(root)
        
    def on_enter(e):
        inp=user.get()
        if inp=='                     Enter Username       ':
            user.delete(0,END)

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'                     Enter Username       ')

    def on_enter2(p):
        inp=password.get()
        if inp=='                     Enter Password       ':
            password.delete(0,END)

    def on_leave2(p):
        name2=password.get()
        if name2=='':
            password.insert(0,'                     Enter Password       ')

    user=Entry(frame,width=35,fg='black',bg='white',font=('Microsoft Yahei UI Light',12))
    user.place(x=65,y=110)
    user.insert(0,'                     Enter Username       ')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    password=Entry(frame,width=35,fg='black',bg='white',font=('Microsoft Yahei UI Light',12))
    password.place(x=65,y=165)
    password.insert(0,'                     Enter Password       ')
    password.bind('<FocusIn>',on_enter2)
    password.bind('<FocusOut>',on_leave2)


    Button(frame,width=20,pady=10,text="Confirm",bg='green',fg='white',cursor='hand2',border=0,font=('Helvetica bold',12),command=Signin).place(x=130,y=285)
    Label(frame,text="=don't have an account?",bg='#3A1584',fg='#FFFFFF',font=('Microsoft Yahei UI Light',9)).place(x=130,y=354)
    sign_up= Button(frame,text="Sign up",bg='#3A1584',fg='#0FDFEC',border=0,cursor='hand2',font=('Helvetica Bold',10),command=signup).place(x=275,y=354)
    window.mainloop()
