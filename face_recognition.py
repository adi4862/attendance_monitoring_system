from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #title
        title_lbl = Label(self.root,text = "FACE RECOGNITION",font = ("times new roman",35,"bold"),bg = "white",fg = "green")
        title_lbl.place(x=0,y=0,width=1530,height =45)

        #left Image
        top_img = Image.open("F:/Study Material/MinorProject/p4.jpeg")
        top_img= top_img.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(top_img)

        f_lbl = Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width = 650,height = 700)


        #right image
        bottom_img = Image.open("F:/Study Material/MinorProject/p1.jpg")
        bottom_img= bottom_img.resize((750,700),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(bottom_img)

        f_lbl = Label(self.root,image = self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width = 750,height = 700)

        save_btn=Button(self.root,text="Save",command=self.face_recog,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.place(x=200,y=200)


    #=============Attendance==================
    def mark_attendance(self,i,r,n,):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            
            if((i not in name_list) or (r not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{dtString},{d1},present")



    #=============Face Recognition==============
    def face_recog(self):
        def draw_boundary(img,classfier,scaleFactor,minNeighbours,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classfier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord = []
            # n=str()
            # r=str()
            # i=str()

            for (x,y,w,h) in features:
                cv2.rectangle(img, (x,y) ,(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int(100*(1-predict/300))
                
                # try:
                conn = mysql.connector.connect(host="localhost",username="adi",password="asdf@1234",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select student_name from student where student_id ="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select student_roll from student where student_id ="+str(id))
                r=my_cursor.fetchone()
                print(n)
                r="+".join(r)

                my_cursor.execute("select student_roll from student where student_id ="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                
                # except Exception as es:
                #     messagebox.showerror("Error",f"due to:{str(es)}",parent = self.root)



                if confidence > 77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Uniform Face:",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        vedio_cap=cv2.VideoCapture(0)

        while True:
            ret,img=vedio_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            if cv2.waitKey(1)==13:
                break
        vedio_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop() 