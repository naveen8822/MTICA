from tkinter import *
master=Tk()
demo_text="this is a sample demo of message widget."
msg=Message(master,text=demo_text)
msg.config(bg='lightGreen',font=('times',300,'italic'))
msg.pack()
