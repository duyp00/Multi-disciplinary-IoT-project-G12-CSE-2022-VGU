
from tkinter import* 
from tkinter import messagebox 
from PIL import Image, ImageTk
import ast  
import Sign_in
def register(root): 
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
    Text1=Label(frame,text="Sign up",bg= '#3A1584',fg='#FFFFFF')
    Text1.config(font=('Helvetica bold', 26))
    Text1.place(x=170,y=20)
    def signup(): 
        username=user.get()
        code=password.get()
        reconfirm=Reconfirm.get()
        if code==reconfirm:
            try:           
                file=open('database.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)       
                dict2={username:code}
                r.update(dict2) 
                file.truncate(0)
                file.close()
                file=open('database.txt','w')
                w=file.write(str(r))
                messagebox.showinfo('Signup','Successfully sign up')
            except:
                file=open('database.txt','w')
                pp=str({'username':'password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid','Both password should match')

    def signin():
        window.destroy()
        Sign_in.log_in(root)
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
    def on_enter3(p):
        inp=Reconfirm.get()
        if inp=='                  Reconfirm Password       ':
            Reconfirm.delete(0,END)
    def on_leave3(p):
        name2=Reconfirm.get()
        if name2=='':
            Reconfirm.insert(0,'                  Reconfirm Password       ')
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

    Reconfirm=Entry(frame,width=35,fg='black',bg='white',font=('Microsoft Yahei UI Light',12))
    Reconfirm.place(x=65,y=220)
    Reconfirm.insert(0,'                  Reconfirm Password       ')
    Reconfirm.bind('<FocusIn>',on_enter3)
    Reconfirm.bind('<FocusOut>',on_leave3)

    Button(frame,width=20,pady=10,text="Confirm",bg='green',fg='white',cursor='hand2',border=0,font=('Helvetica bold',12),command=signup).place(x=130,y=285)
    Label(frame,text="already have an account?",bg='#3A1584',fg='#FFFFFF',font=('Microsoft Yahei UI Light',9)).place(x=130,y=354)
    sign_in= Button(frame,text="Sign in",bg='#3A1584',fg='#0FDFEC',border=0,cursor='hand2',font=('Helvetica Bold',10),command=signin).place(x=275,y=354)
    window.mainloop()
