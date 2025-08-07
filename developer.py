from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Developer", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        # Top Image

        img_top = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\Train_top.jpeg")
        img_top = img_top.resize((1530, 720))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        top_label = Label(self.root, image=self.photoimg_top)
        top_label.place(x=0, y=55, width=1530, height=720)

#Frame
        main_frame=Frame(top_label,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1 = Image.open(r"Developer.jpeg")
        img_top1 = img_top1.resize((200, 200))
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        top_label = Label(main_frame, image=self.photoimg_top1)
        top_label.place(x=300, y=0, width=200, height=200)

        #Developer info
        dev_label=Label(main_frame,text="hello my name is Progya",font=("times now roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am a full stack developer",font=("times now roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        img_top2 = Image.open(r"Developer.jpeg")
        img_top2 = img_top2.resize((500, 400))
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)
        top_label = Label(main_frame, image=self.photoimg_top2)
        top_label.place(x=0, y=200, width=500, height=400)



if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()