
from tkinter import *
from tkinter import ttk, messagebox
import webbrowser


class Info(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x550+350+200")
        self.title("Information")
        self.resizable(False, False)

    # background .
        self.background = PhotoImage(file='backgrounds/—Pngtree—white abstract background vector_3638073.png')
        self.background_label = Label(self, image=self.background)
        self.background_label.pack()

    # info icon .
        self.info_icon = PhotoImage(file='icons/information.png')
        self.info_icon_label = Label(self, image=self.info_icon)
        self.info_icon_label.place(x=100, y=30)

    # title .
        self.title_label = Label(self, text='About Me', font='Times 24 bold', bg='white')
        self.title_label.place(x=260, y=80)

    # name label .
        self.name_label = Label(self, text='vadim beletsker', font='Times 18 bold', bg='white')
        self.name_label.place(x=220, y=200)

    # facebook .
        self.creator_facebook_button = Button(self, text='https://www.facebook.com/profile.php?id=100002074177617',
                                              command=self.open_facebook, width=50, font='Times 13 bold')
        self.creator_facebook_button.place(x=50, y=260)

    # github .
        self.creator_gitHub_page = Button(self, text='https://github.com/vadimbel',
                                          command=self.open_gitHub, width=50, font='Times 13 bold')
        self.creator_gitHub_page.place(x=50, y=300)

    # linkedin .
        self.creator_linkedin_page = Button(self, text='https://www.linkedin.com/in/vadim-beletsker-56103615a/',
                                            command=self.open_linkedin, width=50, font='Times 13 bold')
        self.creator_linkedin_page.place(x=50, y=340)


    def open_facebook(self):
        webbrowser.open("https://www.facebook.com/profile.php?id=100002074177617")

    def open_gitHub(self):
        webbrowser.open("https://github.com/vadimbel")

    def open_linkedin(self):
        webbrowser.open("https://www.linkedin.com/in/vadim-beletsker-56103615a/")




