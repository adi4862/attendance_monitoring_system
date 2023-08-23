from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        #creating the full screen geometry
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        #self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #========variables===============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_session=StringVar()
        self.var_sem=StringVar()
        self.va_st_id=StringVar()
        self.va_st_name=StringVar()
        self.var_gen=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()


        #image 1
        img = Image.open("Utils/p6.jpeg")
        img = img.resize((screen_width//3,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width = screen_width//3,height = 130)
        #image 2
        img1= Image.open("Utils/p4.jpeg")
        img1= img1.resize((screen_width//3,130),Image.ANTIALIAS)
        self.photoimg1= ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=screen_width//3,y=0,width = screen_width//3,height = 130)
        
        #image3
        img2 = Image.open("Utils/p1.jpg")
        img2= img2.resize((screen_width//3,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=2*screen_width//3,y=0,width = screen_width//3,height = 130)

        #bg 
        img3 = Image.open("Utils/p3.jpeg")
        img3= img3.resize((screen_width,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=130,width =screen_width,height =710)

        title_lbl = Label(bg_img,text = "STUDENT DETAIL",font = ("times new roman",35,"bold"),bg = "white",fg = "green")
        title_lbl.place(x=0,y=0,width=screen_width,height =45)
        
        main_frame= Frame(bg_img,bd = 2,bg='white')
        main_frame.place(x=10,y=55,width=screen_width,height=590)
        #left side label
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font= ("Times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width =725,height = 570)
        
        #error
        left_img = Image.open("Utils/p4.jpeg")
        left_img= left_img.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(left_img)

        f_lbl = Label(Left_frame,image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width = 715,height = 130)

        # current course
        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course",font= ("Times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width =710,height = 120)

        #department
        dep_label = Label(current_course_frame,width=10,justify=LEFT,text="Department",font= ("Times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font= ("Times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer Science")#enter remaining
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W) 

        #Course
        course_label = Label(current_course_frame,width=10,justify=LEFT,text="Course",font= ("Times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font= ("Times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","MCA","Msc")#enter remaining
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #session
        session_label = Label(current_course_frame,width=10,justify=LEFT,text="Session",font= ("Times new roman",12,"bold"),bg="white")
        session_label.grid(row=1,column=0,padx=10,sticky=W)

        session_combo = ttk.Combobox(current_course_frame,textvariable=self.var_session,font= ("Times new roman",12,"bold"),state="readonly")
        session_combo["values"]=("Select Session","2021-22","2022-23")#enter remaining
        session_combo.current(0)
        session_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W) 

        #Semester
        semester_label = Label(current_course_frame,width=10,justify=LEFT,text="Semester",font= ("Times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_sem,font= ("Times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4")#enter remaining
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W) 

        #Class student information
        class_student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font= ("Times new roman",12,"bold"))
        class_student_frame.place(x=5,y=255,width =710,height = 290)

        #StudentID
        studentID_label = Label(class_student_frame,text="StudentID:",font= ("Times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry = ttk.Entry(class_student_frame,textvariable=self.va_st_id,font= ("Times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student name
        studentName_label = Label(class_student_frame,text="Student Name:",font= ("Times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.va_st_name,width=20,font= ("Times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label = Label(class_student_frame,text="Class Division:",font= ("Times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font= ("Times new roman",12,"bold"),state="readonly")
        class_div_combo["values"]=("Select Division","A","B","C","D")#enter remaining
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W) 


        #roll_N0
        student_roll_label = Label(class_student_frame,text="Roll No:",font= ("Times new roman",12,"bold"),bg="white")
        student_roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font= ("Times new roman",12,"bold"))
        student_roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        student_gender_label = Label(class_student_frame,text="Gender",font= ("Times new roman",12,"bold"),bg="white")
        student_gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        student_gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gen,font= ("Times new roman",12,"bold"),state="readonly")
        student_gender_combo["values"]=("Select Gender","Male","Female","Other")#enter remaining
        student_gender_combo.current(0)
        student_gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W) 

        #DOB
        student_DOB = Label(class_student_frame,text="DOB:",font= ("Times new roman",12,"bold"),bg="white")
        student_DOB.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studet_DOB_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font= ("Times new roman",12,"bold"))
        studet_DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        student_email = Label(class_student_frame,text="E-mail:",font= ("Times new roman",12,"bold"),bg="white")
        student_email.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studet_email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font= ("Times new roman",12,"bold"))
        studet_email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #phone No
        student_phone = Label(class_student_frame,text="Phone No:",font= ("Times new roman",12,"bold"),bg="white")
        student_phone.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        studet_phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font= ("Times new roman",12,"bold"))
        studet_phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        


        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=4,column=0,padx=5,pady=10,sticky=W)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=4,column=1,padx=5,pady=10,sticky=W)

        #buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=705,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
                      

        Update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Update_btn.grid(row=0,column=1)

        Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2)  

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=705,height=35)

        Take_photo_btn=Button(btn_frame1,text="Take photo Sample",command=self.generate_dataset,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Take_photo_btn.grid(row=0,column=0)
        Update_photo_btn=Button(btn_frame1,text="update photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Update_photo_btn.grid(row=0,column=1)      
            

        #right side label
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font= ("Times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width =725,height = 570)

        right_img = Image.open("Utils/p2.jpeg")
        right_img= right_img.resize((730,130),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(right_img)

        f_lbl = Label(Right_frame,image = self.photoimg_right)
        f_lbl.place(x=5,y=0,width = 700,height = 130)
        #============searching System==========
        Search_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font= ("Times new roman",15,"bold"))
        Search_frame.place(x=5,y=135,width =710,height =80)

        Search_label = Label(Search_frame,text="Search By:",font= ("Times new roman",15,"bold"),bg="red",fg="white")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Search_combo = ttk.Combobox(Search_frame,font= ("Times new roman",12,"bold"),state="readonly",width=15)
        Search_combo["values"]=("Select","Roll_No","Phone_No")#enter remaining
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W) 

        #search button
        Search_btn=Button(Search_frame,text="Search",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=2,padx=4)
        #show button
        ShowAll_btn=Button(Search_frame,text="Show All",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=3,padx=4)
        
        # table frame
        table_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=220,width =710,height =250)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("id","Name","div","roll","gen","dob","email","phone","dep","course","session","sem","photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side = BOTTOM,fill = X)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("session",text="Session")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("Name",text="Student Name")
        self.student_table.heading("roll",text="Roll Number")
        self.student_table.heading("div",text="Class Division")
        self.student_table.heading("gen",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="E-mail")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("session",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("gen",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #==============function declaration==========   
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.va_st_name.get()=="" or self.va_st_id=="" or self.var_course=="Select Course" or self.var_session=="Select Session" or self.var_sem=="Select Semester" or self.var_div=="Select Division" or self.var_roll=="" or self.var_gen=="Select Gender" or self.var_dob=="":
            messagebox.showerror("Error","All Fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="adi",password="asdf@1234",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.va_st_id.get(),
                                                                            self.va_st_name.get(),
                                                                            self.var_div.get(),
                                                                            self.var_roll.get(),
                                                                            self.var_gen.get(),
                                                                            self.var_dob.get(),
                                                                            self.var_email.get(),
                                                                            self.var_phone.get(),
                                                                            self.var_dep.get(),
                                                                            self.var_course.get(),
                                                                            self.var_session.get(),                                                                     
                                                                            self.var_sem.get(),
                                                                            self.var_radio1.get(),
                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"due to:{str(es)}",parent = self.root)

    #=========================fetch data==========================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="adi",password="asdf@1234",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()




    #===========get cursor==============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data = content["values"]

        self.va_st_id.set(data[0]),
        self.va_st_name.set(data[1]),
        self.var_div.set(data[2]),
        self.var_roll.set(data[3]),
        self.var_gen.set(data[4])
        self.var_dob.set(data[5])
        self.var_email.set(data[6])
        self.var_phone.set(data[7])    
        self.var_dep.set(data[8]),
        self.var_course.set(data[9]),
        self.var_session.set(data[10]),
        self.var_sem.set(data[11]),
        self.var_radio1.set(data[12]),
        
        
    

    # =======Update Function========
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.va_st_name.get()=="" or self.va_st_id=="" or self.var_course=="Select Course" or self.var_session=="Select Session" or self.var_sem=="Select Semester" or self.var_div=="Select Division" or self.var_roll=="" or self.var_gen=="Select Gender" or self.var_dob=="":
            messagebox.showerror("Error","All Fields are required")

        else:
            try:
                Update = messagebox.askyesno("Update","Do you wanbt to Update the data",parent=self.root)
                if Update >0:
                    conn = mysql.connector.connect(host="localhost",username="adi",password="asdf@1234",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET student_name=%s,student_division=%s,student_roll=%s,student_gender=%s,student_dob=%s,student_email=%s,student_phone=%s,department=%s,course=%s,session=%s,sem=%s,photo=%s where student_id=%s",(
                                                                                                                                                                                                                                                            self.va_st_name.get(),
                                                                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                                                                            self.var_gen.get(),
                                                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                                                            self.var_session.get(),                                                                     
                                                                                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                                                            self.va_st_id.get()
                                                                                                                                                            ))
                                                                        
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details suceesfkansdgjal",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)




    #===========Delete Function========

    def delete_data(self):
        if self.va_st_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)

                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="adi",password="asdf@1234",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.va_st_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",self.root)    
    

    #===============Reset Data=================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_div.set("Select Division")
        self.var_sem.set("Select Semester")
        self.var_gen.set("Select Gender")
        self.var_radio1.set("")
        self.var_roll.set(0)
        self.var_session.set("Select Session") 
        self.va_st_id.set("")
        self.va_st_name.set("")   
        self.var_roll.set("")   
        self.var_dob.set("") 
        self.var_email.set("") 
        self.var_phone.set("")          



    #==================Generate data set and take a photo sample===============
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.va_st_name.get()=="" or self.va_st_id=="" or self.var_course=="Select Course" or self.var_session=="Select Session" or self.var_sem=="Select Semester" or self.var_div=="Select Division" or self.var_roll=="" or self.var_gen=="Select Gender" or self.var_dob=="":
            messagebox.showerror("Error","All Fields are required")

        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="adi",password="asdf@1234",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE student SET student_name=%s,student_division=%s,student_roll=%s,student_gender=%s,student_dob=%s,student_email=%s,student_phone=%s,department=%s,course=%s,session=%s,sem=%s,photo=%s where student_id=%s",(
                                                                                                                                                                                                                                                            self.va_st_name.get(),
                                                                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                                                                            self.var_gen.get(),
                                                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                                                            self.var_session.get(),                                                                     
                                                                                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                                                            self.va_st_id.get()==id+1
                                                                                                                                                            ))
                                                                        
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close() 

                #=================Load predefined data on face frontals from openCV=============
                face_classifiers=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifiers.detectMultiScale(gray,1.3,5)
                        #scaling factor = 1.3
                        #minimun Neighbor = 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                        
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1                            
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    
                


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop() 

      