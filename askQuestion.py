
from tkinter import *
from tkinter import ttk, messagebox

import sqlite3, random

con = sqlite3.connect("menu.db")
cur = con.cursor()

class AskQuestion(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("400x200")
        self.title("Help")
        self.resizable(False, False)

        self.question_label = Label(self, text='Select one of the options :', font='Times 16 bold')
        self.question_label.pack()

        self.reset_user_name_button = Button(self, text='Reset user name', font='Times 12 bold', bd=5, width=20,
                                             command=self.reset_user_name)
        self.reset_user_name_button.place(x=100, y=40)

        self.reset_password_button = Button(self, text='Reset password', font='Times 12 bold', bd=5, width=20,
                                            command=self.reset_password)
        self.reset_password_button.place(x=100, y=80)

        self.cancel_button = Button(self, text='Cancel', font='Times 12 bold', bd=5, width=20,
                                    command=self.cancel)
        self.cancel_button.place(x=100, y=120)


    def reset_user_name(self):
        newUserName = ResetUserName()
        self.destroy()

    def reset_password(self):
        newPassword = ResetPassword()
        self.destroy()

    def cancel(self):
        self.destroy()


class ResetPassword(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+650+200")
        self.title("Help")
        self.resizable(False, False)

    # background .
        self.background = PhotoImage(file='backgrounds/—Pngtree—business lines red abstract border_5658429.png')
        self.background_label = Label(self, image=self.background)
        self.background_label.pack()

    # icon for new user .
        self.user_icon = PhotoImage(file='icons/id-card.png')
        self.user_icon_label = Label(self, image=self.user_icon)
        self.user_icon_label.place(x=50, y=10)

    # title .
        self.title_label = Label(self, text='Enter the details below', font='Times 20 bold')
        self.title_label.place(x=200, y=60)

    # name .
        self.name_label = Label(self, text='Name :', font='Times 16 bold')
        self.name_label.place(x=20, y=180)
        self.name_text_editor = Text(self, width=50, height=1, bd=5)
        self.name_text_editor.place(x=140, y=180)

    # surname .
        self.surname_label = Label(self, text='Surname :', font='Times 16 bold')
        self.surname_label.place(x=20, y=225)
        self.surname_text_editor = Text(self, width=50, height=1, bd=5)
        self.surname_text_editor.place(x=140, y=225)

    # date (day , month , year) .
        self.date = Label(self, text='Birth day : ', font='Times 16 bold')
        self.date.place(x=20, y=270)

    # create a list for the days and insert them to the combo box .
        days_list = []
        for i in range(1, 32):
            days_list.append(i)

        self.day = StringVar()
        self.date_day = ttk.Combobox(self, textvariable=self.day, values=days_list,
                                     state='readonly', width=15)
        self.date_day.place(x=140, y=274)

    # create a list for the months and insert them to the combo box .
        month_list = []
        for i in range(1, 13):
            month_list.append(i)

        self.month = StringVar()
        self.date_month = ttk.Combobox(self, textvariable=self.month, values=month_list,
                                       state='readonly', width=15)
        self.date_month.place(x=270, y=274)

    # create a list for years and insert them to the combo box .
        year_list = []
        for i in range(1950, 2004):
            year_list.append(i)

        self.year = StringVar()
        self.date_year = ttk.Combobox(self, textvariable=self.year, values=year_list,
                                      state='readonly', width=15)
        self.date_year.place(x=400, y=274)

    # user name label and text editor .
        self.user_name_label = Label(self, text='User Name :', font='Times 16 bold')
        self.user_name_label.place(x=20, y=315)
        self.user_name_text_editor = Text(self, width=50, height=1, bd=5)
        self.user_name_text_editor.place(x=140, y=318)

        def submit():
            """
            this function will be activated after the user click on the 'submit' button .
            the function will search a user with the values was entered .
            if there is a user with those balues then -> a new window will be opened (with 2 security questions) .
            else the user will get error message .
            :return:
            """
        # get all the inputs from the user .
            name = self.name_text_editor.get(1.0, END)
            name = name[0:len(name)-1]

            surname = self.surname_text_editor.get(1.0, END)
            surname = surname[0:len(surname)-1]

            date_day = self.date_day.get()
            date_month = self.date_month.get()
            date_year = self.date_year.get()

            user_name = self.user_name_text_editor.get(1.0, END)
            user_name = user_name[0:len(user_name)-1]

        # check if there is a user with this data in db .
            user_data = cur.execute("SELECT * FROM user_info WHERE user_name=? and user_surname=? and user_date_day=? "
                                    "and user_date_month=? and user_date_year=? and user_user_name=?",
                                    (name, surname, date_day, date_month, date_year, user_name)).fetchall()

        # if len(user_data) == 0 -> there is a user with this data -> open another window with users security questions
            if len(user_data) == 1:
                askSecurityQuestions = AskSecurityQuestions(user_data)
                self.destroy()
            else:
                messagebox.showinfo("Error", "No user with this data !", icon='warning')
                self.destroy()


    # check 'submit' button .
        self.b = Button(self, text='Submit', command=submit, width=30, height=2, bd=5, font='Times 16 bold')
        self.b.place(x=140, y=400)



class ResetUserName(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+650+200")
        self.title("Help")
        self.resizable(False, False)

    # background .
        self.background = PhotoImage(file='backgrounds/—Pngtree—business lines red abstract border_5658429.png')
        self.background_label = Label(self, image=self.background)
        self.background_label.pack()

    # icon for new user .
        self.user_icon = PhotoImage(file='icons/id-card.png')
        self.user_icon_label = Label(self, image=self.user_icon)
        self.user_icon_label.place(x=50, y=10)

    # title .
        self.title_label = Label(self, text='Enter the details below', font='Times 20 bold')
        self.title_label.place(x=200, y=60)

    # name .
        self.name_label = Label(self, text='Name :', font='Times 16 bold')
        self.name_label.place(x=20, y=180)
        self.name_text_editor = Text(self, width=50, height=1, bd=5)
        self.name_text_editor.place(x=140, y=180)

    # surname .
        self.surname_label = Label(self, text='Surname :', font='Times 16 bold')
        self.surname_label.place(x=20, y=225)
        self.surname_text_editor = Text(self, width=50, height=1, bd=5)
        self.surname_text_editor.place(x=140, y=225)

    # date (day , month , year) .
        self.date = Label(self, text='Birth day : ', font='Times 16 bold')
        self.date.place(x=20, y=270)

    # create a list for the days and insert them to the combo box .
        days_list = []
        for i in range(1, 32):
            days_list.append(i)

        self.day = StringVar()
        self.date_day = ttk.Combobox(self, textvariable=self.day, values=days_list,
                                     state='readonly', width=15)
        self.date_day.place(x=140, y=274)

    # create a list for the months and insert them to the combo box .
        month_list = []
        for i in range(1, 13):
            month_list.append(i)

        self.month = StringVar()
        self.date_month = ttk.Combobox(self, textvariable=self.month, values=month_list,
                                       state='readonly', width=15)
        self.date_month.place(x=270, y=274)

    # create a list for years and insert them to the combo box .
        year_list = []
        for i in range(1950, 2004):
            year_list.append(i)

        self.year = StringVar()
        self.date_year = ttk.Combobox(self, textvariable=self.year, values=year_list,
                                      state='readonly', width=15)
        self.date_year.place(x=400, y=274)

    # password that the user knows .
        self.password_label = Label(self, text='Password :', font='Times 16 bold')
        self.password_label.place(x=20, y=315)
        self.password_text_editor = Text(self, width=50, height=1, bd=5)
        self.password_text_editor.place(x=140, y=318)

        def submit():
            """
            this function will be activated when the user clicl on the 'submit' button .
            the function will get all the info the user inserted and check if there is a person with that data in db .
            if so then [line 137] -> the user will be answering his security questions .
            :return:
            """
        # get all the inputs from the user .
            name = self.name_text_editor.get(1.0, END)
            name = name[0:len(name)-1]

            surname = self.surname_text_editor.get(1.0, END)
            surname = surname[0:len(surname)-1]

            date_day = self.date_day.get()
            date_month = self.date_month.get()
            date_year = self.date_year.get()

            password = self.password_text_editor.get(1.0, END)
            password = password[0:len(password)-1]

        # check if there is a user with this data in db .
            user_data = cur.execute("SELECT * FROM user_info WHERE user_name=? and user_surname=? and user_date_day=? "
                                    "and user_date_month=? and user_date_year=? and user_password=?",
                                    (name, surname, date_day, date_month, date_year, password)).fetchall()

        # if len(user_data) == 0 -> there is a user with this data -> open another window with users security questions
            if len(user_data) == 1:
                askSecurityQuestions = AskSecurityQuestions(user_data)
                self.destroy()
            else:
                messagebox.showinfo("Error", "No user with this data !", icon='warning')
                self.destroy()

    # check 'submit' button .
        self.b = Button(self, text='Submit', command=submit, width=30, height=2, bd=5, font='Times 16 bold')
        self.b.place(x=140, y=400)



class AskSecurityQuestions(Toplevel):
    # user_data = when user click on 'help' button
    # -> then insert all the data in the window that pop up
    # -> i search this user in db -> if this user exists
    # -> i get all of his information from db and pass it to this class .

    def __init__(self, user_data):
        Toplevel.__init__(self)
        self.geometry("650x650+650+200")
        self.title("Help")
        self.resizable(False, False)

    # background .
        self.background = PhotoImage(file='backgrounds/—Pngtree—business lines red abstract border_5658429.png')
        self.background_label = Label(self, image=self.background)
        self.background_label.pack()

    # icon at the top of the window .
        self.question_icon = PhotoImage(file='icons/question1.png')
        self.question_icon_label = Label(self, image=self.question_icon)
        self.question_icon_label.place(x=10, y=20)

    # title .
        self.title_label = Label(self, text='Please answer your security questions', font='Times 22 bold')
        self.title_label.place(x=150, y=70)

    # first question .
        self.question_one_label = Label(self, text=user_data[0][5], font='Times 20 bold')
        self.question_one_label.place(x=20, y=170)
        self.question_one_text_editor = Text(self, width=70, height=4, bd=5)
        self.question_one_text_editor.place(x=20, y=220)

    # second question .
        self.question_two_label = Label(self, text=user_data[0][7], font='Times 20 bold')
        self.question_two_label.place(x=20, y=310)
        self.question_two_text_editor = Text(self, width=70, height=4, bd=5)
        self.question_two_text_editor.place(x=20, y=360)

        def check_answers():
            """
            this function will be activated when the user click on the 'submit' button .
            if the answers are the same -> the user will get his user_name and user_password printed .
            if not then the user will het error message .
            :return:
            """
            user_answer_one = self.question_one_text_editor.get(1.0, END)
            user_answer_two = self.question_two_text_editor.get(1.0, END)

        # user answers are correct then print the user_name and user_password .
            if user_answer_one == user_data[0][6] and user_answer_two == user_data[0][8]:
                messagebox.showinfo("Success", "Your user name is : {}\nYour password is : {}"
                                    .format(user_data[0][10], user_data[0][9]))
                self.destroy()
        # user answers are not correct -> print error .
            else:
                messagebox.showinfo("Error", "Wrong answers for security questions !", icon='warning')

    # submit button .
        self.submit_button = Button(self, text='Submit', font='Times 16 bold', width=20, height=2, bd=5,
                                    command=check_answers)
        self.submit_button.place(x=170, y=480)







