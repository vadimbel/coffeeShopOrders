
from tkinter import *
from tkinter import ttk, messagebox

import sqlite3, buttons

con = sqlite3.connect("menu.db")
cur = con.cursor()

class PickFish(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+650+200")
        self.title("Fish Menu")
        self.resizable(False, False)

    # create top frame and place one button on it .
        top_frame = Frame(self, width=500, height=50, relief=SUNKEN, borderwidth=3)
        top_frame.pack(side=TOP, fill=X)

        self.add_item_button = Button(top_frame, text='ADD', font=buttons.options_bd_btn, bd=buttons.options_bd_btn,
                                      height=buttons.options_height_btn, width=buttons.options_width_btn,
                                      command=self.add_item_to_check)
        self.add_item_button.pack(side=LEFT, padx=10)

    # create left frame and place a list with all the fish kinds in the menu .
        left_frame = Frame(self, width=200, height=70, relief=SUNKEN, borderwidth=3)
        left_frame.pack(side=LEFT, fill=Y)

        self.fish_list = Listbox(left_frame, width=35, height=30)
        self.fish_list.pack()

    # create right frame that will display all the info about every fish selected in the list box on the left frame .
        right_frame = Frame(self, width=500, height=70, relief=SUNKEN, borderwidth=3)
        right_frame.pack(side=LEFT, fill=Y)

        self.list_detail = Listbox(right_frame, width=200, height=30)
        self.list_detail.pack()

        self.display_fish()

        def display_values(evt):
            """
            This function will be activated when the user click on one of the items in the 'fish_list' box .
            :param evt:
            :return: None
            """
            # solve a bug : when i click on 'fish_list' then on 'list_detail' -> exception .
            if len(self.list_detail.curselection()) > 0:
                return
            # delete all elements from 'list_detail' .
            self.list_detail.delete(0, END)
            # get the selected item from the 'fish_list' box .
            fish = str(self.fish_list.get(self.fish_list.curselection()))
            # substring the name out of the selected item .
            fish_name = fish[3:]
            # get all the properties of the selected item from db in format : [( ....)] -> tuple inside a list .
            elements = cur.execute("SELECT * FROM fish_kinds WHERE fish_name=?", (fish_name,)).fetchall()
            # 'elements' is a list contains a tuple , 'element' is only the tuple .
            element = elements[0]
            # insert all the ingredients from the tuple to the 'list_detail' box .
            count = 0
            for item in range(1, len(element)):
                self.list_detail.insert(count, element[item])
                count += 1

        # when user click on item in the 'fish_list' box -> the details will appear in the 'list_detail' .
        self.fish_list.bind('<<ListboxSelect>>', display_values)

    def display_fish(self):
        """
        This function created to display the name of the fish on the 'fish_list' box .
        :return: None
        """
        # get all the elements from 'fish_kinds' table in db .
        fish_kinds = cur.execute("SELECT * FROM fish_kinds").fetchall()

        # insert the name of every fish to 'fish_list' box .
        count = 0
        for fish in fish_kinds:
            self.fish_list.insert(count, "{}. {}".format(count+1, str(fish[0])))
            count += 1

    def add_item_to_check(self):
        """
        This function will be activated when the user select one of the items in the 'fish_list' box then click the
        'add' button .
        the function will add the : 1. dish name , 2. dish price the 'check_bill' table in the database .
        :return: None
        """
        # solve bug : when user select one of the items in the 'list_detail' -> exception .
        if len(self.list_detail.curselection()) > 0:
            return
        # the code under will be executed only if the user select one of the items in the 'fish_list' then click 'add' btn.
        if len(self.fish_list.curselection()) > 0:
            try:
                # if the user select one of the item in 'fish_list' and clicked 'add' then :
                # get the item was selected from the 'p_list' .
                fish = str(self.fish_list.get(self.fish_list.curselection()))
                # substring only the name of the dish .
                fish_name = fish[3:]
                # get all the field from db of the selected item . -> elements = list contain a tuple with all the fields .
                elements = cur.execute("SELECT * FROM fish_kinds WHERE fish_name=?", (fish_name,)).fetchall()
                # element = is only the tuple .
                element = elements[0]
                # get the dish name , and its price out of the tuple .
                dish_name = element[0]
                dish_price = element[5]
                # ask the user one more time if he wants to add this dish to the 'check_bill' table in db .
                answer = messagebox.askyesnocancel("Warning", "Are you sure you want to add this item ?")
                # i yes -> i add the dish name and its price to the 'check_bill' .
                if answer is True:
                    # get the amount of times this dish was ordered .
                    dish_amount = cur.execute("SELECT dish_amount FROM total_bill WHERE dish_name=?", (dish_name,)) \
                        .fetchall()

                    # if its the first time -> i insert this dish_name , dish_price and dish_amount=1 to db .
                    if len(dish_amount) == 0:
                        query = "INSERT INTO 'total_bill' (dish_name, dish_price, dish_amount) VALUES (?, ?, ?)"
                        cur.execute(query, (dish_name, dish_price, 1))
                        con.commit()
                        messagebox.showinfo("Success", "Item added to bill successfully")
                        self.destroy()
                    # if the db has this dish in 'total_bill' table -> i increment 'dish_amount' field in db for this dish .
                    else:
                        increment_amount = dish_amount[0][0] + 1
                        query = "UPDATE total_bill set dish_amount=? WHERE dish_name=?"
                        cur.execute(query, (increment_amount, dish_name))
                        con.commit()
                        messagebox.showinfo("Success", "Item added to bill successfully")
                        self.destroy()
                # if the user click on 'no' -> i close this window .
                else:
                    self.destroy()
            # if there any problem -> one of those two line will be executed .
            except:
                messagebox.showinfo("Error", "ops .. something wrong !!", icon='warning')
        else:
            messagebox.showinfo("Error", "Fields cant be empty !", icon='warning')
            self.destroy()



