from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from attendance import Attendance
from developer import Developer
from help import Help
from face_recognition import Face_Recognition
import time  # Added for clock functionality

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Image 1
        img = Image.open(r"C:\Users\hp\OneDrive\Pictures\Lana.png")
        img = img.resize((380, 100), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=380, height=100)

        # Image 2
        img1 = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\face-recognition2.jpg")
        img1 = img1.resize((380, 100), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img1)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=380, y=0, width=380, height=100)

        # Image 3
        img2 = Image.open(r"C:\Users\hp\OneDrive\Pictures\Lana.png")
        img2 = img2.resize((380, 100), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img2)
        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=760, y=0, width=380, height=100)

        # Image 4
        img4 = Image.open(r"C:\Users\hp\OneDrive\Pictures\faceregognition.webp")
        img4 = img4.resize((390, 100), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        f_lbl4 = Label(self.root, image=self.photoimg4)
        f_lbl4.place(x=1140, y=0, width=390, height=100)

        # Background Image
        img5 = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\Face-2.webp")
        img5 = img5.resize((1530, 690), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(img5)
        bg_lbl = Label(self.root, image=self.bg_photo)
        bg_lbl.place(x=0, y=100, width=1530, height=690)

        # Title
        title_lbl = Label(bg_lbl, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", 
                          font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ========== Button Section ==========
        
        # Student Button
        img6 = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\student2.jpg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_lbl, image=self.photoimg5, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_lbl = Label(bg_lbl, text="Student", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="blue")
        b1_lbl.place(x=200, y=320, width=220, height=40)

        # Detect Face Button
        img7 = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\facial-recognition.jpg")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img7)

        b2 = Button(bg_lbl, image=self.photoimg6, cursor="hand2", command=self.face_data)
        b2.place(x=500, y=100, width=220, height=220)

        b2_lbl = Label(bg_lbl, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="blue")
        b2_lbl.place(x=500, y=320, width=220, height=40)
        b2_lbl.bind("<Button-1>", lambda e: self.face_data())

        # Attendance Button
        img8 = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\Attendence.jpeg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img8)

        b3 = Button(bg_lbl, image=self.photoimg7, cursor="hand2", command=self.attendance_data)
        b3.place(x=800, y=100, width=220, height=220)

        b3_lbl = Label(bg_lbl, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="blue")
        b3_lbl.place(x=800, y=320, width=220, height=40)
        b3_lbl.bind("<Button-1>", lambda e: self.attendance_data())

        # Help Desk Button
        img9 = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\Help-Desk.png")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img9)

        b4 = Button(bg_lbl, image=self.photoimg8, cursor="hand2", command=self.help_data)
        b4.place(x=1100, y=100, width=220, height=220)

        b4_lbl = Label(bg_lbl, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="blue")
        b4_lbl.place(x=1100, y=320, width=220, height=40)
        b4_lbl.bind("<Button-1>", lambda e: self.help_data())

        # Train Face Button
        img10 = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\Train-Face2.jpg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img10)

        b5 = Button(bg_lbl, image=self.photoimg9, cursor="hand2", command=self.Train_data)
        b5.place(x=200, y=400, width=220, height=220)

        b5_lbl = Label(bg_lbl, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="blue")
        b5_lbl.place(x=200, y=620, width=220, height=40)
        b5_lbl.bind("<Button-1>", lambda e: self.Train_data())

        # Photos Button
        img11 = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\Photos.jpeg")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img11)

        b6 = Button(bg_lbl, image=self.photoimg10, cursor="hand2", command=self.open_img)
        b6.place(x=500, y=400, width=220, height=220)

        b6_lbl = Label(bg_lbl, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="blue")
        b6_lbl.place(x=500, y=620, width=220, height=40)
        b6_lbl.bind("<Button-1>", lambda e: self.Train_data())

        # Developer Button
        img12 = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\Developer.jpeg")
        img12 = img12.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img12)

        b7 = Button(bg_lbl, image=self.photoimg11, cursor="hand2", command=self.developer_data)
        b7.place(x=800, y=400, width=220, height=220)

        b7_lbl = Label(bg_lbl, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="blue")
        b7_lbl.place(x=800, y=620, width=220, height=40)
        b7_lbl.bind("<Button-1>", lambda e: self.developer_data())

        # Exit Button
        img13 = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\Exit.webp")
        img13 = img13.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img13)

        b8 = Button(bg_lbl, image=self.photoimg12, cursor="hand2", command=self.iExit)
        b8.place(x=1100, y=400, width=220, height=220)

        b8_lbl = Label(bg_lbl, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="blue")
        b8_lbl.place(x=1100, y=620, width=220, height=40)

        # Clock Label (Added for time display)
        self.clock_label = Label(bg_lbl, text="", font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.clock_label.place(x=10, y=10, width=100, height=30)
        self.update_time()  # Start the clock

    def update_time(self):
        """Update the clock label with current time every second"""
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_time)  # Schedule the next update

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def open_img(self):
        os.startfile("data")

    def Train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def Train_(self):
        os.startfile("data")

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def Train_(self):
        os.startfile("data")

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def Train_(self):
        os.startfile("data")

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def Developer(self):
        os.startfile("data")

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def Help(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognise", "Are you sure exit this project", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()