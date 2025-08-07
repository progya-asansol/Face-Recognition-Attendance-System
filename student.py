# Student Management System with Update and Photo Buttons
import os
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Variables
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_course = StringVar()
        self.var_semester = StringVar()
        self.var_stuid = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_adress = StringVar()
        self.var_teacher = StringVar()
        self.var_radio = StringVar()

        # Top Images
        img1 = Image.open(r"C:\Users\hp\OneDrive\Pictures\student1.jpg").resize((500, 130))
        img2 = Image.open(r"C:\Users\hp\OneDrive\Pictures\student4.jpg").resize((500, 130))
        img3 = Image.open(r"C:\Users\hp\OneDrive\Pictures\student5.jpg").resize((550, 130))

        self.photoimg1 = ImageTk.PhotoImage(img1)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        Label(self.root, image=self.photoimg1).place(x=0, y=0, width=500, height=130)
        Label(self.root, image=self.photoimg2).place(x=500, y=0, width=500, height=130)
        Label(self.root, image=self.photoimg3).place(x=1000, y=0, width=550, height=130)

        # Background
        bg_img = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\Face-2.webp").resize((1530, 690))
        self.bg_photo = ImageTk.PhotoImage(bg_img)
        bg_lbl = Label(self.root, image=self.bg_photo)
        bg_lbl.place(x=0, y=130, width=1530, height=690)

        title_lbl = Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Main Frame
        main_frame = Frame(bg_lbl, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=600)

        # Left Frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"), bg="white")
        Left_frame.place(x=10, y=10, width=760, height=580)

        img_left = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\student3..jpg").resize((720, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(Left_frame, image=self.photoimg_left).place(x=5, y=0, width=720, height=130)

        # Current Course Frame
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)

        def add_combo(label, row, col, values, var):
            Label(current_course_frame, text=label, font=("times new roman", 12, "bold"), bg="white").grid(row=row, column=col, padx=10, pady=5, sticky=W)
            combo = ttk.Combobox(current_course_frame, textvariable=var, font=("times new roman", 12), state="readonly", width=18)
            combo["values"] = values
            combo.current(0)
            combo.grid(row=row, column=col + 1, padx=10, pady=5, sticky=W)

        add_combo("Department", 0, 0, ("Select Department", "CSE", "IT", "ECE", "AIML", "IOT", "EE", "MECH", "CIVIL"), self.var_dep)
        add_combo("Course", 0, 2, ("Select Course", "B.Tech", "M.Tech", "PhD"), self.var_course)
        add_combo("Year", 1, 0, ("Select Year", "1st", "2nd", "3rd", "4th"), self.var_year)
        add_combo("Semester", 1, 2, ("Select Semester", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"), self.var_semester)

        # Student Info Frame
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=290, width=720, height=270)

        def add_entry(label, var, row, col):
            Label(class_student_frame, text=label, font=("times new roman", 12, "bold"), bg="white").grid(row=row, column=col * 2, padx=10, pady=5, sticky=W)
            if label == "Gender":
                combo = ttk.Combobox(class_student_frame, textvariable=var, font=("times new roman", 12), state="readonly", width=20)
                combo["values"] = ("Select Gender", "Male", "Female", "Other")
                combo.current(0)
                combo.grid(row=row, column=col * 2 + 1, padx=10, pady=5, sticky=W)
            else:
                Entry(class_student_frame, textvariable=var, width=22, font=("times new roman", 12)).grid(row=row, column=col * 2 + 1, padx=10, pady=5, sticky=W)

        entries = [
            ("Student ID", self.var_stuid), ("Student Name", self.var_std_name),
            ("Class Division", self.var_div), ("Roll No", self.var_roll),
            ("Gender", self.var_gender), ("DOB", self.var_dob),
            ("Email", self.var_email), ("Phone No", self.var_phone),
            ("Address", self.var_adress), ("Teacher Name", self.var_teacher)
        ]

        for i, (label, var) in enumerate(entries):
            row, col = divmod(i, 2)
            add_entry(label, var, row, col)

        Radiobutton(class_student_frame, text="Take Photo Sample", variable=self.var_radio, value="Yes", font=("times new roman", 12), bg="white").grid(row=5, column=0, padx=10, pady=5, sticky=W)
        Radiobutton(class_student_frame, text="No Photo Sample", variable=self.var_radio, value="No", font=("times new roman", 12), bg="white").grid(row=5, column=1, padx=10, pady=5, sticky=W)

        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=180, width=715, height=50)

        Button(btn_frame, text="Save", command=self.add_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame, text="Update", command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=1)
        Button(btn_frame, text="Delete",command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=2)
        Button(btn_frame, text="Reset",command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=3)

        btn_frame_photo = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame_photo.place(x=0, y=225, width=715, height=35)

        Button(btn_frame_photo,command=self.generate_dataset, text="Take Photo", width=35, font=("times new roman", 13, "bold"), bg="green", fg="white").grid(row=0, column=0)
        Button(btn_frame_photo, text="Update Photo",command=self.update_photo, width=35, font=("times new roman", 13, "bold"), bg="green", fg="white").grid(row=0, column=1)

        # Right Frame
        right_frame = Frame(main_frame, bd=2, relief=RIDGE, bg="white")
        right_frame.place(x=780, y=10, width=700, height=580)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=10, width=690, height=550)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("id", "course", "year", "sem", "name", "div", "roll", "gender", "dob", "email", "address", "photo", "dep", "phone", "teacher"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table["show"] = "headings"
        for col in self.student_table["columns"]:
            self.student_table.heading(col, text=col.capitalize())
            self.student_table.column(col, width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_stuid.get() == "" or self.var_std_name.get() == "" or self.var_dep.get() == "Select Department":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Progya@2003", database="face_recognize")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.var_stuid.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(),
                self.var_dob.get(), self.var_email.get(), self.var_adress.get(), self.var_radio.get(),
                self.var_dep.get(), self.var_phone.get(), self.var_teacher.get()
            ))
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Success", "Student data added successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Progya@2003", database="face_recognize")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in data:
                self.student_table.insert("", END, values=row)
        conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        if data:
            self.var_stuid.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.var_std_name.set(data[4])
            self.var_div.set(data[5])
            self.var_roll.set(data[6])
            self.var_gender.set(data[7])
            self.var_dob.set(data[8])
            self.var_email.set(data[9])
            self.var_adress.set(data[10])
            self.var_radio.set(data[11])
            self.var_dep.set(data[12])
            self.var_phone.set(data[13])
            self.var_teacher.set(data[14])

    def update_data(self):
        if self.var_stuid.get() == "" or self.var_std_name.get() == "" or self.var_dep.get() == "Select Department":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Progya@2003", database="face_recognize")
            my_cursor = conn.cursor()
            my_cursor.execute("""
                UPDATE student SET
                    course=%s, Year=%s, semester=%s, Name=%s, Division=%s,
                    Roll=%s, Gender=%s, Dob=%s, Email=%s, Address=%s,
                    PhotoSample=%s, Dep=%s, Phone=%s, Teacher=%s
                WHERE Student_id=%s
            """, (
                self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                self.var_std_name.get(), self.var_div.get(), self.var_roll.get(),
                self.var_gender.get(), self.var_dob.get(), self.var_email.get(),
                self.var_adress.get(), self.var_radio.get(), self.var_dep.get(),
                self.var_phone.get(), self.var_teacher.get(), self.var_stuid.get()
            ))
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Success", "Student data updated successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


