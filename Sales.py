import os
from tkinter import*
from PIL import Image, ImageTk #pip install pillow 
from tkinter import ttk,messagebox
import sqlite3
class SalesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+200+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #Variables
        self.bill_list=[]
        self.var_invoice = StringVar()

        #title
        lbl_title=Label(self.root,text="Veiw Customer Bills",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,pady=20)
        #labels
        lbl_invoice=Label(self.root,text="Invoice Number",font=("times new roman",15),bg="white").place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg="light yellow").place(x=200,y=100,width=160,height=28)
    

        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15,"bold"),bg="#2196f3",fg="black",bd=2,cursor="hand2").place(x=380,y=100,width=120,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="light blue",fg="black",bd=2,cursor="hand2").place(x=510,y=100,width=120,height=28)
        
        
            #sales Frame
        
        sales_frame=Label(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=50,y=140,width=200,height=330)

            #Sales List

        scrolly=Scrollbar(sales_frame,orient="vertical")
        self.sales_list=Listbox(sales_frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.getdata)

            #Bill Area
        bill_frame=Label(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=280,y=140,width=410,height=330)

        lbl_title2 = Label(bill_frame,text="Customer Bill Area",font=("Arial Black",15,"bold"),bg="orange",fg="red").pack(side=TOP,fill=X)
        scrolly_2=Scrollbar(bill_frame,orient="vertical")
        self.bill_area=Text(bill_frame,bg="light yellow",yscrollcommand=scrolly_2.set)
        scrolly_2.pack(side=RIGHT,fill=Y)
        scrolly_2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)

          #Image
        self.bill_photo1 = Image.open("Images/cat2.jpg")
        self.bill_photo1 = self.bill_photo1.resize((450, 300))
        self.bill_photo1 = ImageTk.PhotoImage(self.bill_photo1)
        
        lbl_image1 = Label(self.root,image=self.bill_photo1,bd=0)
        lbl_image1.place(x=700,y=120)

        self.show()
           

######################################################################################################################

    def show(self):
        del self.bill_list[:]
        self.sales_list.delete
        for i in os.listdir('bill'):
            if i.split('.')[1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])


    def getdata(self,ev):
        index_=self.sales_list.curselection()
        file_name=self.sales_list.get(index_)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice number should be required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid invoice number",parent=self.root)
    def clear(self):
        self.bill_area.delete('1.0',END)            

if __name__=="__main__":
    root=Tk()
    obj=SalesClass(root)
    root.mainloop()        