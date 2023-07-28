from tkinter import* 
from tkinter import messagebox 
from PIL import Image, ImageTk
import ast  
import Home_menu
import chatbot_module 
def Chatbot(root): 
    root.withdraw()
    window=Toplevel(root)
    window.title("Python virtual helper")
    window.geometry('900x600+300+70')
    window.configure(bg="#fff")
    window.resizable(False,False)
    imagebg= Image.open("Content_bg0.png")
    framebg= ImageTk.PhotoImage(imagebg)
    background_label = Label(window, image=framebg)
    background_label.place(x=0, y=0, relwidth=1)


    def Goback():
        window.destroy()
        Home_menu.Home(root)
    

    chatFrame=Frame(window,width=900,height=100,bg='#002d51')
    chatFrame.place(x=0,y=500)

    Chatscreen=Text(window,bg='#18181C',font=("Microsoft Yahei light",12),width=65,wrap=WORD,height=21,border=0,fg="#FAF9DD")
    Chatscreen.config(state=DISABLED)
    Chatscreen.place(x=150,y=37)

    Chatscreen_scroll = Scrollbar(window,command=Chatscreen.yview,width=20,highlightthickness=20)
    Chatscreen.configure(yscrollcommand=Chatscreen_scroll.set)
    Chatscreen_scroll.place(x=715,y=220)

    Menu_frame=Frame(window,width=32,height=495,bg='#220257')
    Menu_frame.place(x=0,y=5)
    
    Go_back=Button(Menu_frame,text="<--",font=('Microsoft Yahei light',11),fg="#FFFEF6",bg='#220257',border=0,command=Goback)
    Go_back.place(x=0,y=10)
    global status 
    status = 0 

    global previous_input
    previous_input=""

    def get_text():
        global status
        global previous_input
        text = Boxchat.get("1.0", END).strip()  # Use strip() to remove leading/trailing whitespace
        if status == 0: 
            temp=status 
            Chatscreen.config(state=NORMAL)  
            Chatscreen.insert(END, "\n----------------------------------\n\n" + "you:   " + text + "\n\n----------------------------------\n")
            Chatscreen.config(state=DISABLED)          
            status, bot_answer=chatbot_module.data_processing(text,Chatscreen,temp,previous_input)
            Chatscreen.config(state=NORMAL)
            Chatscreen.insert(END,bot_answer)
            Chatscreen.config(state=DISABLED)
            Boxchat.delete(1.0, END)  
        elif status==1: 
            temp=status 
            Chatscreen.config(state=NORMAL)  
            Chatscreen.insert(END, "\n----------------------------------\n\n" + "you:   " + text + "\n\n----------------------------------\n")
            Chatscreen.config(state=DISABLED) 
            status, bot_answer=chatbot_module.data_processing(text,Chatscreen,temp,previous_input)
            Chatscreen.config(state=NORMAL)
            Chatscreen.insert(END,bot_answer)
            Chatscreen.config(state=DISABLED)
            Boxchat.delete(1.0, END)
         
        elif status==2: 
            temp=status 
            Chatscreen.config(state=NORMAL)  
            Chatscreen.insert(END, "\n----------------------------------\n\n" + "you:   " + text + "\n\n----------------------------------\n")
            Chatscreen.config(state=DISABLED) 
            status, bot_answer=chatbot_module.data_processing(text,Chatscreen,temp,previous_input)
            Chatscreen.config(state=NORMAL)
            Chatscreen.insert(END,bot_answer)
            Chatscreen.config(state=DISABLED)
            Boxchat.delete(1.0, END)
        previous_input=text 


    Boxchat=Text(chatFrame,bg='white',width=40,font=("Microsoft Yahei light",14),wrap=WORD, height=3)
    Boxchat.place(x=180,y=10)
    scrollbar = Scrollbar(chatFrame, command=Boxchat.yview)
    Boxchat.configure(yscrollcommand=scrollbar.set)

    scrollbar.place(x=595,y=25)


    submit_button = Button(chatFrame, text="Submit", command=get_text,padx=18,pady=12,font=("Helvetica Bold",12),bg="green",fg="white",border=0)
    submit_button.place(x=640,y=25)



    window.mainloop()