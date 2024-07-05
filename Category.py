from tkinter import*
from PIL import Image, ImageTk #pip install pillow 
from tkinter import ttk,messagebox
import sqlite3
class CategoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+200+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
         
         #Variables

        self.var_cat_ID = StringVar()
        self.var_cat_name = StringVar()
 
         #Title

        lbl_title=Label(self.root,text="Manage Product Category",font=("Calibri",30),bg="#184a45",fg="white",bd=3,relief="ridge").pack(side=TOP,fill=X,padx=10,pady=10)
        lbl_C_id=Label(self.root,text="Enter the Product Category ID",font=("goudy old style",18),bg="white").place(x=50,y=80)
        txt_Cname=Label(self.root,text="Enter the Product Category",font=("goudy old style",18),bg="white").place(x=50,y=120)
        txt_C_id=Entry(self.root,textvariable=self.var_cat_ID,font=("goudy old style",18),bg="lightyellow").place(x=350,y=80,width=250)
        txt_Cname=Entry(self.root,textvariable=self.var_cat_name,font=("goudy old style",18),bg="lightyellow").place(x=350,y=120,width=250)
        
         # Buttons
        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",18),bg="#4caf50",fg="white",cursor="hand2").place(x=240,y=170,width=100,height=30)
        btn_del=Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",18),bg="#72b72d",fg="white",cursor="hand2").place(x=360,y=170,width=100,height=30)
       
  # Catego0ry details
        
        cat_frame=Frame(self.root,bd=3, relief=RIDGE)
        cat_frame.place(x=700,y=80,width=380,height=120)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.CategoryTable=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)
        self.CategoryTable.heading("cid",text="CATEGORY ID")
        self.CategoryTable.heading("name",text="NAME")
        self.CategoryTable["show"]="headings"
        self.CategoryTable.column("cid",width=90)
        self.CategoryTable.column("name",width=100)
        self.CategoryTable.pack(fill=BOTH,expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>",self.get_data)
        
        # Image1
        self.Im1 = Image.open("Images/category1.jpg")
        self.Im1 = self.Im1.resize((500, 250))
        self.Im1 = ImageTk.PhotoImage(self.Im1)

        self.lbl_Im1 = Label(self.root, image=self.Im1, bd=2, relief=RAISED)
        self.lbl_Im1.place(x=30, y=210)
        
        #Image2
      
        self.Im2 = Image.open("Images/category2.jpg")
        self.Im2 = self.Im2.resize((500, 250))
        self.Im2 = ImageTk.PhotoImage(self.Im2)
        
        self.lbl_Im2 = Label(self.root, image=self.Im2, bd=2, relief=RAISED)
        self.lbl_Im2.place(x=560, y=210)

        self.show()

 ########################################################################################################################       
    def add(self):
          con = sqlite3.connect(database=r'ims.db')
          cur = con.cursor()
          try:
             if self.var_cat_name.get() == "":
                    messagebox.showerror("Error", "Category name should be required", parent=self.root)

             cur.execute("SELECT * FROM category WHERE name=?", (self.var_cat_name.get(),))
             row = cur.fetchone()
             if row is not None:
                    messagebox.showerror("Error","This Category already assigned, try different name", parent=self.root)
             else:
                    cur.execute("INSERT INTO category (name) VALUES (?)", (self.var_cat_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Category added Successfully", parent=self.root)
                    self.show()
          except Exception as ex:
              messagebox.showerror("Error", f"Error due to: {str(ex)}")
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)   

    def get_data(self,ev):
        f=self.CategoryTable.focus()
        content=(self.CategoryTable.item(f))
        row=content['values']
        #print(row)
        self.var_cat_ID.set(row[0]),
        self.var_cat_name.set(row[1])     

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_name.get()=="":
                messagebox.showerror("Error","Please select Category from the list", parent=self.root)
            else:
                cur.execute("select * from category where name=?",(self.var_cat_name.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Category name", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                      cur.execute("delete from category where name=?", (self.var_cat_name.get(),))
                      con.commit()
                    messagebox.showinfo("Delete", "Category Deleted Sucessfully", parent=self.root)
                    self.show()
                    self.var_cat_ID.set("")
                    self.var_cat_name.set("")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")       


if __name__=="__main__":
    root=Tk()
    obj=CategoryClass(root)
    root.mainloop()