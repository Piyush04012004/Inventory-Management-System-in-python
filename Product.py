from tkinter import*
from PIL import Image, Image #pip install pillow 
from tkinter import ttk,messagebox
import sqlite3
class ProductClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+200+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        #Variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_pid=IntVar()
        self.var_category=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_supplier=StringVar()
        self.var_product_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()

     #Product Frame
        product_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=450,height=480)
     
      #======title===========
        title=Label(product_frame,text="Product Details",font=("goudy old style",18,"bold"),bg= "#0f4d7d", fg ="white").pack(side=TOP,fill=X)
        lbl_product_Id=Label(product_frame,text="Product Id :",font=("goudy old style",18,"bold"),bg= "white").place(x=30,y=60)
        lbl_category=Label(product_frame,text="Category :",font=("goudy old style",18,"bold"),bg= "white").place(x=30,y=100)
        lbl_supplier=Label(product_frame,text="Supplier :",font=("goudy old style",18,"bold"),bg= "white").place(x=30,y=140)
        lbl_product_name=Label(product_frame,text="Product Name :",font=("goudy old style",18,"bold"),bg= "white").place(x=30,y=180)
        lbl_price=Label(product_frame,text="Price :",font=("goudy old style",18,"bold"),bg= "white").place(x=30,y=220)
        lbl_quantity=Label(product_frame,text="Quantity :",font=("goudy old style",18,"bold"),bg= "white").place(x=30,y=260)
        lbl_status=Label(product_frame,text="Status :",font=("goudy old style",18,"bold"),bg= "white").place(x=30,y=300) 
        
        #options
        txt_product_Id = Entry(product_frame,textvariable=self.var_pid,font=("goudy old style",15),bg="lightyellow").place(x=200,y=60,width=180)
        cmb_cat = ttk.Combobox(product_frame,textvariable=self.var_category,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=200,y=100,width=180)
        cmb_cat.current(0)

        cmb_supplier = ttk.Combobox(product_frame,textvariable=self.var_supplier,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_supplier.place(x=200,y=140,width=180)
        cmb_supplier.current(0)

        txt_product_name = Entry(product_frame,textvariable=self.var_product_name,font=("goudy old style",15),bg="lightyellow").place(x=200,y=180,width=180)
        txt_price = Entry(product_frame,textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow").place(x=200,y=220,width=180)
        
        txt_quantity = Entry(product_frame,textvariable=self.var_quantity,font=("goudy old style",15),bg="lightyellow").place(x=200,y=260,width=180)
        

        cmb_status = ttk.Combobox(product_frame,textvariable=self.var_status,values=("select","Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=200,y=300,width=180)
        cmb_status.current(0) 

        #Button
        btn_add = Button(product_frame,text="Save",command=self.add, font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update = Button(product_frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete = Button(product_frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear = Button(product_frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)
        

        
        SearchFrame=LabelFrame(self.root,text="Search Product details",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)

         #====options=====
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("select","Category","Supplier","name"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt ,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)
             
         # Product Details

        p_frame=Frame(self.root,bd=3, relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.ProductTable=ttk.Treeview(p_frame,columns=("pid","Category","Supplier","name","price","quantity","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.heading("pid",text="P ID")
        self.ProductTable.heading("Category",text="Category")
        self.ProductTable.heading("Supplier",text="Supplier")
        self.ProductTable.heading("name",text="Name")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("quantity",text="Quantity")
        self.ProductTable.heading("status",text="Status")
       
        self.ProductTable["show"]="headings"

        self.ProductTable.column("pid",width=90)
        self.ProductTable.column("Category",width=100)
        self.ProductTable.column("Supplier",width=100)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("quantity",width=100)
        self.ProductTable.column("status",width=100)
       
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)


        self.show()

#####################################################################################################################
    def fetch_cat_sup(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select name from category")
            cat=cur.fetchall()
            self.cat_list.append("Empty")
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("select")
                for i in cat:
                    self.cat_list.append(i[0]) 
            
            cur.execute("select name from supplier")
            sup=cur.fetchall()
            self.sup_list.append("Empty")
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("select")
                for i in sup:
                    self.sup_list.append(i[0])
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")
    
    
    
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_category.get()=="select" or self.var_supplier.get()=="select" or self.var_product_name.get()=="":
                messagebox.showerror("Error","All fields are required", parent=self.root)
            else:
                cur.execute("select * from Product where name=?",(self.var_product_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product already present, add differnt")
                else:
                    cur.execute("Insert into  Product (pid,Category,Supplier,name,price,quantity,status)values(?,?,?,?,?,?,?)",(
                                            self.var_pid.get(),
                                            self.var_category.get(),
                                            self.var_supplier.get(),
                                            self.var_product_name.get(),
                                            self.var_price.get(),
                                            self.var_quantity.get(),
                                            self.var_status.get(),
                                ))
                    con.commit()
                    messagebox.showinfo("Sucess", "Product added Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")
    
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from Product")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_category.set(row[1]),
        self.var_supplier.set(row[2]),
        self.var_product_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_quantity.set(row[5]),
        self.var_status.set(row[6])      
    
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","please select product of any category from the list !!", parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid product ID", parent=self.root)
                else:
                    cur.execute("Update Product set Category=?,Supplier=?,name=?,price=?,quantity=?,status=? where pid=?",(
                                
                                            self.var_category.get(),
                                            self.var_supplier.get(),
                                            self.var_product_name.get(),
                                            self.var_price.get(),
                                            self.var_quantity.get(),
                                            self.var_status.get(),
                                            self.var_pid.get()
                                                   
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess", "Product details updated Successfully",parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")
    
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Product ID Must be required", parent=self.root)
            else:
                cur.execute("select * from Product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product ID", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                      cur.execute("delete from Product where pid=?", (self.var_pid.get(),))
                      con.commit()
                    messagebox.showinfo("Delete", "Product Deleted Sucessfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")
    def clear(self):
        self.var_category.get(),
        self.var_supplier.get(),
        self.var_product_name.get(),
        self.var_price.get(),
        self.var_quantity.get(),
        self.var_status.get(),
        self.var_pid.get()                                     
        self.show()

    
    
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="Select":
                messagebox.showerror("Error","Select Search By option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            
            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=None:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record found!!",parent=self.root)
        except EXCEPTION as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)




if __name__=="__main__":
    root=Tk()
    obj=ProductClass(root)
    root.mainloop()