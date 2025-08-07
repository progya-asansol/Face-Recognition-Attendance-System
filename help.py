from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System - Help Desk")
        self.root.resizable(True, True)
        self.root.minsize(800, 600)

        # Background Image
        try:
            bg_img = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\help_desk_background.jpg").resize((1280, 720))
            self.photoimg_bg = ImageTk.PhotoImage(bg_img)
            bg_label = Label(self.root, image=self.photoimg_bg)
            bg_label.place(x=0, y=0, width=1280, height=720)
        except FileNotFoundError:
            messagebox.showerror("Error", "Background image not found! Using default background.")
            bg_label = Label(self.root, bg="white")
            bg_label.place(x=0, y=0, width=1280, height=720)

        # Title
        title_lbl = Label(bg_label, text="Help Desk", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1280, height=45)

        # Main Frame for Content
        main_frame = Frame(bg_label, bd=2, relief=RIDGE, bg="white")
        main_frame.place(x=100, y=60, width=1080, height=600)

        # Header in Frame
        header_lbl = Label(main_frame, text="Welcome to the Face Recognition System Help Desk", 
                          font=("times new roman", 20, "bold"), bg="white", fg="darkblue")
        header_lbl.pack(pady=10)

        # Contact Information Section
        contact_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Contact Us", 
                                  font=("times new roman", 14, "bold"), bg="white")
        contact_frame.place(x=20, y=60, width=500, height=200)

        # Email
        try:
            email_icon = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\email_icon.png").resize((30, 30))
            self.photoimg_email = ImageTk.PhotoImage(email_icon)
            email_icon_lbl = Label(contact_frame, image=self.photoimg_email, bg="white")
            email_icon_lbl.place(x=10, y=20)
        except FileNotFoundError:
            email_icon_lbl = Label(contact_frame, text="📧", font=("arial", 20), bg="white")
            email_icon_lbl.place(x=10, y=20)

        email_lbl = Label(contact_frame, text="Email: progya.asansol@gmail.com", 
                         font=("times new roman", 14, "bold"), bg="white", fg="blue")
        email_lbl.place(x=50, y=20)

        # Phone
        try:
            phone_icon = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\phone_icon.png").resize((30, 30))
            self.photoimg_phone = ImageTk.PhotoImage(phone_icon)
            phone_icon_lbl = Label(contact_frame, image=self.photoimg_phone, bg="white")
            phone_icon_lbl.place(x=10, y=60)
        except FileNotFoundError:
            phone_icon_lbl = Label(contact_frame, text="📞", font=("arial", 20), bg="white")
            phone_icon_lbl.place(x=10, y=60)

        phone_lbl = Label(contact_frame, text="Phone: +91-123-456-7890", 
                         font=("times new roman", 14, "bold"), bg="white", fg="blue")
        phone_lbl.place(x=50, y=60)

        # Website
        website_lbl = Label(contact_frame, text="Website: www.face-recognition-support.com", 
                           font=("times new roman", 14, "bold"), bg="white", fg="blue")
        website_lbl.place(x=50, y=100)

        # Support Hours
        hours_lbl = Label(contact_frame, text="Support Hours: Mon-Fri, 9 AM - 5 PM IST", 
                         font=("times new roman", 12), bg="white", fg="black")
        hours_lbl.place(x=50, y=140)

        # Troubleshooting Section
        troubleshoot_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Troubleshooting Tips", 
                                      font=("times new roman", 14, "bold"), bg="white")
        troubleshoot_frame.place(x=540, y=60, width=500, height=200)

        tips_text = Text(troubleshoot_frame, font=("times new roman", 12), bg="white", fg="black", height=8, width=50)
        tips_text.insert(END, "- Camera not working? Ensure your webcam is connected and drivers are updated.\n")
        tips_text.insert(END, "- Face not recognized? Check lighting conditions and retrain the system.\n")
        tips_text.insert(END, "- Database error? Verify MySQL credentials and connection.\n")
        tips_text.insert(END, "- CSV issues? Ensure Progya.csv is not open in another program.\n")
        tips_text.config(state="disabled")
        tips_text.place(x=10, y=10)

        # System Description Section
        desc_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="About the System", 
                               font=("times new roman", 14, "bold"), bg="white")
        desc_frame.place(x=20, y=280, width=1020, height=150)

        desc_text = Text(desc_frame, font=("times new roman", 12), bg="white", fg="black", height=5, width=100)
        desc_text.insert(END, "The Face Recognition System is designed to automate attendance management using facial recognition technology. It integrates with a MySQL database and supports CSV export/import for attendance records. For detailed documentation, contact our support team or visit our website.")
        desc_text.config(state="disabled")
        desc_text.place(x=10, y=10)

        # Back Button
        back_btn = Button(main_frame, text="Back to Main Menu", command=self.back_to_main, 
                         font=("times new roman", 14, "bold"), bg="darkgreen", fg="white")
        back_btn.place(x=900, y=450, width=140, height=40)

    def back_to_main(self):
        messagebox.showinfo("Info", "Returning to main menu (functionality to be implemented).")

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()