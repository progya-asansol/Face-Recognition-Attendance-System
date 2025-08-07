from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import csv
from datetime import datetime
import mysql.connector
import re

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Attendance Management System")
        self.root.resizable(True, True)
        self.root.minsize(800, 600)

        # Variables for entry fields
        self.attendance_id_var = StringVar()
        self.roll_var = StringVar()
        self.name_var = StringVar()
        self.dep_var = StringVar()
        self.time_var = StringVar()
        self.date_var = StringVar()
        self.atten_status_var = StringVar(value="Present")

        # Auto-fill time and date
        now = datetime.now()
        self.time_var.set(now.strftime("%H:%M:%S"))
        self.date_var.set(now.strftime("%d/%m/%Y"))

        # Top Images
        try:
            img_top = Image.open("attendance1.jpeg").resize((650, 200))
            self.photoimg_top = ImageTk.PhotoImage(img_top)
            top_label = Label(self.root, image=self.photoimg_top)
            top_label.place(x=0, y=0, width=650, height=200)

            img_bottom = Image.open("attendance2.jpg").resize((650, 200))
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
            bottom_label = Label(self.root, image=self.photoimg_bottom)
            bottom_label.place(x=650, y=0, width=650, height=200)
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"Image not found: {e}")
            return

        # Background Image
        try:
            bg_img = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\Face-2.webp").resize((1280, 520))
            self.bg_photo = ImageTk.PhotoImage(bg_img)
            bg_lbl = Label(self.root, image=self.bg_photo)
            bg_lbl.place(x=0, y=200, width=1280, height=520)
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"Background image not found: {e}")
            return

        # Title
        title_lbl = Label(bg_lbl, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1280, height=45)

        # Main Frame
        main_frame = Frame(bg_lbl, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1260, height=450)

        # Left Frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"), bg="white")
        Left_frame.place(x=10, y=10, width=620, height=430)

        try:
            img_left = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\student3..jpg").resize((600, 130))
            self.photoimg_left = ImageTk.PhotoImage(img_left)
            Label(Left_frame, image=self.photoimg_left).place(x=5, y=0, width=600, height=130)
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"Left frame image not found: {e}")
            return

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=135, width=610, height=250)

        # Labels and Entries
        attendanceId_label = Label(left_inside_frame, text="Student ID:", font=("times new roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        attendanceId_entry = ttk.Entry(left_inside_frame, textvariable=self.attendance_id_var, width=20, font=("times new roman", 12))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        rollLabel = Label(left_inside_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        rollLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        roll_entry = ttk.Entry(left_inside_frame, textvariable=self.roll_var, width=20, font=("times new roman", 12), state="readonly")
        roll_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        nameLabel = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        nameLabel.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        name_entry = ttk.Entry(left_inside_frame, textvariable=self.name_var, width=20, font=("times new roman", 12), state="readonly")
        name_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        depLabel = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        depLabel.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        dep_entry = ttk.Entry(left_inside_frame, textvariable=self.dep_var, width=20, font=("times new roman", 12), state="readonly")
        dep_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        timeLabel = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        timeLabel.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        time_entry = ttk.Entry(left_inside_frame, textvariable=self.time_var, width=20, font=("times new roman", 12))
        time_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        dateLabel = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        dateLabel.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        date_entry = ttk.Entry(left_inside_frame, textvariable=self.date_var, width=20, font=("times new roman", 12))
        date_entry.grid(row=5, column=1, padx=10, pady=5, sticky=W)

        attendanceLabel = Label(left_inside_frame, text="Attendance Status:", font=("Comic Sans MS", 11, "bold"), bg="white")
        attendanceLabel.grid(row=6, column=0, padx=10, pady=5, sticky=W)
        self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.atten_status_var, width=20, font=("Comic Sans MS", 11), state="readonly")
        self.atten_status["values"] = ("Present", "Absent")
        self.atten_status.grid(row=6, column=1, pady=8, padx=10, sticky=W)
        self.atten_status.current(0)

        # Buttons
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=210, width=605, height=35)

        import_btn = Button(btn_frame, text="Import CSV", command=self.import_csv, width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0, padx=5)
        export_btn = Button(btn_frame, text="Export CSV", command=self.export_csv, width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1, padx=5)
        update_btn = Button(btn_frame, text="Update", command=self.update_attendance, width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2, padx=5)
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_attendance, width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=3, padx=5)
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_fields, width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=4, padx=5)
        face_btn = Button(btn_frame, text="Face Recognition", command=self.face_recognition, width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        face_btn.grid(row=0, column=5, padx=5)

        # Right Frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"), bg="white")
        right_frame.place(x=640, y=10, width=610, height=430)

        # Table for Attendance Details
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=600, height=400)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.attendance_table = ttk.Treeview(table_frame, columns=("ID", "Roll", "Name", "Department", "Time", "Date", "Status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("ID", text="Student ID")
        self.attendance_table.heading("Roll", text="Roll No")
        self.attendance_table.heading("Name", text="Name")
        self.attendance_table.heading("Department", text="Department")
        self.attendance_table.heading("Time", text="Time")
        self.attendance_table.heading("Date", text="Date")
        self.attendance_table.heading("Status", text="Status")
        self.attendance_table["show"] = "headings"

        self.attendance_table.column("ID", width=100)
        self.attendance_table.column("Roll", width=100)
        self.attendance_table.column("Name", width=150)
        self.attendance_table.column("Department", width=150)
        self.attendance_table.column("Time", width=100)
        self.attendance_table.column("Date", width=100)
        self.attendance_table.column("Status", width=100)

        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease-1>", self.get_cursor)

    def validate_inputs(self):
        """Validate input fields"""
        if not self.attendance_id_var.get():
            messagebox.showerror("Error", "Student ID is required!")
            return False
        if not self.attendance_id_var.get().isdigit():
            messagebox.showerror("Error", "Student ID must be numeric!")
            return False
        if not re.match(r"^\d{2}:\d{2}:\d{2}$", self.time_var.get()):
            messagebox.showerror("Error", "Time must be in HH:MM:SS format!")
            return False
        if not re.match(r"^\d{2}/\d{2}/\d{4}$", self.date_var.get()):
            messagebox.showerror("Error", "Date must be in DD/MM/YYYY format!")
            return False
        return True

    def fetch_student_details(self, student_id):
        """Fetch student details from student table"""
        try:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Progya@2003", database="face_recognize"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT Name, Roll, Dep FROM student WHERE Student_id=%s", (student_id,))
            result = cursor.fetchone()
            conn.close()
            if result:
                self.name_var.set(result[0])
                self.roll_var.set(result[1])
                self.dep_var.set(result[2])
                return True
            else:
                messagebox.showerror("Error", f"Student ID {student_id} not found!")
                return False
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch student details: {e}")
            return False

    def save_attendance(self):
        """Save attendance data to CSV, MySQL, and table"""
        if not self.validate_inputs():
            return
        if not self.fetch_student_details(self.attendance_id_var.get()):
            return

        try:
            # Save to MySQL
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Progya@2003", database="face_recognize"
            )
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO attendance (student_id, time, date, status) VALUES (%s, %s, %s, %s)",
                (
                    self.attendance_id_var.get(),
                    self.time_var.get(),
                    self.date_var.get(),
                    self.atten_status_var.get()
                )
            )
            conn.commit()
            conn.close()

            # Add to table
            self.attendance_table.insert("", END, values=(
                self.attendance_id_var.get(),
                self.roll_var.get(),
                self.name_var.get(),
                self.dep_var.get(),
                self.time_var.get(),
                self.date_var.get(),
                self.atten_status_var.get()
            ))

            # Save to CSV
            with open("Progya.csv", "a", newline="\n") as f:
                writer = csv.writer(f)
                writer.writerow([
                    self.attendance_id_var.get(),
                    self.roll_var.get(),
                    self.name_var.get(),
                    self.dep_var.get(),
                    self.time_var.get(),
                    self.date_var.get(),
                    self.atten_status_var.get()
                ])

            messagebox.showinfo("Success", "Attendance saved successfully!")
            self.reset_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save attendance: {e}")

    def import_csv(self):
        """Import attendance data from CSV"""
        try:
            self.attendance_table.delete(*self.attendance_table.get_children())
            with open("Progya.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 7:
                        self.attendance_table.insert("", END, values=row[:7])
            messagebox.showinfo("Success", "CSV imported successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "Progya.csv not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to import CSV: {e}")

    def export_csv(self):
        """Export attendance data to CSV"""
        try:
            with open("Progya.csv", "w", newline="\n") as f:
                writer = csv.writer(f)
                for row_id in self.attendance_table.get_children():
                    row = self.attendance_table.item(row_id)["values"]
                    writer.writerow(row)
            messagebox.showinfo("Success", "CSV exported successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export CSV: {e}")

    def update_attendance(self):
        """Update selected attendance record"""
        selected = self.attendance_table.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a record to update!")
            return
        if not self.validate_inputs():
            return
        if not self.fetch_student_details(self.attendance_id_var.get()):
            return

        try:
            # Update table
            self.attendance_table.item(selected[0], values=(
                self.attendance_id_var.get(),
                self.roll_var.get(),
                self.name_var.get(),
                self.dep_var.get(),
                self.time_var.get(),
                self.date_var.get(),
                self.atten_status_var.get()
            ))

            # Update MySQL
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Progya@2003", database="face_recognize"
            )
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE attendance SET time=%s, date=%s, status=%s WHERE student_id=%s AND date=%s AND time=%s",
                (
                    self.time_var.get(),
                    self.date_var.get(),
                    self.atten_status_var.get(),
                    self.attendance_id_var.get(),
                    self.attendance_table.item(selected[0])["values"][5],  # Original date
                    self.attendance_table.item(selected[0])["values"][4]   # Original time
                )
            )
            conn.commit()
            conn.close()

            # Update CSV
            rows = []
            for row_id in self.attendance_table.get_children():
                row = self.attendance_table.item(row_id)["values"]
                rows.append(row)
            with open("Progya.csv", "w", newline="\n") as f:
                writer = csv.writer(f)
                writer.writerows(rows)

            messagebox.showinfo("Success", "Attendance updated successfully!")
            self.reset_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update attendance: {e}")

    def delete_attendance(self):
        """Delete selected attendance record"""
        selected = self.attendance_table.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a record to delete!")
            return

        if messagebox.askyesno("Confirm", "Are you sure you want to delete this record?"):
            try:
                # Get selected record's details
                selected_id = self.attendance_table.item(selected[0])["values"][0]
                selected_date = self.attendance_table.item(selected[0])["values"][5]
                selected_time = self.attendance_table.item(selected[0])["values"][4]

                # Delete from table
                self.attendance_table.delete(selected[0])

                # Delete from MySQL
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Progya@2003", database="face_recognize"
                )
                cursor = conn.cursor()
                cursor.execute("DELETE FROM attendance WHERE student_id=%s AND date=%s AND time=%s",
                              (selected_id, selected_date, selected_time))
                conn.commit()
                conn.close()

                # Update CSV
                rows = []
                for row_id in self.attendance_table.get_children():
                    row = self.attendance_table.item(row_id)["values"]
                    rows.append(row)
                with open("Progya.csv", "w", newline="\n") as f:
                    writer = csv.writer(f)
                    writer.writerows(rows)

                messagebox.showinfo("Success", "Attendance record deleted successfully!")
                self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete attendance: {e}")

    def get_cursor(self, event):
        """Populate fields when a table row is clicked"""
        selected = self.attendance_table.selection()
        if selected:
            row = self.attendance_table.item(selected[0])["values"]
            self.attendance_id_var.set(row[0])
            self.roll_var.set(row[1])
            self.name_var.set(row[2])
            self.dep_var.set(row[3])
            self.time_var.set(row[4])
            self.date_var.set(row[5])
            self.atten_status_var.set(row[6])

    def reset_fields(self):
        """Reset all entry fields"""
        self.attendance_id_var.set("")
        self.roll_var.set("")
        self.name_var.set("")
        self.dep_var.set("")
        now = datetime.now()
        self.time_var.set(now.strftime("%H:%M:%S"))
        self.date_var.set(now.strftime("%d/%m/%Y"))
        self.atten_status_var.set("Present")

    def face_recognition(self):
        """Trigger face recognition and update table"""
        try:
            from face_recognition import Face_Recognition
            face_root = Toplevel(self.root)
            face_obj = Face_Recognition(face_root, self)
            face_obj.face_recog()
        except ImportError:
            messagebox.showerror("Error", "Face Recognition module not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start face recognition: {e}")


        #====================================fetch data===========================
    

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()