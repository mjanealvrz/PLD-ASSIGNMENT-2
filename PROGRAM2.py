import tkinter as tk
from tkinter import Tk, LabelFrame, PhotoImage, Button
import pyttsx3

def submit():
    
    name_val = name_entry.get()
    age_val = age_entry.get()
    address_val = address_entry.get()
    print("Name:", name_val)
    print("Age:", age_val)
    print("Address:", address_val)
 
    text_speech = pyttsx3.init()
    text_speech.say(f"Name: {name_val}")
    text_speech.say(f"Age: {age_val}")
    text_speech.say(f"Address: {address_val}")
    text_speech.runAndWait()


window = Tk() 
window.geometry("679x399")
window.title("PLD ASSIGNMENT 2")
window.configure(bg="#ffffff")


custom_font = ('Comic Sans MS', 13)  

image_file = PhotoImage(file="background.png")
image = tk.Label(window, image=image_file)
image.pack()

frame = LabelFrame(window, text="Data Entry", padx=20, pady=20, font=custom_font)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
name_label = tk.Label(frame, text="Name:", font=custom_font)
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(frame, font=custom_font)
name_entry.grid(row=0, column=1, padx=10, pady=5)
age_label = tk.Label(frame, text="Age:", font=custom_font)
age_label.grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(frame, font=custom_font)
age_entry.grid(row=1, column=1, padx=10, pady=5)

address_label = tk.Label(frame, text="Address:", font=custom_font)
address_label.grid(row=2, column=0, padx=10, pady=5)
address_entry = tk.Entry(frame, font=custom_font)
address_entry.grid(row=2, column=1, padx=10, pady=5)

submit_button = Button(frame, text="Submit", command=submit, font=custom_font)
submit_button.grid(row=3, columnspan=2, pady=10)

display_frame = tk.Frame(window)
display_frame.pack(pady=20)

submitted_data_label = tk.Label(display_frame, text="", font=("Comic Sans MS", 12), justify=tk.LEFT)
submitted_data_label.pack()

  
window.mainloop()




