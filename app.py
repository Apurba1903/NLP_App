from tkinter import *

class NLPApp:
    
    def __init__(self):
        
        # Login GUI Load
        self.root = Tk()
        self.root.title('NLP App')
        self.root.iconbitmap('recources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#283747')
        
        self.login_gui()
        
        self.root.mainloop()
    
    
    # Login GUI Code
    def login_gui(self):
        
        heading = Label(self.root, text='NLP App', bg='#283747', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure( font=('verdana', 24, 'bold'))
        
        
        # Login Email
        label1 = Label(self.root, text='Enter Email', bg='#f0f0f0', fg='#333333' , font=('verdana', 10, 'bold'), anchor='w')
        label1.pack(fill='x', padx=60, pady=(10, 0),ipady=4, anchor='w')

        self.email_input = Entry(self.root, width=40, bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da')
        self.email_input.pack(pady=(5, 10), ipady=4, padx=60, anchor='w', fill='x')


        # Login Password
        label2 = Label(self.root, text='Password', bg='#f0f0f0', fg='#333333', font=('verdana', 10, 'bold'), anchor='w')
        label2.pack(fill='x', padx=60, pady=(10, 0),ipady=4, anchor='w')

        self.password_input = Entry(self.root, width=40, bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da')
        self.password_input.pack(pady=(5, 10), ipady=4, padx=60, anchor='w', fill='x')
        
        
        # Login Button
        login_btn = Button(self.root, text='Login', width=10 ,bg='#f0f0f0', fg='#333333', font=('verdana', 10, 'bold'))
        login_btn.pack(pady=(10, 10))
        
        
        # Not Registered
        label3 = Label(self.root, text='Not Registered?', bg='#f0f0f0', fg='#333333', font=('verdana', 10, 'bold'), anchor='w')
        label3.pack(pady=(150, 10))
        
        
        # Not Registered Button
        redirect_btn = Button(self.root, text='Register Now', bg='#f0f0f0', fg='#333333', font=('verdana', 10, 'bold'))
        redirect_btn.pack(pady=(10, 10))







nlp = NLPApp()