from tkinter import * 
import ast 
import cv2
import numpy as np
from keras.models import load_model
from threading import Thread
import time
from PIL import Image, ImageTk
from Adafruit_IO import MQTTClient
import Iot_register


def image_dect(root):

    def read_data_from_file():
        filename="iot_info.txt"
        try:
            with open(filename, "r") as file:
                data_str = file.read().strip()
                data = ast.literal_eval(data_str)
                return data
        except (FileNotFoundError, ValueError):
            return {}
    data = read_data_from_file()

    Adf_user=data.get("Username", "")
    Adf_key=data.get("Key", "")
    Adf_Feed1=data.get("Feed1", "")
    Adf_Feed2=data.get("Feed2", "")
    # Load the model
    model = load_model("keras_Model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r").readlines()

    # CAMERA can be 0 or 1 based on the default camera of your computer
    camera = cv2.VideoCapture(0)

    # MQTT client setup
    try:
        client = MQTTClient(Adf_user,Adf_key)
        client.connect()
        client.loop_background()
    except:
        pass 

    # Global variable to store the latest frame from the camera
    global latest_frame
    latest_frame = None

    def start_detection():
        global detection_enabled
        detection_enabled = True
        detection_thread = Thread(target=image_detection)
        detection_thread.daemon = True
        detection_thread.start()

    def stop_detection():
        global detection_enabled
        detection_enabled = False

    # Image detection function using Google Teachable Machine
    def image_detection():
        global latest_frame

        while detection_enabled:
            # Grab the webcamera's image.
            ret, frame = camera.read()

            # Resize the raw image into (224-height, 224-width) pixels
            resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)

            # Make the frame a numpy array and reshape it to the model's input shape.
            image = np.asarray(resized_frame, dtype=np.float32).reshape(1, 224, 224, 3)

            # Normalize the image array
            image = (image / 127.5) - 1

            # Predict the model
            prediction = model.predict(image)
            index = np.argmax(prediction)
            class_name = class_names[index]
            confidence_score = prediction[0][index]

            # Print prediction and confidence score
            display_box.config(state=NORMAL)
            display_box.insert(END,"\nClass:" + str(class_name[2:]) + "")
            display_box.insert(END,"\nConfidence Score: " + str(np.round(confidence_score * 100))[:-2] + "%")
            display_box.config(state=DISABLED)
            
            client.publish(Adf_Feed1, class_name[2:])
            
            client.publish(Adf_Feed2, np.round(confidence_score * 100))

            # Convert the frame to RGB before storing it
            latest_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

            time.sleep(1)  # Add a small delay to control the frame rate

    def process_and_display_frame():
        global latest_frame

        while True:
            if latest_frame is not None:
                # Modify the size you want (e.g., 640x480, 800x600, etc.)
                display_width, display_height = 670, 500

                # Resize the latest frame to the desired display size
                resized_frame = cv2.resize(latest_frame, (display_width, display_height), interpolation=cv2.INTER_AREA)

                # Convert the resized frame to a Tkinter PhotoImage
                img = Image.fromarray(resized_frame)
                img = ImageTk.PhotoImage(img)

                # Update the canvas with the current frame
                canvas.create_image(0, 0, anchor=NW, image=img)
                canvas.img = img

                time.sleep(1)
    def info_register():
        Iot_register.register2(root)

    def EXIT():
        window.quit()

    # Tkinter GUI setup
    root.withdraw()
    window=Toplevel(root)
    window.title("Python virtual helper")
    window.geometry('900x600+300+70')
    window.configure(bg="#fff")
    window.resizable(False,False)
    window.title("Image Detection GUI")

    canvas = Canvas(window, width=655, height=495)
    canvas.place(x=0,y=0)

    Control_frame=Frame(window,width=900,height=105,bg='#053FB5')
    Control_frame.place(x=0,y=495)

    button_dect=Button(Control_frame,bg='green',fg='white',text="Detect",font=('Helvetica Bold',12),command=start_detection)
    button_dect.place(x=50,y=40)
    button_notdect=Button(Control_frame,bg='red',fg='white',text="Disable detection",font=('Helvetica Bold',12),command=stop_detection)
    button_notdect.place(x=300,y=40)

    button_iot=Button(Control_frame,bg='#015D1F',fg='white',text="IoT",font=('Helvetica Bold',12),command=info_register)
    button_iot.place(x=850,y=70)


    # Run process_and_display_frame in a separate thread
    processing_thread = Thread(target=process_and_display_frame)
    processing_thread.daemon = True
    processing_thread.start()

    display_box=Text(window,width=20,height=18,bg='white',fg='black',wrap=WORD,font=("Comic Sans MS",12),state=DISABLED)
    display_box.place(x=680,y=0)
    display_scroll = Scrollbar(window,command=display_box.yview,width=20,highlightthickness=20)
    display_box.configure(yscrollcommand=display_scroll.set)
    display_scroll.place(x=855,y=180)


    window.mainloop()

    # Release the camera and close the OpenCV windows when the GUI is closed
    camera.release()
    cv2.destroyAllWindows()

