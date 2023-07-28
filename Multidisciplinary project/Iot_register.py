from tkinter import* 
from tkinter import messagebox 
from PIL import Image, ImageTk
import ast  

def register2(root): 

    def is_empty_or_whitespace(s):
        return not s or s.isspace()

    def save_data():
        # Get the information from the Entry widgets
        username_info = Username.get()
        key_info = Key.get()
        feed1_info = Feed1.get()
        feed2_info = Feed2.get()

        # Check if any entry is empty or contains only whitespace characters
        if is_empty_or_whitespace(username_info) or is_empty_or_whitespace(key_info) \
            or is_empty_or_whitespace(feed1_info) or is_empty_or_whitespace(feed2_info):
            messagebox.showwarning("Invalid Input", "Please fill in all the fields.")
            return

        # Read existing data from the file (if it exists)
        try:
            with open("iot_info.txt", "r") as file:
                data = ast.literal_eval(file.read())
        except (FileNotFoundError, ValueError):
            # If the file doesn't exist or is not in the correct format, start with an empty dictionary
            data = {}

        # Update the data with the new information
        data["Username"] = username_info
        data["Key"] = key_info
        data["Feed1"] = feed1_info
        data["Feed2"] = feed2_info

        # Save the data back to the file
        with open("iot_info.txt", "w") as file:
            file.write(str(data))

        messagebox.showinfo("Saved", "Data saved successfully.")


 #tkinter GUI start from here

    root.withdraw()
    window=Toplevel(root)
    window.title("IoT settings")
    window.geometry('650x550+300+70')
    window.configure(bg="#ECECEA")
    window.resizable(False,False)
    
    
    Intro=Frame(window,bg= '#0C65F6',width=650,height=38)
    Intro.place(x=0,y=0)
    text1=Label(Intro,bg='#0C65F6',fg='white',text="Settings",font=("Time New Roman Bold",12))
    text1.place(x=10,y=7)

    def on_enter(e):
        Username.delete(0,END)
    def on_leave(e):
        a=Username.get()
        if a=="":
            Username.insert(0, 'Enter Adafruit username')

    def on_enter1(e):
        Key.delete(0,END)
    def on_leave1(e):
        a=Key.get()
        if a=="":
            Key.insert(0, 'Enter Adafruit key')


    acc_display=Frame(window,bg="#E9E9E9",width=400,height=170,highlightbackground='gray',highlightthickness=1)
    acc_display.place(x=40,y=80)
    Text2=Label(acc_display,bg="#E9E9E9",text="Adafruit account connection",font=("Times New Roman",14))
    Text2.place(x=90,y=5)


    Username=Entry(acc_display,width=40,font=("Times New Roman",11))
    Username.place(x=50,y=50)
    Username.bind('<FocusIn>',on_enter)
    Username.bind('<FocusOut>',on_leave)
    Username.insert(0,'Enter Adafruit username')

    Key=Entry(acc_display,width=40,font=("Times New Roman",11))
    Key.place(x=50,y=110)
    Key.bind('<FocusIn>',on_enter1)
    Key.bind('<FocusOut>',on_leave1)
    Key.insert(0,'Enter Adafruit key')


    acc_display1=Frame(window,bg="#E9E9E9",width=400,height=80,highlightbackground='gray',highlightthickness=1)
    acc_display1.place(x=40,y=270)
    Text3=Label(acc_display1,bg="#E9E9E9",text="Feed connection 1",font=("Times New Roman",14))
    Text3.place(x=125,y=5)
    Feed1=Entry(acc_display1,width=40,font=("Times New Roman",11))
    Feed1.place(x=50,y=40)

    acc_display2=Frame(window,bg="#E9E9E9",width=400,height=80,highlightbackground='gray',highlightthickness=1)
    acc_display2.place(x=40,y=370)
    Text4=Label(acc_display2,bg="#E9E9E9",text="Feed connection 2",font=("Times New Roman",14))
    Text4.place(x=125,y=5)
    Feed2=Entry(acc_display2,width=40,font=("Times New Roman",11))
    Feed2.place(x=50,y=40)

    Confirm=Button(window,bg='red',fg='white',text="Confirm",font=("Tahoma",14),command=save_data)
    Confirm.place(x=510,y=480)

    window.mainloop()

