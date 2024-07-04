from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from dashboard import IMS
import sqlite3

class Admin:
    def __init__(self, root):
        self.root = root
        self.root.title("Login system")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
    
        self.phone_image = ImageTk.PhotoImage(file="Images/phone.png")
        self.lbl_phone_image = Label(self.root, image=self.phone_image, bd=0).place(x=200, y=10)
        
        login_frame = Frame(self.root, bd=2, relief="ridge", bg='white')
        login_frame.place(x=680, y=120, width=350, height=400)
        title = Label(login_frame, text="Login System", font=("Elephant", 30, "bold")).place(x=0, y=20, relwidth=1)
        lbl_user_name = Label(login_frame, text="User Name", font=("Andalus", 15), bg="white", fg="#767171").place(x=40, y=90)
        self.user_name = StringVar()
        self.user_password = StringVar()
        txt_username = Entry(login_frame, textvariable=self.user_name, font=("times New Roman", 15), bg="#ECECEC").place(x=40, y=130)
        
        lbl_user_password = Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171").place(x=40, y=170)
        txt_user_password = Entry(login_frame, textvariable=self.user_password, font=("times New Roman", 15), bg="#ECECEC", show='*').place(x=40, y=220)
        
        btn_login = Button(login_frame, command=self.login, text="Log In", font=("Arial rounded MT Bold", 15), bg="#00B0F0", activebackground="white", fg="white", cursor="hand2").place(x=40, y=270, width=250, height=35)
        
        hr = Label(login_frame, bg="lightgray").place(x=40, y=320, width=250, height=2)
        or_ = Label(login_frame, text="OR", font=("Times new Roman", 15), bg="white", fg="darkgray").place(x=150, y=320)
        
        btn_forget = Button(login_frame, text="Forgot Password?", font=("Times new roman", 15), bd=0, bg="white", fg="black", cursor="hand2").place(x=90, y=350)
        
        register_frame = Frame(self.root, bd=2, relief="ridge", bg="white")
        register_frame.place(x=680, y=540, width=350, height=60)
     
        lbl_register = Label(register_frame, text="Don't have an account?", font=("Times new roman", 13, "bold"), bg="white").place(x=40, y=15)
        btn_sign_up = Button(register_frame, command=self.open_signup_window, text="Sign up", font=("Times new roman", 13, "bold"), bd=0, bg="white", fg="#00759E", activebackground="white", activeforeground="#00759E").place(x=220, y=15)
        
        self.im1 = ImageTk.PhotoImage(file="Images/im1.png")
        self.im2 = ImageTk.PhotoImage(file="Images/im2.png")
        self.im3 = ImageTk.PhotoImage(file="Images/im3.png")
        
        self.lbl_change_image = Label(self.root, bg="white")
        self.lbl_change_image.place(x=408, y=150, width=232, height=420)
        self.animate()
        
    def animate(self):
        self.im1, self.im2, self.im3 = self.im2, self.im3, self.im1
        self.lbl_change_image.config(image=self.im1)
        self.lbl_change_image.after(2000, self.animate)
    
    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
             if self.user_name.get() == "" or self.user_password.get() == "":
                 messagebox.showerror("Error", "All fields are required")
             elif self.user_name.get() != self.user_name or self.user_password.get() != self.user_password:
                 messagebox.showerror("Error", "Invalid user name or password! Try again with correct credentials")
             elif self.user_name.get() == self.user_name or self.user_password.get() == self.user_password:
                 messagebox.showinfo("Information", f"Welcome: {self.user_name.get()}\nYour password: {self.user_password.get()}")    
    
             elif self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All fields are reqiured", parent=self.root)
             else:
                cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid USERNAME/PASSWORD", parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system(" python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")

        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    

       
    def open_signup_window(self):
        signup_window = Toplevel(self.root)
        signup_window.title("Signup Page")
        signup_window.geometry("400x300")

        Label(signup_window, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        entry_username = Entry(signup_window)
        entry_username.grid(row=0, column=1, padx=10, pady=10)

        Label(signup_window, text="Password:").grid(row=1, column=0, padx=10, pady=10)
        entry_password = Entry(signup_window, show="*")
        entry_password.grid(row=1, column=1, padx=10, pady=10)

        Label(signup_window, text="Email:").grid(row=2, column=0, padx=10, pady=10)
        entry_email = Entry(signup_window)
        entry_email.grid(row=2, column=1, padx=10, pady=10)

        Button(signup_window, text="Signup", command=lambda: self.signup(entry_username, entry_password, entry_email)).grid(row=3, column=0, columnspan=2, pady=10)

    def signup(self, entry_username, entry_password, entry_email):
        username = entry_username.get()
        password = entry_password.get()
        email = entry_email.get()
        
        if username and password and email:
            # Here you can add the logic to save the details or process them as needed
            messagebox.showinfo("Signup", "Signup successful!")
        else:
            messagebox.showwarning("Signup", "Please fill out all fields.")
                    
root = Tk()
obj = Admin(root)
root.mainloop()
