
from tkinter import *
from tkinter import ttk, messagebox

import sqlite3, random

con = sqlite3.connect("menu.db")
cur = con.cursor()

class CreateUser(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+650+200")
        self.title("Create User")
        self.resizable(False, False)

    # background for this window .
        self.background = PhotoImage(file='backgrounds/coffee_menu_background.png')
        self.background_label = Label(self, image=self.background)
        self.background_label.pack()

    # icon new to the title .
        self.new_user_icon = PhotoImage(file='icons/add-group.png')
        self.new_user_label = Label(self, image=self.new_user_icon)
        self.new_user_label.place(x=120, y=30)

    # title .
        self.title_label = Label(self, text='Create New User', font='Times 20 bold', bg='white')
        self.title_label.place(x=230, y=50)

    # name , surname and date labels and entries .
        self.name_label = Label(self, text='Name : ', font='Times 14 bold', bg='white')
        self.name_label.place(x=25, y=140)
        self.name_entry = Entry(self, width=60, bd=5)
        self.name_entry.place(x=140, y=141)

        self.surname_label = Label(self, text='Surname : ', font='Times 14 bold', bg='white')
        self.surname_label.place(x=25, y=180)
        self.surname_entry = Entry(self, width=60, bd=5)
        self.surname_entry.place(x=140, y=181)

    # date label :
        self.date_label = Label(self, text='Date : ', font='Times 14 bold', bg='white')
        self.date_label.place(x=25, y=220)

    # select day of your birth day .
        days_list = []
        for i in range(1, 32):
            days_list.append(i)

        self.day = StringVar()
        self.date_day = ttk.Combobox(self, textvariable=self.day, values=days_list,
                                     state='readonly', width=10)
        self.date_day.place(x=140, y=223)

    # select month of your birthday .
        month_list = []
        for i in range(1, 13):
            month_list.append(i)

        self.month = StringVar()
        self.date_month = ttk.Combobox(self, textvariable=self.month, values=month_list,
                                      state='readonly', width=10)
        self.date_month.place(x=240, y=223)

    # select year of your birthday .
        year_list = []
        for i in range(1950, 2003):
            year_list.append(i)

        self.year = StringVar()
        self.date_year = ttk.Combobox(self, textvariable=self.year, values=year_list,
                                      state='readonly', width=10)
        self.date_year.place(x=340, y=223)

    # two security questions and answers :
        question_one_list = [
            "",
            "What is your favorite TV show ?",
            "What is your favorite sport ?",
            "What is your favorite movie ?",
            "What is your favorite cartoon ?",
            "What is your favorite food ?",
            "What is your favorite animal ?",
        ]

    # question and combobox box for first question :
        self.security_question_one_label = Label(self, text='Question 1 :', font='Times 14 bold', bg='white')
        self.security_question_one_label.place(x=25, y=261)

        self.answer_one = StringVar()
        self.security_question_one = ttk.Combobox(self, textvariable=self.answer_one, values=question_one_list,
                                                  state='readonly', width=58)
        self.security_question_one.place(x=140, y=264)

        self.security_question_one_label_answer = Label(self, text='Answer :', font='Times 14 bold', bg='white')
        self.security_question_one_label_answer.place(x=25, y=301)

    # answer for first question :
        self.answer_one_text_editor = Text(self, width=37, height=1, font="times 15 bold", wrap=WORD)
        self.answer_one_text_editor.place(x=140, y=304)

        question_two_list = [
            "",
            "What is your childhood neighborhood name ?",
            "What is your childhood pet name ?",
            "What is your grandmather name ?",
            "What is your childhood first teacher name ?",
            "What is you first school name ?",
        ]

    # question and combobox box for second question :
        self.security_question_two_label = Label(self, text='Question 2 :', font='Times 14 bold', bg='white')
        self.security_question_two_label.place(x=25, y=351)

        self.answer_two = StringVar()
        self.security_question_two = ttk.Combobox(self, textvariable=self.answer_two, values=question_two_list,
                                                  state='readonly', width=58)
        self.security_question_two.place(x=140, y=354)

        self.security_question_two_label_answer = Label(self, text='Answer :', font='Times 14 bold', bg='white')
        self.security_question_two_label_answer.place(x=25, y=391)

        self.answer_two_text_editor = Text(self, width=37, height=1, font='times 15 bold', wrap=WORD)
        self.answer_two_text_editor.place(x=140, y=394)

    # submit button -> when the user click on this button -> 'user_info' table will be updated and a new user will be
    # created .

        self.submit_button = Button(self, text='Submit', font='Times 14 bold', bd=5, width=20, command=self.create_user)
        self.submit_button.place(x=205, y=450)


    def create_user(self):
        """
        This function will be activate when the user press on the 'Create New User' button .
        if the user fill all the fields in the page -> the function will update the 'user_info' table in db and a new
        user will be created .
        :return: None
        """
    # get all the inputs from the page entered by the user .
        user_name = self.name_entry.get()
        user_surname = self.surname_entry.get()
        date_day = self.date_day.get()
        date_month = self.date_month.get()
        date_year = self.date_year.get()
        security_question_one = self.security_question_one.get()
        security_question_one_answer = self.answer_one_text_editor.get(1.0, END)
        security_question_two = self.security_question_two.get()
        security_question_two_answer = self.answer_two_text_editor.get(1.0, END)

    # if all the values are not empty then :
        if(user_name and user_surname and date_day and date_month and date_year and security_question_one and
                security_question_one_answer and security_question_two and security_question_two_answer != None):
        # i create a user name and a password for the new user :
            signs = "!@#$%^&*"
            numbers = "123456789"
            letters = "abcdefghijklmnopqrstuvwxyz"

            def create_user_name(user_name: str) -> str:
                """
                This function will be activated if the user filled all the fields -> the function will create a new
                user name for the new user .
                :param user_name: personal name of the new user entered in the entry box from page .
                :return: the new user_name
                """
                user_user_name = user_name+"_"
                for i in range(2):
                    rand1 = random.randint(0, 7)
                    user_user_name += signs[rand1]
                    for j in range(1):
                        rand2 = random.randint(0, 8)
                        user_user_name += numbers[rand2]
                return user_user_name

            def create_password() -> str:
                """
                This function will be activated if the user filled all the fields -> the function will create a new
                password for the user .
                :return: new password
                """
                new_password = ""
                for i in range(3):
                    rand1 = random.randint(0, 7)
                    new_password += signs[rand1]
                    for j in range(1):
                        rand2 = random.randint(0, 8)
                        new_password += numbers[rand2]
                    for k in range(1):
                        rand3 = random.randint(0, 25)
                        new_password += letters[rand3]
                return new_password

            user_user_name = create_user_name(user_name)
            user_password = create_password()

            query = "INSERT INTO 'user_info' (user_name, user_surname, user_date_day, user_date_month, user_date_year," \
                    " user_security_q1, user_security_a1, user_security_q2, user_security_a2," \
                    " user_password, user_user_name) VALUES (?,?,?,?,?,?,?,?,?,?,?)"
            cur.execute(query, (user_name, user_surname, date_day, date_month, date_year, security_question_one,
                                security_question_one_answer, security_question_two, security_question_two_answer,
                                user_password, user_user_name))
            con.commit()
            messagebox.showinfo("Success", "New user has been created !\nuser name : {}\nuser password : {}"
                                .format(user_user_name, user_password))
            self.destroy()
        else:
            messagebox.showinfo("Error", "All fields must be filled !")
            self.destroy()



