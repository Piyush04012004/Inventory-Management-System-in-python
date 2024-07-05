from tkinter import*
from PIL import Image, Image #pip install pillow 
from tkinter import ttk,messagebox
import sqlite3
class SupplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+200+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        #=========================
        # All variables======
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_supID=StringVar()
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_desc=StringVar()
        

         #==========searchframe=====

         #====options====
        lbl_search=Label(self.root,text="Search by Invoice No.",bg="white",font=("goudy old style",15))
        lbl_search.place(x=650,y=60)
        

        txt_search=Entry(self.root,textvariable=self.var_searchtxt ,font=("goudy old style",15),bg="lightyellow").place(x=830,y=60,width=140)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=980,y=60,width=80,height=30)

        #======title===========
        title=Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold"),bg= "#0f4d7d", fg ="white").place(x=50,y=10,width=1000,height=40)

        #====content====
        #=====row1===
        
        lbl_Supid=Label(self.root,text="Supplier ID",bg="white",font=("goudy old style",15)).place(x=50,y=60)
        txt_supplier_Id=Entry(self.root, textvariable=self.var_supID,font=("goudy old style",15),bg="lightyellow").place(x=180,y=60,width=180)

        lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=50,y=100)
       
        txt_supplier_invoice=Entry(self.root, textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=180,y=100,width=180)
        
        #=====row2=====
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=150)
        txt_name=Entry(self.root, textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=180,y=150,width=180)
       
        #=====row3=====
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=200)
        txt_contact=Entry(self.root, textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=180,y=200,width=180)
      
        #=====row4=====
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=250)
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=180,y=250,width=400,height=120)
       

        #===buttons====
        btn_add=Button(self.root,text="Save",command=self.add, font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=100,y=400,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=220,y=400,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=340,y=400,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=460,y=400,width=110,height=28)

        #======Supplier Details===
        sup_frame=Frame(self.root,bd=3, relief=RIDGE)
        sup_frame.place(x=600,y=100,width=450,height=350)

        scrolly=Scrollbar(sup_frame,orient=VERTICAL)
        scrollx=Scrollbar(sup_frame,orient=HORIZONTAL)

        self.SupplierTable=ttk.Treeview(sup_frame,columns=("sup_id","invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        self.SupplierTable.heading("sup_id",text="SUPPLIER ID")
        self.SupplierTable.heading("invoice",text="INVOICE")
        self.SupplierTable.heading("name",text="NAME")
        self.SupplierTable.heading("contact",text="CONTACT")
        self.SupplierTable.heading("desc",text="DESCRIPTION]")
        self.SupplierTable["show"]="headings"
        
        self.SupplierTable.column("sup_id",width=80)
        self.SupplierTable.column("invoice",width=60)
        self.SupplierTable.column("name",width=100)
        self.SupplierTable.column("contact",width=90)
        self.SupplierTable.column("desc",width=120)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)


        self.show()

#===============================================================================================
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice must be required", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "This invoice number is already assigned, try different.")
                else:
                    cur.execute("insert into supplier (sup_id,invoice, name, contact, desc) values (?, ?, ?, ?, ?)",(
                             self.var_supID.get(),
                             self.var_sup_invoice.get(),
                             self.var_name.get(),
                             self.var_contact.get(),
                             self.txt_desc.get('1.0', END)
                    ))
                con.commit()
                messagebox.showinfo("Success", "Supplier added successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
        finally:
            con.close()

    
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        #print(row)
        self.var_supID.set(row[0]),
        self.var_sup_invoice.set(row[1]),
        self.var_name.set(row[2]),
        self.var_contact.set(row[3]),
        self.var_desc.set(row[4])
        
    def update(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                if self.var_sup_invoice.get()=="":
                    messagebox.showerror("Error","Invoice number Must be required", parent=self.root)
                else:
                    cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice number", parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                                            self.var_supID.get(),
                                            self.var_name.get(),
                                            self.var_contact.get(),
                                            self.var_desc.get(),
                                            self.var_sup_invoice.get(),            
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess", "Supplier updated Successfully",parent=self.root)
                    self.show()

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to:{str(ex)}")
    
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice number Must be required", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid invoice number", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                      cur.execute("delete from supplier where invoice=?", (self.var_sup_invoice.get(),))
                      con.commit()
                    messagebox.showinfo("Delete", "Supplier Deleted Sucessfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")
    def clear(self):
        self.var_sup_invoice.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.var_desc.set("Select"),
        self.var_searchtxt.set(""),
        self.var_searchby.set("Select"),
        self.show()

    
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice number should be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record found!!",parent=self.root)
        except EXCEPTION as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=SupplierClass(root)
    root.mainloop()
                    







