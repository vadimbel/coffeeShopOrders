
from tkinter import *
from tkinter import ttk, messagebox

import sqlite3, coffeeShop, createUser, askQuestion, info

con = sqlite3.connect("menu.db")
cur = con.cursor()


class ChooseTable(object):
    def __init__(self, parent):
        self.parent = parent

    # create and locate background and icon :
        self.background = PhotoImage(file='backgrounds/first_screen_background.png')
        self.background_label = Label(self.parent, image=self.background)
        self.background_label.pack()

        self.icon = PhotoImage(file='icons/login.png')
        self.login_icon = Label(self.parent, image=self.icon)
        self.login_icon.place(x=300, y=25)

    # create user name entry and label and locate them on the app .
        self.user_name_label = Label(self.parent, text='User Name :', font='Times 16 bold')
        self.user_name_label.place(x=20, y=100)
        self.user_name_entry = Entry(self.parent, width=60, bd=5)
        self.user_name_entry.insert(0, "Please enter user name")
        self.user_name_entry.place(x=160, y=103)

    # create password entry and label and locate it on the app .
        self.password_label = Label(self.parent, text='Password : ', font='Times 16 bold')
        self.password_label.place(x=20, y=140)
        self.password_entry = Entry(self.parent, width=60, bd=5)
        self.password_entry.insert(0, "Please enter password")
        self.password_entry.place(x=160, y=143)

    # create login button and place it on the app .
        self.login_button = Button(self.parent, text='Login', width=30, height=1, font='Times 12 bold', bd=5,
                                   command=self.user_login)
        self.login_button.place(x=190, y=200)

    # create a button to add a new user to the system , the button will user 'create_user' function calling other class.
        self.new_user_button = Button(self.parent, text='Create New User', width=30, height=1, font='Times 12 bold'
                                      , bd=5, command=self.create_new_user)
        self.new_user_button.place(x=190, y=240)

    # create help button to reset password/user name .
        self.help_button = Button(self.parent, text='Help', width=30, height=1, font='Times 12 bold',
                                  bd=5, command=self.help)
        self.help_button.place(x=190, y=280)

    # create info button about my self .
        self.information_button = Button(self.parent, text='Information', width=30, height=1, font='Times 12 bold',
                                         bd=5, command=self.get_info)
        self.information_button.place(x=190, y=320)

        def click_on_entry_user_name(evt):
            """
            This function will be activated when the user click on the 'userNameEntry' box .
            the text inserted to the entry box will be deleted on click .
            :param evt:
            :return: None
            """
            self.user_name_entry.delete(0, 'end')

        def click_on_entry_password(evt):
            """
            This function will be activated when the user click on the 'passwordEntry' box .
            the text inserted to the entry box will be deleted on click .
            :param evt:
            :return: None
            """
            self.password_entry.delete(0, 'end')

    # when user click on the entry box text -> the text inserted will be deleted .
        self.user_name_entry.bind('<Button-1>', click_on_entry_user_name)
        self.password_entry.bind('<Button-1>', click_on_entry_password)


    def user_login(self):
        """
        This fucntion will be activated when the user click on the 'login' button .
        the function will check what the user typed to the two entries 'user_name' , 'password' then check if there is
        a user name with this data in the data base .
        :return: None
        """
    # get the data from the two entries .
        user_name = self.user_name_entry.get()
        user_password = self.password_entry.get()

    # all users from data base .
        all_users = cur.execute("SELECT * FROM user_info").fetchall()

    # check if the user is exists in the data base .
        for user in all_users:
            # if the user exists then open the system .
            if user[10] == user_name and user[9] == user_password:
                open_system = coffeeShop.CoffeeShop()
                return
        # user doesnt exist in the data base -> show this message .
        messagebox.showerror("Error", "Wrong user_name or password ...", icon='warning')

    def create_new_user(self):
        create_user = createUser.CreateUser()

    def help(self):
        ask = askQuestion.AskQuestion()

    def get_info(self):
        information = info.Info()


def main():
    root = Tk()
    app = ChooseTable(root)
    root.title("Choose Table")
    root.geometry("650x550+350+200")
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()






