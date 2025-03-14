from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

############################################################################################   
    def __init__(self):
        
        # Database Object
        self.dbo = Database()
        
        # API Object
        self.apio = API()
        
        # Login GUI Load
        self.root = Tk()
        self.root.title('NLP App')
        self.root.iconbitmap('recources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#283747')
        
        self.login_gui()
        
        self.root.mainloop()


############################################################################################


    # Login GUI Code
    def login_gui(self):
        self.clear()
        
        # Heading
        heading = Label(self.root, text='NLP App', bg='#283747', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure( font=('verdana', 24, 'bold'))
        
        
        # Login Email
        label1 = Label(self.root, text='Enter Email', bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', font=('verdana', 10, 'bold'), anchor='w')
        label1.pack(fill='x', padx=60, pady=(10, 0),ipady=4, anchor='w')

        self.email_input = Entry(self.root, width=40, bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da')
        self.email_input.pack(pady=(5, 10), ipady=4, padx=60, anchor='w', fill='x')


        # Login Password
        label2 = Label(self.root, text='Password',  font=('verdana', 10, 'bold'),bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', anchor='w')
        label2.pack(fill='x', padx=60, pady=(10, 0),ipady=4, anchor='w')

        self.password_input = Entry(self.root, width=40, bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', show='*')
        self.password_input.pack(pady=(5, 10), ipady=4, padx=60, anchor='w', fill='x')
        
        
        # Login Button
        login_btn = Button(self.root, text='Login',bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', width=10 , font=('verdana', 10, 'bold'), command=self.perform_login)
        login_btn.pack(pady=(10, 10))
        
        
        # Not Registered
        label3 = Label(self.root, text='Not Registered?', bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', font=('verdana', 10, 'bold'), anchor='w')
        label3.pack(pady=(150, 10))
        
        
        # Not Registered Button
        redirect_btn = Button(self.root, text='Register Now',bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', font=('verdana', 10, 'bold'), command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))


############################################################################################


    # Registration GUI Code
    def register_gui(self):
        self.clear()
        
        # Heading
        heading = Label(self.root, text='NLP App', bg='#283747', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure( font=('verdana', 24, 'bold'))
        
        
        # Registration Name
        label0 = Label(self.root, text='Enter Name', bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', font=('verdana', 10, 'bold'), anchor='w')
        label0.pack(fill='x', padx=60, pady=(10, 0),ipady=4, anchor='w')

        self.name_input = Entry(self.root, width=40, bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da')
        self.name_input.pack(pady=(5, 10), ipady=4, padx=60, anchor='w', fill='x')
        
        
        # Registration Email
        label1 = Label(self.root, text='Enter Email', bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', font=('verdana', 10, 'bold'), anchor='w')
        label1.pack(fill='x', padx=60, pady=(10, 0),ipady=4, anchor='w')

        self.email_input = Entry(self.root, width=40, bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da')
        self.email_input.pack(pady=(5, 10), ipady=4, padx=60, anchor='w', fill='x')


        # Registration Password
        label2 = Label(self.root, text='Password',  font=('verdana', 10, 'bold'),bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', anchor='w')
        label2.pack(fill='x', padx=60, pady=(10, 0),ipady=4, anchor='w')

        self.password_input = Entry(self.root, width=40, bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', show='*')
        self.password_input.pack(pady=(5, 10), ipady=4, padx=60, anchor='w', fill='x')
        
        
        # Registration Button
        register_btn = Button(self.root, text='Register',bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', width=10 , font=('verdana', 10, 'bold'), command=self.perform_registration)
        register_btn.pack(pady=(10, 10))
        
        
        # Already Registered
        label3 = Label(self.root, text='Already Registered?', bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', font=('verdana', 10, 'bold'), anchor='w')
        label3.pack(pady=(100, 10))
        
        
        # Login Button
        redirect_btn = Button(self.root, text='Login Now',bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', font=('verdana', 10, 'bold'), command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))


############################################################################################


    # Clear GUI Utility Function
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


############################################################################################

    # Registration Button Fetching Data
    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        
        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Registration Status', 'Registration Successful! You can login now!')
        else:
            messagebox.showerror('Registration Status', 'Email Already Exists!')


############################################################################################


    # Login Button Checking Data
    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        
        
        response = self.dbo.search(email, password)
        
        if response:
            messagebox.showinfo('Login Status', 'Login Successful!')
            self.home_gui()
        else:
            messagebox.showerror('Login Status', 'Invalid Credentials!')


############################################################################################


    # Home GUI
    def home_gui(self):
        self.clear()
        
        # Heading
        heading = Label(self.root, text='NLP App', bg='#283747', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure( font=('verdana', 24, 'bold'))
        
        
        # Sentiment Analysis
        sentiment_btn = Button(self.root, text='Sentiment Analysis',bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', width=30, height=4 , font=('verdana', 10, 'bold'), command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))
        
        
        # NER Analysis
        ner_btn = Button(self.root, text='Named Entity Recognition',bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', width=30, height=4 , font=('verdana', 10, 'bold'), command=self.sentiment_gui)
        ner_btn.pack(pady=(10, 10))
        
        
        # Emotion Analysis
        emotion_btn = Button(self.root, text='Emotion Prediction',bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', width=30, height=4 , font=('verdana', 10, 'bold'), command=self.sentiment_gui)
        emotion_btn.pack(pady=(10, 10))


        # Logout Button
        logout_btn = Button(self.root, text='Logout',bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', font=('verdana', 10, 'bold'), command=self.login_gui)
        logout_btn.pack(pady=(100, 10))



############################################################################################


    # Sentiment Analysis GUI
    def sentiment_gui(self):
        self.clear()
        
        
        # Heading
        heading = Label(self.root, text='NLP App', bg='#283747', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure( font=('verdana', 24, 'bold'))
        
        
        # Sentiment Analysis
        heading = Label(self.root, text='Sentiment Analysis', bg='#283747', fg='white')
        heading.pack(pady=(10, 20))
        heading.configure( font=('verdana', 20, ))


        # Sentiment Text Label
        label1 = Label(self.root, text='Enter The Text', bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', font=('verdana', 10, 'bold'), anchor='w')
        label1.pack(fill='x', padx=60, pady=(10, 0),ipady=4, anchor='w')


        # Sentiment Text Input
        self.sentiment_input = Entry(self.root, width=40, bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da')
        self.sentiment_input.pack(pady=(20, 10), ipady=4, padx=60, anchor='w', fill='x')
        
        
        # Sentiment Analysis Button
        sentiment_btn = Button(self.root, text='Analyze Sentiment',bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', font=('verdana', 10, 'bold'), command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))
        
        
        # Result Text Label
        self.sentiment_result = Label(self.root, text='', bg='#283747', fg='white', anchor='w', justify='left', wraplength=400)
        self.sentiment_result.pack(fill='x', padx=60, pady=(10, 0), ipady=4, anchor='w')
        self.sentiment_result.configure(font=('verdana', 10))
        
        
        # Go Back Button
        goback_btn = Button(self.root, text='Go Back',bg='#e8f0fe', fg='black', bd=0, highlightthickness=1, highlightbackground='#ced4da', font=('verdana', 10, 'bold'), command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    
    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        sentiment = result['type'].capitalize()
        
        # Extracting top 5 positive and negative words
        positive_words = [kw['word'] for kw in result['keywords'] if kw['score'] > 0][:3]
        negative_words = [kw['word'] for kw in result['keywords'] if kw['score'] < 0][:3]

        # Displaying result
        self.sentiment_result['text'] = f"Sentiment: {sentiment}\n\nPositive Words:\n{', '.join(positive_words)}\nNegative Words:\n{', '.join(negative_words)}"

############################################################################################


############################################################################################


############################################################################################



############################################################################################


############################################################################################


############################################################################################

nlp = NLPApp()