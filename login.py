from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from face_recognition_system import Face_Recognition_System

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System - Login")
        self.root.resizable(True, True)
        self.root.minsize(800, 600)

        # Variables
        self.username_var = StringVar()
        self.password_var = StringVar()

        # Background Image
        try:
            bg_img = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\Face-2.webp").resize((1280, 720))
            self.bg_photo = ImageTk.PhotoImage(bg_img)
            bg_label = Label(self.root, image=self.bg_photo)
            bg_label.place(x=0, y=0, width=1280, height=720)
        except FileNotFoundError as e:
            print(f"Error loading background image: {e}")
            messagebox.showerror("Error", f"Background image not found: {e}")
            bg_label = Label(self.root, bg="white")
            bg_label.place(x=0, y=0, width=1280, height=720)

        # Title
        title_lbl = Label(bg_label, text="FACE RECOGNITION SYSTEM - LOGIN", 
                          font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1280, height=45)

        # Login Frame
        login_frame = Frame(bg_label, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=400, y=150, width=400, height=400)

        # Login Icon
        try:
            login_icon = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\login_icon.png").resize((100, 100))
            self.login_photo = ImageTk.PhotoImage(login_icon)
            login_icon_lbl = Label(login_frame, image=self.login_photo, bg="white")
            login_icon_lbl.place(x=150, y=20)
        except FileNotFoundError:
            login_icon_lbl = Label(login_frame, text="🔒", font=("arial", 40), bg="white")
            login_icon_lbl.place(x=175, y=20)

        # Username
        username_lbl = Label(login_frame, text="Username:", font=("times new roman", 14, "bold"), bg="white")
        username_lbl.place(x=50, y=120)
        username_entry = ttk.Entry(login_frame, textvariable=self.username_var, font=("times new roman", 12))
        username_entry.place(x=150, y=120, width=200)

        # Password
        password_lbl = Label(login_frame, text="Password:", font=("times new roman", 14, "bold"), bg="white")
        password_lbl.place(x=50, y=160)
        password_entry = ttk.Entry(login_frame, textvariable=self.password_var, font=("times new roman", 12), show="*")
        password_entry.place(x=150, y=160, width=200)

        # Buttons
        login_btn = Button(login_frame, text="Login", command=self.login, font=("times new roman", 14, "bold"), bg="darkgreen", fg="white")
        login_btn.place(x=50, y=220, width=120, height=40)

        signup_btn = Button(login_frame, text="Signup", command=self.open_signup, font=("times new roman", 14, "bold"), bg="blue", fg="white")
        signup_btn.place(x=230, y=220, width=120, height=40)

        exit_btn = Button(login_frame, text="Exit", command=self.exit, font=("times new roman", 14, "bold"), bg="red", fg="white")
        exit_btn.place(x=140, y=280, width=120, height=40)

    def login(self):
        """Validate login credentials and open main system"""
        if not self.username_var.get() or not self.password_var.get():
            messagebox.showerror("Error", "Username and password are required!", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Progya@2003", database="face_recognize"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE username=%s", (self.username_var.get(),))
            result = cursor.fetchone()
            conn.close()

            if result and result[0] == self.password_var.get():
                messagebox.showinfo("Success", "Login successful!", parent=self.root)
                self.root.destroy()  # Close login window
                main_root = Tk()  # Create new root for main system
                Face_Recognition_System(main_root)  # Launch main system
                main_root.mainloop()
            else:
                messagebox.showerror("Error", "Invalid username or password!", parent=self.root)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Database error: {e}", parent=self.root)

    def open_signup(self):
        """Open signup window"""
        self.signup_window = Toplevel(self.root)
        self.signup_window.geometry("800x600+200+100")
        self.signup_window.title("Face Recognition System - Signup")
        self.signup_window.resizable(False, False)

        # Variables
        self.signup_username_var = StringVar()
        self.signup_password_var = StringVar()
        self.confirm_password_var = StringVar()

        # Signup Frame
        signup_frame = Frame(self.signup_window, bd=2, relief=RIDGE, bg="white")
        signup_frame.place(x=200, y=100, width=400, height=400)

        # Title
        title_lbl = Label(signup_frame, text="Create New Account", font=("times new roman", 20, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=20, width=400, relheight=0.1)

        # Username
        username_lbl = Label(signup_frame, text="Username:", font=("times new roman", 14, "bold"), bg="white")
        username_lbl.place(x=50, y=100)
        username_entry = ttk.Entry(signup_frame, textvariable=self.signup_username_var, font=("times new roman", 12))
        username_entry.place(x=150, y=100, width=200)

        # Password
        password_lbl = Label(signup_frame, text="Password:", font=("times new roman", 14, "bold"), bg="white")
        password_lbl.place(x=50, y=150)
        password_entry = ttk.Entry(signup_frame, textvariable=self.signup_password_var, font=("times new roman", 12), show="*")
        password_entry.place(x=150, y=150, width=200)

        # Confirm Password
        confirm_password_lbl = Label(signup_frame, text="Confirm Password:", font=("times new roman", 14, "bold"), bg="white")
        confirm_password_lbl.place(x=50, y=200)
        confirm_password_entry = ttk.Entry(signup_frame, textvariable=self.confirm_password_var, font=("times new roman", 12), show="*")
        confirm_password_entry.place(x=150, y=200, width=200)

        # Buttons
        signup_btn = Button(signup_frame, text="Register", command=self.register, font=("times new roman", 14, "bold"), bg="blue", fg="white")
        signup_btn.place(x=50, y=260, width=120, height=40)

        cancel_btn = Button(signup_frame, text="Cancel", command=self.signup_window.destroy, font=("times new roman", 14, "bold"), bg="red", fg="white")
        cancel_btn.place(x=230, y=260, width=120, height=40)

    def register(self):
        """Register new user in the database"""
        if not self.signup_username_var.get() or not self.signup_password_var.get() or not self.confirm_password_var.get():
            messagebox.showerror("Error", "All fields are required!", parent=self.signup_window)
            return
        if self.signup_password_var.get() != self.confirm_password_var.get():
            messagebox.showerror("Error", "Passwords do not match!", parent=self.signup_window)
            return

        try:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Progya@2003", database="face_recognize"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM users WHERE username=%s", (self.signup_username_var.get(),))
            if cursor.fetchone():
                messagebox.showerror("Error", "Username already exists!", parent=self.signup_window)
            else:
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", 
                              (self.signup_username_var.get(), self.signup_password_var.get()))
                conn.commit()
                messagebox.showinfo("Success", "Registration successful! Please log in.", parent=self.signup_window)
                self.signup_window.destroy()
            conn.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Database error: {e}", parent=self.signup_window)

    def exit(self):
        """Exit the application"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=self.root):
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()