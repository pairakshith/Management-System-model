from enum import IntEnum
from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from tkinter.font import BOLD
import mysql.connector
import mysql.connector
from mysql.connector.catch23 import make_abc
from mysql.connector.fabric import connect


class hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("HOSPITAL MANAGEMENT SYSTEM")
        self.root.geometry("1540x800+0+0")

        self.Name=StringVar()
        self.Ref=StringVar()
        self.Dose=StringVar()
        self.tablets=StringVar()
        self.lot=StringVar()
        self.issue=StringVar()
        self.expiry=StringVar()
        self.sideeffect=StringVar()
        self.bloodpressure=StringVar()
        self.storage=StringVar()
        self.pid=StringVar()
        self.DoB=StringVar()
        self.Pname=StringVar()
        self.paddrs=StringVar()
        self.suggestion=StringVar()
        
        labelTitle=Label(self.root,bd=21,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",
        fg="red",bg="black",font=("times new roman",50,BOLD))
        labelTitle.pack(side=TOP,fill=X) #adjust title in X axis

        # ---------------DataFrame--------------- #
        
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=120,width=1530,height=400)


        LeftDataFrame=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
        font=("times new roman",15,BOLD),text="Patient Information")
        LeftDataFrame.place(x=0,y=7,width=980,height=350)

        RightDataFrame=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
        font=("times new roman",15,BOLD),text="Details ")
        RightDataFrame.place(x=990,y=7,width=500,height=350)

        # ---------------ButtonsFrame--------------- #
        
        buttonframe=Frame(self.root,bd=10,relief=RIDGE)
        buttonframe.place(x=0,y=500,width=1530,height=60)
       
       
        # ---------------DetailsFrame--------------- #
        
        Detailsframe=Frame(self.root,bd=10,relief=RIDGE)
        Detailsframe.place(x=0,y=560,width=1530,height=230)

        # ---------------LeftSection information--------------- #

        tabletsName=Label(LeftDataFrame,text="Name of the Tablet",font=("times new roman",12,BOLD),padx=2,pady=6)
        tabletsName.grid(row=0,column=0)
        tabletcombo=ttk.Combobox(LeftDataFrame,font=("times new roman",12,BOLD),state="readonly",textvariable=self.Name,width=33)
        tabletcombo["values"]=("Paracetomol","Dolo 650","Crocin","Anacin")
        tabletcombo.grid(row=0,column=1)

        referenceNumber=Label(LeftDataFrame,text="Reference Number",font=("times new roman",12,BOLD),padx=2,pady=6)
        referenceNumber.grid(row=1,column=0)
        referenceNumberEntry=Entry(LeftDataFrame,font=("times new roman",12,BOLD),textvariable=self.Ref,width=35)
        referenceNumberEntry.grid(row=1,column=1)

        Doses=Label(LeftDataFrame,text="Doses",font=("times new roman",12,BOLD),padx=2,pady=6)
        Doses.grid(row=2,column=0)
        DosesEntry=Entry(LeftDataFrame,font=("times new roman",12,BOLD),textvariable=self.Dose,width=35)
        DosesEntry.grid(row=2,column=1)

        NumberofTablets=Label(LeftDataFrame,text="Number of Tablets ",font=("times new roman",12,BOLD),padx=2,pady=6)
        NumberofTablets.grid(row=3,column=0)
        NumberofTabletsEntry=Entry(LeftDataFrame,font=("times new roman",12,BOLD),textvariable=self.tablets,width=35)
        NumberofTabletsEntry.grid(row=3,column=1)

        LotNumber=Label(LeftDataFrame,text="Lot Number ",font=("times new roman",12,BOLD),padx=2,pady=6)
        LotNumber.grid(row=4,column=0)
        LotNumberEntry=Entry(LeftDataFrame,font=("times new roman",12,BOLD),textvariable=self.lot,width=35)
        LotNumberEntry.grid(row=4,column=1)

        IssueDate=Label(LeftDataFrame,text="Issue Date ",font=("times new roman",12,BOLD),padx=2,pady=6)
        IssueDate.grid(row=5,column=0)
        IssueDateEntry=Entry(LeftDataFrame,font=("times new roman",12,BOLD),textvariable=self.issue,width=35)
        IssueDateEntry.grid(row=5,column=1)
        

        ExpiryDate=Label(LeftDataFrame,text="Expiry Date (MM/YY)",font=("times new roman",12,BOLD),padx=2,pady=6)
        ExpiryDate.grid(row=6,column=0)
        ExpiryDateEntry=Entry(LeftDataFrame,font=("times new roman",12,BOLD),textvariable=self.expiry,width=35)
        ExpiryDateEntry.grid(row=6,column=1)

        sideEffect=Label(LeftDataFrame,text="Side Effect ",font=("times new roman",12,BOLD),padx=2,pady=6)
        sideEffect.grid(row=7,column=0)
        sideEffectEntry=Entry(LeftDataFrame,font=("times new roman",12,BOLD),textvariable=self.sideeffect,width=35)
        sideEffectEntry.grid(row=7,column=1)

        BloodPressure=Label(LeftDataFrame,text="Blood Pressure ",font=("times new roman",12,BOLD),padx=2,pady=6)
        BloodPressure.grid(row=0,column=2)
        BloodPressureEntry=Entry(LeftDataFrame,font=("times new roman",12,BOLD),textvariable=self.bloodpressure,width=35)
        BloodPressureEntry.grid(row=0,column=3)

        storage=Label(LeftDataFrame,text="Storage Place ",font=("times new roman",12,BOLD),padx=2,pady=6)
        storage.grid(row=1,column=2)
        storageEntry=ttk.Combobox(LeftDataFrame,font=("times new roman",12,BOLD),textvariable=self.storage,width=33)
        storageEntry["values"]=("Cool and dry","Refrigerator","Low Light","Do not expose to Direct Sun light")
        storageEntry.grid(row=1,column=3)

        patientID=Label(LeftDataFrame,text="Patient ID ",font=("times new roman",12,BOLD),padx=2,pady=6)
        patientID.grid(row=2,column=2)
        patientIDEntry=Entry(LeftDataFrame,font=("times new roman",12,BOLD),textvariable=self.pid,width=35)
        patientIDEntry.grid(row=2,column=3)

        DoB=Label(LeftDataFrame,text="Date Of Birth  ",font=("times new roman",12,BOLD),padx=2,pady=6)
        DoB.grid(row=3,column=2)
        DoBEntry=Entry(LeftDataFrame,font=("times new roman",12,BOLD),textvariable=self.DoB,width=35)
        DoBEntry.grid(row=3,column=3)

        patientName=Label(LeftDataFrame,text="Patient Name ",font=("times new roman",12,BOLD),padx=2,pady=6)
        patientName.grid(row=4,column=2)
        patientNameEntry=Entry(LeftDataFrame,font=("times new roman",12,BOLD),textvariable=self.Pname,width=35)
        patientNameEntry.grid(row=4,column=3)

        suggestion=Label(LeftDataFrame,text="Suggestion ",font=("times new roman",12,BOLD),padx=2,pady=6)
        suggestion.grid(row=5,column=2)
        suggestionEntry=Entry(LeftDataFrame,font=("times new roman",12,BOLD),textvariable=self.suggestion,width=35)
        suggestionEntry.grid(row=5,column=3)
        
        #entry is replaced here with text for testing

        patientAddress=Label(LeftDataFrame,text="Patient address ",font=("times new roman",12,BOLD),padx=2,pady=6)
        patientAddress.grid(row=6,column=2)
        patientAddressEntry=Entry(LeftDataFrame,font=("times new roman",12,BOLD),textvariable=self.paddrs,width=35)
        #Text(LeftDataFrame,font=("times new roman",12,BOLD),width=35,height=3,pady=1,padx=2)
        patientAddressEntry.grid(row=6,column=3)
        
        # ---------------Prescription Section--------------- #

        self.prescriptionText=Text(RightDataFrame,font=("times new roman",12,BOLD),width=56,height=16,padx=3,pady=6)
        self.prescriptionText.grid(row=0,column=0)


        # ----------------Table buttons-------------- #

        DetailsButton=Button(buttonframe,command=self.idetails,text="Details",bg="Black",fg="White",font=("times new roman",12,BOLD),width=25,height=1,padx=2,pady=6)
        DetailsButton.grid(row=0,column=0)

        AddButton=Button(buttonframe,text="Add ",bg="Black",fg="White",font=("times new roman",12,BOLD),command=self.iadd,width=25,height=1,padx=2,pady=6)
        AddButton.grid(row=0,column=1) 

        UpdateButton=Button(buttonframe,text="Update",bg="Black",fg="White",font=("times new roman",13,BOLD),command=self.iupdate,width=25,height=1,padx=2,pady=6)
        UpdateButton.grid(row=0,column=2)

        DeleteButton=Button(buttonframe,text="Delete",bg="Black",fg="White",font=("times new roman",13,BOLD),command=self.idelete,width=25,height=1,padx=2,pady=6)
        DeleteButton.grid(row=0,column=3)

        ClearButton=Button(buttonframe,command=self.iclear,text="Clear",bg="Black",fg="White",font=("times new roman",13,BOLD),width=25,height=1,padx=2,pady=6)
        ClearButton.grid(row=0,column=4)

        ExitButton=Button(buttonframe,command=self.iexit,text="Exit",bg="Black",fg="White",font=("times new roman",13,BOLD),width=24,height=1,padx=2,pady=6)
        ExitButton.grid(row=0,column=5)

        #------------------------Scrolls----------------------#
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)

        self.hospital_table=ttk.Treeview(Detailsframe,column=("Name","Ref","Dose","tablets","lot","issue","expiry","sideeffect","bloodpressure",
        "storage","pid","DoB","Pname","paddrs","suggestion"),
        xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)#setting scroll bar
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)


        self.hospital_table.heading("Name",text="Tablet name")
        self.hospital_table.heading("Ref",text="Ref Number")
        self.hospital_table.heading("Dose",text="Dose")
        self.hospital_table.heading("tablets",text="Tablet no")
        self.hospital_table.heading("lot",text="Lot no")
        self.hospital_table.heading("issue",text="Issue Date")
        self.hospital_table.heading("expiry",text="Expiry Date" )
        self.hospital_table.heading("sideeffect",text="Side Effect")
        self.hospital_table.heading("bloodpressure",text="Blood Pressure")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("pid",text="ID")
        self.hospital_table.heading("Pname",text="Patient Name")
        self.hospital_table.heading("DoB",text="Date of Birth")
        self.hospital_table.heading("paddrs",text="Address")
        self.hospital_table.heading("suggestion",text="Suggestion")
 

        self.hospital_table["show"]="headings"

        self.hospital_table.column("Name",width=100)
        self.hospital_table.column("Ref",width=100)
        self.hospital_table.column("Dose",width=100)
        self.hospital_table.column("tablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issue",width=100)
        self.hospital_table.column("expiry",width=100)
        self.hospital_table.column("sideeffect",width=100)
        self.hospital_table.column("bloodpressure",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("pid",width=100)
        self.hospital_table.column("Pname",width=100)
        self.hospital_table.column("DoB",width=100)
        self.hospital_table.column("paddrs",width=100)
        self.hospital_table.column("suggestion",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetchdata()

    #-----------------------functionality declaration-------------
    def iadd(self):
        if self.Name.get()=="" or self.Ref.get()=="":
            messagebox.showerror("Data Error","Enter Valid Data")
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='password',database='mydata')
            my_cursor=conn.cursor()   
            my_cursor.execute("insert into hospital values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.Name.get(),self.Ref.get(),self.Dose.get(),self.tablets.get(),
            self.lot.get(),self.issue.get(),self.expiry.get(),self.sideeffect.get(),
            self.bloodpressure.get(),self.storage.get(),self.pid.get(),
            self.Pname.get(),self.DoB.get(),self.paddrs.get(),self.suggestion.get()))
            conn.commit()
            self.fetchdata()
            self.prescriptionText.delete("1.0",END)
            conn.close()
            messagebox.showinfo("Success","Data has been INSERTED Successfully")
            self.idetails()
    
    def fetchdata(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='password',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in row:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=''):
        rowcursor=self.hospital_table.focus()
        content=self.hospital_table.item(rowcursor)
        rows=content["values"]
        self.Name.set(rows[0])
        self.Ref.set(rows[1])
        self.Dose.set(rows[2])
        self.tablets.set(rows[3])
        self.lot.set(rows[4])
        self.issue.set(rows[5])
        self.expiry.set(rows[6])
        self.sideeffect.set(rows[7])
        self.bloodpressure.set(rows[8])
        self.storage.set(rows[9])
        self.pid.set(rows[10])
        self.Pname.set(rows[11])
        self.DoB.set(rows[12])
        self.paddrs.set(rows[13])
        self.suggestion.set(rows[14])

    def iupdate(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='password',database='mydata')
        my_cursor=conn.cursor()  
        my_cursor.execute("update hospital set name_of_tablets=%s,Doses=%s, Number_of_tablets=%s, lot_number=%s,issuedate=%s, expiry_date=%s, side_effect=%s, blood_pressure=%s, storage=%s, Patient_ID=%s, date_of_birth=%s, Patient_Name=%s, address=%s, suggestion=%s where reference_number=%s",(
            self.Name.get(),self.Dose.get(),self.tablets.get(),
            self.lot.get(),self.issue.get(),self.expiry.get(),self.sideeffect.get(),
            self.bloodpressure.get(),self.storage.get(),self.pid.get(),
            self.Pname.get(),self.DoB.get(),self.paddrs.get(),self.suggestion.get(),self.Ref.get()
            ))
        
        conn.commit()
        self.fetchdata()
        self.prescriptionText.delete("1.0",END)
        self.idetails()
        
        conn.close()
        messagebox.showinfo("Update","Record Updated Succesfully!!!")

    def idelete(self):
        askdelete=messagebox.askyesno("WARNING","This Record Will be DELETED Permanently")
        if askdelete>0:
            conn=mysql.connector.connect(host='localhost',user='root',password='password',database='mydata')
            my_cursor=conn.cursor()
            query="delete from hospital where reference_number=%s"
            value=(self.Ref.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            conn.close()
            self.fetchdata()
            messagebox.showinfo("DELETE","Record Deleted Successfully")

    def idetails(self):
        self.prescriptionText.insert(END,"Name of Tablet :   "+self.Name.get()+'\n')
        self.prescriptionText.insert(END,"Reference Number :   "+self.Ref.get()+'\n')
        self.prescriptionText.insert(END,"Dosage :   "+self.Dose.get()+'\n')
        self.prescriptionText.insert(END,"Number of Tablet :   "+self.tablets.get()+'\n')
        self.prescriptionText.insert(END,"Lot Number :   "+self.lot.get()+'\n')
        self.prescriptionText.insert(END,"Issue Date :   "+self.issue.get()+'\n')
        self.prescriptionText.insert(END,"Expiry Date :   "+self.expiry.get()+'\n')
        self.prescriptionText.insert(END,"Side Effect :   "+self.sideeffect.get()+'\n')
        self.prescriptionText.insert(END,"Blood Pressure :   "+self.bloodpressure.get()+'\n')
        self.prescriptionText.insert(END,"Starage :   "+self.storage.get()+'\n')
        self.prescriptionText.insert(END,"Patient ID :   "+self.pid.get()+'\n')
        self.prescriptionText.insert(END,"Date of Birth :   "+self.DoB.get()+'\n')
        self.prescriptionText.insert(END,"Patient Name :   "+self.Pname.get()+'\n')
        self.prescriptionText.insert(END,"Suggestion :   "+self.suggestion.get()+'\n')
        self.prescriptionText.insert(END,"Patient Address :   "+self.paddrs.get()+'\n')


    def iclear(self):
        self.Name.set("")
        self.Ref.set("")
        self.Dose.set("")
        self.tablets.set("")    
        self.lot.set("")
        self.issue.set("")

        self.expiry.set("")
        self.sideeffect.set("")
        self.bloodpressure.set("")
        self.storage.set("")
        self.pid.set("")
        self.Pname.set("")
        self.DoB.set("")
        self.paddrs.set("")
        self.suggestion.set("")
        self.prescriptionText.delete("1.0",END)

    def iexit(self):
        isexit=messagebox.askyesno("Hospital Management System","Exit")
        if isexit>0:
            root.destroy()
            return

root=Tk()
ob= hospital(root)
root.mainloop()