#Delete Fuction
    def delete_data(self):
        if self.var_stuid.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Progya@2003", database="face_recognize")
                    my_cursor = conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_stuid.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Delete","Sucessfully deleted details from student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

#RESET FUNCTION
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_stuid.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_adress.set("")
        self.var_teacher.set("")
        self.var_radio.set("")

#=================Generate Data 
# set or Take Photo samples============================
    def generate_dataset(self):
        student_id = self.var_stuid.get().strip()

        # Validation checks
        if student_id == "" or self.var_std_name.get().strip() == "" or self.var_dep.get() == "Select Department":
            messagebox.showerror("Error", "All fields are required including Student ID", parent=self.root)
            return

        try:
            # Step 1: Update database with photo sample status
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Progya@2003",
                database="face_recognize"
            )
            my_cursor = conn.cursor()

            my_cursor.execute("""
                UPDATE student SET
                    course=%s, Year=%s, semester=%s, Name=%s, Division=%s,
                    Roll=%s, Gender=%s, Dob=%s, Email=%s, Address=%s,
                    PhotoSample=%s, Dep=%s, Phone=%s, Teacher=%s
                WHERE Student_id=%s
            """, (
                self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                self.var_std_name.get(), self.var_div.get(), self.var_roll.get(),
                self.var_gender.get(), self.var_dob.get(), self.var_email.get(),
                self.var_adress.get(), "Yes", self.var_dep.get(),
                self.var_phone.get(), self.var_teacher.get(), student_id
            ))

            conn.commit()
            conn.close()

            self.fetch_data()
            self.reset_data()

            # Step 2: Face detection using OpenCV
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    return img[y:y + h, x:x + w]
                return None

            # Ensure data folder exists
           
            if not os.path.exists("data"):
                os.makedirs("data")

            cap = cv2.VideoCapture(0)
            img_id = 0

            while True:
                ret, my_frame = cap.read()
                if face_cropped(my_frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_cropped(my_frame), (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                    # Save image to data folder
                    file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                    cv2.imwrite(file_name_path, face)

                    # Show preview
                    cv2.putText(face, f"Image {img_id}", (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow("Capturing Face", face)

                if cv2.waitKey(1) == 13 or img_id >= 100:  # Enter key or 100 samples
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Dataset generation completed successfully!", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Error while generating dataset:\n{str(es)}", parent=self.root)

    def update_photo(self):
        student_id = self.var_stuid.get().strip()

        if student_id == "" or not student_id.isdigit():
            messagebox.showerror("Error", "Student ID must be a valid number", parent=self.root)
            return

    # Delete existing photos
        folder_path = "data"
        for file in os.listdir(folder_path):
            if file.startswith(f"user.{student_id}."):
                os.remove(os.path.join(folder_path, file))

    # Then re-capture photos like in generate_dataset
        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        def face_cropped(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                return img[y:y + h, x:x + w]
            return None

        cap = cv2.VideoCapture(0)
        img_id = 0
        while True:
            ret, my_frame = cap.read()
            if face_cropped(my_frame) is not None:
                img_id += 1
                face = cv2.resize(face_cropped(my_frame), (450, 450))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                cv2.imwrite(file_name_path, face)

                cv2.putText(face, f"Image {img_id}", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Updating Photo", face)

            if cv2.waitKey(1) == 13 or img_id >= 100:
                break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Success", "Photos updated. Please retrain the model.", parent=self.root)


    



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
