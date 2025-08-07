from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\hp\OneDrive\Desktop\Face Recognisation System\Detect face2.jpeg")
        img_top = img_top.resize((650, 700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        top_label = Label(self.root, image=self.photoimg_top)
        top_label.place(x=0, y=55, width=650, height=700)

        # Bottom Image
        img_bottom = Image.open(r"face recognition3.jpeg")
        img_bottom = img_bottom.resize((950, 700))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        bottom_label = Label(self.root, image=self.photoimg_bottom)
        bottom_label.place(x=650, y=55, width=950, height=700)

        b1_lbl = Button(self.root, text="FACE RECOGNITION",command=self.face_recog,
                        cursor="hand2", font=("times new roman", 18, "bold"),
                        bg="darkgreen", fg="white")
        b1_lbl.place(x=800, y=600, width=250, height=50)

#===========Attendence======================================
    def mark_attendence(self, i, r, n, d):
        try:
            with open("Progya.csv", "r+", newline="\n") as f:
                myDataList = f.readlines()
                record = f"{i},{r},{n},{d}"
                if not any(record in line for line in myDataList):
                    now = datetime.now()
                    d1 = now.strftime("%d/%m/%Y")
                    dtstring = now.strftime("%H:%M:%S")
                    f.writelines(f"\n{record},{dtstring},{d1},Present")
        except Exception as e:
            print(f"Error marking attendance: {e}")

#===================Face Recognition==========================
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            try:
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Fixed color conversion
                features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
                print(f"Detected {len(features)} faces")
                coord = []

                for (x, y, w, h) in features:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                    confidence = int(100 - predict)
                    print(f"ID: {id}, Confidence: {confidence}")

                    try:
                        conn = mysql.connector.connect(
                            host="localhost", username="root", password="Progya@2003", database="face_recognize")
                        my_cursor = conn.cursor()

                        my_cursor.execute("SELECT Name FROM student WHERE Student_id=%s", (id,))
                        n = my_cursor.fetchone()
                        n = "+".join(n) if n else "Unknown"

                        my_cursor.execute("SELECT Roll FROM student WHERE Student_id=%s", (id,))
                        r = my_cursor.fetchone()
                        r = "+".join(r) if r else "Unknown"

                        my_cursor.execute("SELECT Dep FROM student WHERE Student_id=%s", (id,))
                        d = my_cursor.fetchone()
                        d = "+".join(d) if d else "Unknown"

                        my_cursor.execute("SELECT Student_id FROM student WHERE Student_id=%s", (id,))
                        i = my_cursor.fetchone()
                        i = "+".join(i) if i else "Unknown"

                        conn.close()

                        if confidence > 50:  # Lowered threshold for testing
                            cv2.putText(img, f"ID:{i}", (x, y - 90), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Name:{n}", (x, y - 65), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Roll:{r}", (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Dept:{d}", (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            self.mark_attendence(i, r, n, d)
                        else:
                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                            cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                        coord = [x, y, w, h]
                    except Exception as e:
                        print(f"Database error: {e}")

                return coord
            except Exception as e:
                print(f"Error in draw_boundray: {e}")
                return []

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.05, 5, (255, 25, 255), "Face", clf)  # Adjusted parameters
            return img

        try:
            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            if faceCascade.empty():
                print("Error: Failed to load Haar cascade file")
                return

            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")
            print("Classifier loaded successfully")

            video_cap = cv2.VideoCapture(0)
            if not video_cap.isOpened():
                print("Error: Camera not accessible")
                return

            while True:
                ret, img = video_cap.read()
                if not ret:
                    print("Error: Failed to capture image")
                    break

                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome To Face Recognizer", img)

                if cv2.waitKey(1) == 13:  # Enter key
                    break

            video_cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print(f"Error in face_recog: {e}")



                   

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()