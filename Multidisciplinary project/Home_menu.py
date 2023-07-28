from tkinter import* 
from PIL import Image, ImageTk 
import Chatbot_GUI
import AI_image
def Home(root): 
    root.withdraw()
    window=Toplevel(root)
    window.title("Python virtual helper")
    window.geometry('900x600+300+70')
    window.configure(bg="#fff")
    window.resizable(False,False)
    image= Image.open("Home background.png")
    framebg= ImageTk.PhotoImage(image)
    background_label = Label(window, image=framebg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    button_width = 27
    button_height = 12

    def Forward1():
        
        AI_image.image_dect(root)

    def Forward2():
        window.destroy()
        Chatbot_GUI.Chatbot(root)
        

    Imagebot="Image detection AI \n Simple bot used for image detection "
    Chatbot= "Chat bot  \n Default chatbot by receiving input \n from user"
    button1 =Button(window, text=Imagebot, width=button_width, height=button_height, font=("Helvetica Bold",17), bg="#002d51",fg="#ff3efc", cursor="hand2",command=Forward1)
    button2 =Button(window, text=Chatbot, width=button_width, height=button_height, font=("Helvetica Bold",17), bg="#002d51",fg="#ff3efc", cursor="hand2",command=Forward2)

    button1.place(x=85,y=125)
    button2.place(x=455,y=125)
    window.mainloop()

