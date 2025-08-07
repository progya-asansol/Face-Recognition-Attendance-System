from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_lbl = Label(self.root, text="TRAIN DATASET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top Image
        img_top = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\Train_top.jpeg")
        img_top = img_top.resize((1530, 325))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        top_label = Label(self.root, image=self.photoimg_top)
        top_label.place(x=0, y=55, width=1530, height=325)

        # Train Button
        b1_lbl = Button(self.root, text="TRAIN DATA", command=self.train_classifier,
                        cursor="hand2", font=("times new roman", 30, "bold"),
                        bg="red", fg="white")
        b1_lbl.place(x=0, y=380, width=1530, height=60)

        # Bottom Image
        img_bottom = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\Train_bottom.jpeg")
        img_bottom = img_bottom.resize((1530, 325))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        bottom_label = Label(self.root, image=self.photoimg_bottom)
        bottom_label.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(".jpg")]

        faces = []
        ids = []

        for image in path:
            filename = os.path.split(image)[1]
            try:
            # Expecting filename like: user.<id>.<img_id>.jpg
                id = int(filename.split('.')[1])
            except (IndexError, ValueError):
                print(f"Skipping invalid file: {filename}")
                continue

            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)

        if len(faces) == 0 or len(ids) == 0:
            messagebox.showerror("Error", "No valid training data found.")
            return

        ids = np.array(ids, dtype=np.int32)  # ✅ Correct dtype

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed successfully.")



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
