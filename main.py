from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import attendance


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root

        #creating the full screen geometry
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        #self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #image 1
        img = Image.open("Utils/bg 1.jpeg")
        img = img.resize((screen_width//3,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width = screen_width//3,height = 130)
        #image 2
        img1= Image.open("Utils/bg2.jpeg")
        img1= img1.resize((screen_width//3,130),Image.ANTIALIAS)
        self.photoimg1= ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=screen_width//3,y=0,width = screen_width//3,height = 130)
        
        #image3
        img2 = Image.open("Utils/bg 3.jpeg")
        img2= img2.resize((screen_width//3,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=2*screen_width//3,y=0,width = screen_width//3,height = 130)

        #bg 
        img3 = Image.open("Utils/BHU 2.jpeg")
        img3= img3.resize((screen_width,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=130,width =screen_width,height =710)

        title_lbl = Label(bg_img,text = "FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font = ("times new roman",35,"bold"),bg = "white",fg = "red")
        title_lbl.place(x=0,y=0,width=1530,height =45)

        #student button
        img4  =  Image.open("Utils/p5.jpeg")
        img4 = img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #FaceButton
        img5  =  Image.open("Utils/p5.jpeg")
        img5 = img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Face Detection",cursor="hand2",font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=500,y=300,width=220,height=40)

        #attendance
        img6  =  Image.open("Utils/attendance.jpg")
        img6 = img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=800,y=300,width=220,height=40)
        #exit
        img7  =  Image.open("Utils/exit.jpg")
        img7 = img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Exit",cursor="hand2",font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=1100,y=300,width=220,height=40)
        # Train data
        img8  =  Image.open("Utils/exit.jpg")
        img8 = img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Train Data",cursor="hand2",font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=200,y=580,width=220,height=40)

        # Student Photo
        img9  =  Image.open("Utils/exit.jpg")
        img9 = img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Photo",cursor="hand2",font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x=500,y=580,width=220,height=40)

        






    # ==============Function Buttons==============

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop() 

        