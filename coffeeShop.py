
from tkinter import *
from tkinter import ttk, messagebox

import buttons, pickPasta, pickPizza, pickFish, pickMeat, pickHotDrink, pickColdDrink, pickDessert, pickAlcohol
import sqlite3

con = sqlite3.connect("menu.db")
cur = con.cursor()

class CoffeeShop(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+650+200")
        self.title("Table Menu")
        self.resizable(False, False)

    # the title at the top of the window .
        self.title = Label(self, text='Coffee Shop :', font='Times 30 bold')
        self.title.place(x=30, y=20)

    # icon and button for pasta
        self.pasta_icon = PhotoImage(file='icons/spaguetti.png')
        self.pasta_button = Button(self, text='Pasta', font=buttons.font_btn, bd=buttons.bd_btn,
                                   height=buttons.height_btn, width=buttons.width_btn, image=self.pasta_icon,
                                   compound=LEFT, padx=10, command=self.choose_pasta)
        self.pasta_button.place(x=buttons.x_distance, y=buttons.y_distance)

    # icon and button for pizza
        self.pizza_icon = PhotoImage(file='icons/pizza.png')
        self.pizza_button = Button(self, text='Pizza', font=buttons.font_btn, bd=buttons.bd_btn,
                                   height=buttons.height_btn, width=buttons.width_btn, image=self.pizza_icon,
                                   compound=LEFT, padx=10, command=self.choose_pizza)
        self.pizza_button.place(x=buttons.x_distance+160, y=buttons.y_distance)

    # icon and button for fish
        self.fish_icon = PhotoImage(file='icons/fish.png')
        self.fish_button = Button(self, text='Fish', font=buttons.font_btn, bd=buttons.bd_btn,
                                  height=buttons.height_btn, width=buttons.width_btn, image=self.fish_icon,
                                  compound=LEFT, padx=10, command=self.choose_fish)
        self.fish_button.place(x=buttons.x_distance, y=buttons.y_distance+80)

    # icon and button for meat
        self.meat_icon = PhotoImage(file='icons/meat.png')
        self.meat_button = Button(self, text='Meat', font=buttons.font_btn, bd=buttons.bd_btn,
                                  height=buttons.height_btn, width=buttons.width_btn, image=self.meat_icon,
                                  compound=LEFT, padx=10, command=self.choose_meat)
        self.meat_button.place(x=buttons.x_distance+160, y=buttons.y_distance+80)

    # icon and button for hot drinks .
        self.hot_drinks_icon = PhotoImage(file='icons/black-tea.png')
        self.hot_drinks_button = Button(self, text='Hot Drinks', font=buttons.font_btn, bd=buttons.bd_btn,
                                        height=buttons.height_btn, width=buttons.width_btn, image=self.hot_drinks_icon,
                                        compound=LEFT, padx=10, command=self.choose_hot_drink)
        self.hot_drinks_button.place(x=buttons.x_distance, y=buttons.y_distance+160)

    # icon and button for cold drinks .
        self.cold_drinks_icon = PhotoImage(file='icons/cold-drink.png')
        self.cold_drinks_button = Button(self, text='Cold Drinks', font=buttons.font_btn, bd=buttons.bd_btn,
                                         height=buttons.height_btn, width=buttons.width_btn,
                                         image=self.cold_drinks_icon, compound=LEFT, padx=10,
                                         command=self.choose_cold_drink)
        self.cold_drinks_button.place(x=buttons.x_distance+160, y=buttons.y_distance+160)

    # icon and button for dessert .
        self.dessert_icon = PhotoImage(file='icons/cake.png')
        self.dessert_button = Button(self, text='Dessert', font=buttons.font_btn, bd=buttons.bd_btn,
                                     height=buttons.height_btn, width=buttons.width_btn,
                                     image=self.dessert_icon, compound=LEFT, padx=10, command=self.choose_dessert)
        self.dessert_button.place(x=buttons.x_distance, y=buttons.y_distance+240)

    # icon and button for extras .
        self.alcohol_icon = PhotoImage(file='icons/waiter.png')
        self.alcohol_button = Button(self, text='Alcohol', font=buttons.font_btn, bd=buttons.bd_btn,
                                   height=buttons.height_btn, width=buttons.width_btn,
                                   image=self.alcohol_icon, compound=LEFT, padx=10, command=self.choose_alcohol)
        self.alcohol_button.place(x=buttons.x_distance+160, y=buttons.y_distance+240)

    # create a frame at the right side of the window with bill label , a list box and refresh , delete ,
        # print bill buttons .
        frame = Frame(self, width=250, height=70, bg='white', padx=20, relief=SUNKEN, borderwidth=2)
        frame.pack(side=RIGHT, fill=Y)

    # 'TOTAL' label at the top of the frame .
        self.bill_label = Label(frame, text='TOTAL : 0', font='Times 20 bold', bg='white')
        self.bill_label.place(x=20, y=1)

    # a list box -> display clients order .
        self.client_order_list_box = Listbox(frame, width=35, height=22)
        self.client_order_list_box.place(x=0, y=35)

        def display_bill():
            """
            this function will be activated when the user click on the 'refresh' button .
            the function will display all the dishes the user ordered from the menu to the list box .
            :return: None
            """
        # delete every thing from the list box (fix a bug when the user add another item and its prints the new items
        # under the old ones) .
            self.client_order_list_box.delete(0, END)

        # get every line from the 'total_bill' table in db .
            data = cur.execute("SELECT * FROM total_bill").fetchall()
            sum = 0

        # i get a list of tuples so i : (data is a list of tuples)
            for item in data:
                # unpack every tuple then
                name, price, amount = item
                count = 0

                # make a string in this format then
                name_and_price = "{}   -   {}".format(name, amount)

                # insert it to the 'client_order_list_box' ( display the dish name next to amount of time this dish was ordered .)
                self.client_order_list_box.insert(count, name_and_price)

                # strip the '$' from the price and calculate the total price
                price = price.strip("$")
                sum += float(price)*amount

            # display the total price at the 'TOTAL' label .
            self.bill_label.config(text='TOTAL : {}'.format(sum))

    # the function above will be activated when the user press the 'refresh' button to refresh the bill list box .
        self.refresh_button = Button(frame, text='Refresh', font='Times 12 bold', bd=6, height=1, width=21,
                                     command=display_bill)
        self.refresh_button.place(x=2, y=395)

        def delete_item():
            """
            this function will be activated when the user click on one of the items on the 'client_order_list_box'
            then click on the 'delete' button -> the function will delete the selected item from the bill .
            :return: None
            """
            # if the user selected on of the items in the list box .
            if len(self.client_order_list_box.curselection()) > 0:
            # get the string from the 'list_box' in the bill list box .
                contact_to_delete = self.client_order_list_box.get(self.client_order_list_box.curselection())

            # i want to cut out the dish name out of this string so :
                contact_to_delete_name = ""

            # i split the string then
                contact_to_delete_splited = contact_to_delete.split()

            # i take the first word and delete it from the split list . (every dish will have at least one word)
                contact_to_delete_name += contact_to_delete_splited[0]
                del contact_to_delete_splited[0]

            # if the next word is not '-' then i add : " "+the next word from the split list .
                for word in contact_to_delete_splited:
                    if word == '-':
                        break
                    contact_to_delete_name += " "+word

            # ask the user if he sure about delete .
                mbox = messagebox.askquestion("Warning", "Are you sure to delete this item ?", icon='warning')
                if mbox == 'yes':
                    # get all the fields from 'total_bill' table (name, price, amount) -> get a list contains a tuple .
                    data = cur.execute("SELECT * FROM total_bill WHERE dish_name=?", (contact_to_delete_name,))\
                        .fetchall()

                    # data is a list contains a tuple -> i want only the tuple inside -> unpack the tuple .
                    data_tuple = data[0]
                    name, price, amount = data_tuple

                    # if the dish is ordered more then once then i only update the 'dish_amount' .
                    if amount > 1:
                        query = "UPDATE total_bill set dish_amount=? WHERE dish_name=?"
                        cur.execute(query, (amount-1, name))
                        con.commit()
                        messagebox.showinfo("Success", "Item deleted successfully")

                    # if the dish ordered only once -> i delete it from the db .
                    elif amount == 1:
                        cur.execute("DELETE FROM total_bill WHERE dish_name=?", (name,))
                        con.commit()
                        messagebox.showinfo("Success", "Item deleted successfully")

                    # display all the item on the bill after delete one of them .
                    display_bill()

        # create 'delete' button to delete one of the item from the list box .
        self.delete_item = Button(frame, text='Delete', font='Times 12 bold', bd=6, height=1, width=21,
                                  command=delete_item)
        self.delete_item.place(x=2, y=440)

        def print_bill():
            """
            This function will be activated when the user click on the 'print bill' button .
            the function will delete everything from the 'total_bill' table in db then print a message to the user
            (the bill) .
            :return:
            """
        # get all the fields from 'total_bill' table in db .
            data = cur.execute("SELECT * FROM total_bill").fetchall()

        # string for the message to be printed at the end of the function .
            message = ""
            sum = 0

        # unpack every tuple and insert the values in the format under for the message will be displayed at the end of
        # the function .
            for item in data:
                name, price, amount = item
                message += "item : {}    amount : {}    price : {}\n".format(name, amount, float(price)*amount)
                sum += float(price)*amount

            message += "\nTotal Price : {}".format(sum)

        # the user wants the bill -> the table closed -> i delete every thing from his bill and print it .
            cur.execute("DELETE FROM total_bill").fetchall()
            con.commit()

        # clean the 'client_order_list_box' and show the message created .
            display_bill()
            messagebox.showinfo("Success", message)

    # create another button for printing the bill .
        self.print_bill_button = Button(frame, text='Print Bill', font='Times 12 bold', bd=6, height=1, width=21,
                                        command=print_bill)
        self.print_bill_button.place(x=2, y=485)




    def choose_pasta(self):
        pick_paste = pickPasta.PickPasta()

    def choose_pizza(self):
        pick_pizza = pickPizza.PickPizza()

    def choose_fish(self):
        pick_fish = pickFish.PickFish()

    def choose_meat(self):
        pick_meat = pickMeat.PickMeat()

    def choose_hot_drink(self):
        pick_hot_drink = pickHotDrink.PickHotDrink()

    def choose_cold_drink(self):
        pick_cold_drink = pickColdDrink.PickColdDrink()

    def choose_dessert(self):
        pick_dessert = pickDessert.PickDessert()

    def choose_alcohol(self):
        pick_alcohol = pickAlcohol.PickAlcohol()











