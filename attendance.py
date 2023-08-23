from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class attendance:
    def __init__(self,root):
        self.root = root
        #creating the full screen geometry
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        #self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #============================variables=============#
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name= StringVar()
        
        self.var_atten_time= StringVar()
        self.var_atten_date= StringVar()
        self.var_atten_attendance= StringVar()



        #First Image
        first_img = Image.open("Utils/p4.jpeg")
        first_img= first_img.resize((800,200),Image.ANTIALIAS)
        self.photoimg_first = ImageTk.PhotoImage(first_img)

        f_lbl = Label(self.root,image = self.photoimg_first)
        f_lbl.place(x=0,y=0,width = 800,height = 200)

        #Second image
        second_img = Image.open("Utils/p1.jpg")
        second_img= second_img.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_second = ImageTk.PhotoImage(second_img)

        f_lbl = Label(self.root,image = self.photoimg_second)
        f_lbl.place(x=800,y=0,width = 800,height = 200)

        #bg 
        img3 = Image.open("Utils/p3.jpeg")
        img3= img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=130,width =1530,height =710)

        title_lbl = Label(bg_img,text = "ATTENDANCE MANAGEMENT SYSTEM",font = ("times new roman",35,"bold"),bg = "white",fg = "green")
        title_lbl.place(x=0,y=0,width=1530,height =45)

        main_frame= Frame(bg_img,bd = 2,bg='white')
        main_frame.place(x=10,y=55,width=1500,height=590)

        #left side label
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font= ("Times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width =725,height = 570)

        left_img = Image.open("Utils/p4.jpeg")
        left_img= left_img.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(left_img)

        f_lbl = Label(Left_frame,image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width = 715,height = 130)

        left_inside_frame= Frame(Left_frame,bd = 2,relief=RIDGE,bg='white')
        left_inside_frame.place(x=0,y=135,width=720,height=300)

        #Lebels and Entryd

        #AttendanceID
        attendanceID_label = Label(left_inside_frame,text="AttendanceID:",font= ("Times new roman",12,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame,width = 20,textvariable = self.var_atten_id,font= ("Times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll
        roll_label = Label(left_inside_frame,text="Roll:",font= ("Times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        roll_entry = ttk.Entry(left_inside_frame,width = 22,textvariable = self.var_atten_roll,font= ("Times new roman",12,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Name
        name_label = Label(left_inside_frame,text="Name:",font= ("Times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry = ttk.Entry(left_inside_frame,width = 22,textvariable = self.var_atten_name,font= ("Times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #time
        time_label = Label(left_inside_frame,text="Time:",font= ("Times new roman",12,"bold"),bg="white")
        time_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        time_entry = ttk.Entry(left_inside_frame,width = 22,textvariable = self.var_atten_time,font= ("Times new roman",12,"bold"))
        time_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #date
        date_label = Label(left_inside_frame,text="date:",font= ("Times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        date_entry = ttk.Entry(left_inside_frame,width = 22,textvariable = self.var_atten_date,font= ("Times new roman",12,"bold"))
        date_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Attendance Status
        attendance_status_label = Label(left_inside_frame,text="Attendance Status:",font= ("Times new roman",12,"bold"),bg="white")
        attendance_status_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        attendance_status_combo = ttk.Combobox(left_inside_frame,width = 20,textvariable = self.var_atten_attendance,font= ("Times new roman",12,"bold"),state="readonly")
        attendance_status_combo["values"]=("Select Status","Present","Absent")#enter remaining
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=705,height=35)

        save_btn=Button(btn_frame,text="Import CSV",command = self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
                      

        Update_btn=Button(btn_frame,text="Export CSV",command = self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Update_btn.grid(row=0,column=1)

        Delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2)  

        reset_btn=Button(btn_frame,text="Reset",command = self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        #right side label
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font= ("Times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width =725,height = 570)

        # table frame
        table_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=0,width =700,height =545)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("id","roll","name","time","date","attendance" ),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side = BOTTOM,fill = X)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id",text="AttendanceID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("roll",text="Roll Number")
        self.student_table.heading("time",text="Time")
        self.student_table.heading("date",text="Date")
        self.student_table.heading("attendance",text="Attendance")
        self.student_table["show"]="headings"

        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("time",width=100)
        self.student_table.column("date",width=100)
        self.student_table.column("attendance",width=100)

        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)



    # =================fetch data=======================#


    def fetchData(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)


    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetype=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter = ",")
            for i in csvread:
             mydata.append(i)
            self.fetchData(mydata)


    #=========================Export csv===========================#
    def exportCsv(self):
      try:
        if len(mydata)<1:
           messagebox.showerror("No data","No data found too expert",parent = self.root)
           return False
        fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetype=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln,mode="W",newline=" ")as myfile:
           exp_write=csv.writer(myfile,delimiter=",")
           for i in mydata:
            exp_write.writerow(i)
            messagebox.showinfo("Data Export","Your Data Exported to"+os.path.basename(fln)+"successfully")
      except Exception as es:
            messagebox.showerror("Error",f"due to:{str(es)}",parent = self.root)


    # ==========================
    def get_cursor(self,event=""):
       cursor_row=self.student_table.focus()
       content = self.student_table.item(cursor_row)
       rows = content['values']
       self.var_atten_id.set(rows[0])
       self.var_atten_roll.set(rows[1])
       self.var_atten_name.set(rows[2])
       self.var_atten_time.set(rows[3])
       self.var_atten_date.set(rows[4])
       self.var_atten_attendance.set(rows[5])
    
    def reset_data(self):
       self.var_atten_id.set("")
       self.var_atten_roll.set("")
       self.var_atten_name.set("")
       self.var_atten_time.set("")
       self.var_atten_date.set("")
       self.var_atten_attendance.set("")
    
       



if __name__ == "__main__":
    root = Tk()
    obj = attendance(root)
    root.mainloop() 
