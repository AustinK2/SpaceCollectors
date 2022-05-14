import tkinter
import tkinter.font as tkfont
import time

"""
Use a GUI interface
Be object oriented (classes and objects)
Use an external data file
Appropriately organized into functions
Be well documented (appropriate names and comments)
Use looping structures
Use data structures (e.g. lists, dictionaries, class objects that hold data)
Clean code, no warnings
"""

class Management:
    def __init__(self):

        # Creating Main Window
        self.main_window = tkinter.Tk()
        self.main_window.config(bg="dim gray")
        # Creates minimum window size instead of auto-sizing
        self.main_window.geometry("1600x800+0+0")
        self.main_window.title("Restaurant Management System (RMS)")
        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(size=20)

        # Setting up time to display
        self.__time = time.strftime("%I:%M:%S")

        # Creating Frame layout (Register at the top, food items on the left side, total calculations on the right side, time at bottom)
        # Colors are used to test out the zones of the frames
        self.__top = tkinter.Frame(self.main_window)
        self.__top.pack(side="top")
        self.__bottom = tkinter.Frame(self.main_window)
        self.__bottom.pack(side="bottom")
        self.__left_main = tkinter.Frame(self.main_window, bg="dim gray")
        self.__left_main.pack(side="left", anchor="nw")
        self.__right_main = tkinter.Frame(self.main_window, bg="dim gray")
        self.__right_main.pack(side="right", anchor="ne")
        # Creating frame inside frame (top_left inside left_main)
        self.__row1 = tkinter.Frame(self.__left_main, bg="dim gray")
        self.__row1.pack(side="left", in_=self.__left_main)
        self.__register_label = tkinter.Label(self.__top, text="Register 1", width=1600, height=1, relief="raised",
                                              bg="red2")
        self.__register_label.pack(pady=5)

        # Condiments Menu (Add)
        self.__condiments_button = tkinter.Button(self.__bottom, text='Condiments', width=15, height=1, relief='raised', bg='red2', command=lambda: Condiments.start_window(self))
        self.__condiments_button.pack(anchor='n')

        # Creating time label and packing it
        self.__time_label = tkinter.Label(self.__bottom, width=1600, text=self.__time, relief="raised",
                                          bg="red2")
        self.__time_label.pack(pady=5)

        # Creating logo in top right
        try:
            logo = tkinter.PhotoImage(file='logo3.png')
        except tkinter.TclError:
            print("No company logo found.")
            self.__logo = tkinter.Canvas(self.__right_main, width=900, height=900, bg="dim gray")
            self.__logo.pack()
        else:
            resized_logo = logo.subsample(3,3)
            self.__logo = tkinter.Canvas(self.__right_main, width=900, height=900, bg="dim gray")
            self.__logo.pack()
            self.__logo.create_image(750, 120, image=resized_logo)

        # https://stackoverflow.com/questions/7137636/how-can-i-add-a-lot-of-buttons-to-the-tkinter-frame-efficiently
        # Credit to Unutbu on StackOverflow for the idea of looping to create the buttons, with the following code:
        # Need to use as list
        global names
        global prices
        names = ['Add Entry', 'Add Entry', 'Add Entry', 'Add Entry', 'Add Entry', 'Add Entry', 'Add Entry', 'Add Entry',
                 'Add Entry', 'Add Entry', 'Add Entry', 'Add Entry', 'Add Entry', 'Add Entry', 'Add Entry']
        prices = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.button = []
        for i, name in enumerate(names):
            if i < 5:
                # Adds new button to list (frame of placement, default name, width, height, callback to allow changing entry name and price)
                self.button.append(
                    tkinter.Button(self.__row1, text=name, width=15, height=3, bg="red2", command=self.callback(i + 1, name)))
                # self.button[i].pack(pady=5, padx=5)
                self.button[i].grid(column=0, row=i, padx=5, pady=5)
            elif i < 10:
                self.button.append(
                    tkinter.Button(self.__row1, text=name, width=15, height=3, bg="red2", command=self.callback(i + 1, name)))
                self.button[i].grid(column=2, row=i-5, padx=5, pady=5)
                # self.button[i].pack(pady=5, padx=5)
            else:
                self.button.append(
                    tkinter.Button(self.__row1, text=name, width=15, height=3, bg="red2", command=self.callback(i + 1, name)))
                self.button[i].grid(column=3, row=i-10, padx=5, pady=5)
                # self.button[i].pack(pady=5, padx=5)

            # Credit of Unutbu ends, some code has been modified to fit project



        tkinter.mainloop()
    # Replacing default entry button values with user created ones
    def set_entry(self, price, name_revision, c):
        print("Setting entry to: ", name_revision)
        self.button[c-1].config(text=name_revision)
        # HAVE TO SET THE NAME IN NAMES ARRAY, MIGHT HAVE TO USE RETURN
        names[c-1] = name_revision
        print("Set to: ", self.button[c-1].cget("text"))
        print("In names: ", names[c-1])
        print(names)
        # Prices Change
        print("Setting price to: ", price)
        prices[c-1] = price
        print("Set to: ", prices[c-1])
        print("In prices: ", prices[c-1])
        print(prices)
        # print(name_revision.get())
        # print(self.button[c].set(price))     TESTING SETTING... but button object has no attribute set?

    def send_food(self, button_num):
        print(button_num)
        #total += prices[button_num]
        #print("Total:", total)




    def callback(self, i, name):  # This is the callback factory. Calling it returns a function.

        def _callback():
            print(i, name)  # I tells you which button has been pressed.
            if names[i-1] == "Add Entry":
                # Creating New Entry Window
                entry_window = tkinter.Tk()
                x = self.main_window.winfo_pointerx() - self.main_window.winfo_vrootx()
                y = self.main_window.winfo_pointery() - self.main_window.winfo_vrooty()
                entry_window_mouse_pos = "400x150"+"+"+str(x)+"+"+str(y)
                entry_window.geometry(entry_window_mouse_pos)
                entry_window.resizable(False, False)
                entry_window.title("Restaurant Management System (RMS) - Add New Entry")
                # Creating frames for labels and inputs
                entry_window.__top = tkinter.Frame(entry_window)
                entry_window.__top.pack(side="top")
                entry_window.__bottom = tkinter.Frame(entry_window)
                entry_window.__bottom.pack(side="bottom")
                entry_window.__name_label = tkinter.Label(entry_window.__top, text="Enter entry name:", width=15,
                                                          height=5, relief="flat", bg="red2")
                entry_window.__name_label.pack(side="left")
                # Creating string variable I can use to return to main window to set the text of said button
                name_entered = tkinter.StringVar()
                entry_window.__name_entrybox = tkinter.Entry(entry_window.__top, width=20, relief="flat",
                                                             bg="red2", bd=8, textvariable=name_entered)
                entry_window.__name_entrybox.pack(side="left", padx=10)
                entry_window.__name_entrybox.focus()
                entry_window.__price_label = tkinter.Label(entry_window.__bottom, text="Enter entry price:", width=15,
                                                           height=5, relief="flat", bg="red2")
                entry_window.__price_label.pack(side="left")
                price_entered = tkinter.IntVar()
                entry_window.__price_entrybox = tkinter.Entry(entry_window.__bottom, width=20, relief="flat", bg="red2", bd=8)
                entry_window.__price_entrybox.pack(side="left", padx=10)
                entry_window.__entry_cancel_button = tkinter.Button(entry_window.__top, text="Cancel", width=50,
                                                                    height=3, command=lambda: entry_window.destroy())
                entry_window.__entry_cancel_button.pack(pady=5, padx=5)
                entry_window.__entry_exit_button = tkinter.Button(entry_window.__bottom, text="Save & Exit", width=50,
                                                                  height=3, command=lambda c=i: [name_entered.set(entry_window.__name_entrybox.get()),
                                                                                                 price_entered.set(entry_window.__price_entrybox.get()),
                                                                                                 self.set_entry(price_entered.get(), name_entered.get(), c),
                                                                                                 entry_window.destroy()])
                                                                                    # lambda forces to wait for input, c temporarily holds that value.
                # Got the idea of C=i and temporary storage from Ethan Field on StackOverflow: https://stackoverflow.com/questions/45728548/how-can-i-get-the-button-id-when-it-is-clicked
                entry_window.__entry_exit_button.pack(pady=5, padx=5)
            else:
                print("THIS COMMAND", self.button[i-1].cget("text"))
                choose_window = tkinter.Tk()
                x = self.main_window.winfo_pointerx() - self.main_window.winfo_vrootx()
                y = self.main_window.winfo_pointery() - self.main_window.winfo_vrooty()
                mouse_pos = "+"+str(x)+"+"+str(y)
                choose_window.geometry(mouse_pos)
                choose_window.resizable(False, False)
                choose_window.title("Restaurant Management System (RMS) - Choose Condiments")
                choose_window.__top = tkinter.Frame(choose_window)
                choose_window.__top.pack(side="top")
                choose_window.__bottom = tkinter.Frame(choose_window)
                choose_window.__bottom.pack(side="bottom")
                choose_window.__choose_label = tkinter.Label(choose_window.__top, text="Choose condiments\n======================", width=25,
                                                           height=5, relief="flat", bg="red2")
                choose_window.__choose_label.pack(side="left")

                if condiments[0] == "Add Entry":
                    choose_window.__no_condiments_label = tkinter.Label(choose_window.__bottom, text="No Condiments to choose from.", width=25,
                                                           height=5, relief="flat", bg="red2")
                    choose_window.__no_condiments_label.pack(side="bottom")
                    choose_window.__quit_button = tkinter.Button(choose_window.__bottom, text="Quit", relief="groove", width=24, height=5, bg="dim gray", command=lambda: choose_window.destroy())
                    choose_window.__quit_button.pack(side="bottom", padx=2, pady=2)
                elif len(condiments) < 10:
                    # Creating dictionary in format "Condiment" : IntVar() Value
                    global checked_options
                    checked_options = {}
                    choose_window.__checkbox = []
                    my_IntVars = []
                    # checkbox = tkinter.Checkbutton(choose_window.__bottom, relief="groove", onvalue=1, offvalue=0)

                    for index, condiment in enumerate(condiments):
                        # Creating a single variable for each condiment, then updating the dictionary with the condiment and its respective IntVar()
                        # var = tkinter.IntVar()
                        # var.set(0)
                        my_IntVars.append(tkinter.IntVar(value=0))
                        checked_options.update([(condiment, my_IntVars[index])])
                        print(checked_options)
                        # Creating a singular checkbox entry, adding it to list of checkboxes, displaying the condiment name, variable is default 0
                        choose_window.__checkbox.append(tkinter.Checkbutton(choose_window.__bottom, relief="groove", onvalue=1, offvalue=0))
                        choose_window.__checkbox[index].pack(padx=3, pady=3, side="bottom")
                        print(checked_options[condiment].get())
                        choose_window.__checkbox[index].configure(text=condiment, variable=my_IntVars[index], command=lambda: [(checked_options[condiment]).set((checked_options[condiment].get() + 1) % 2), print("Value changed: ", (checked_options[condiment]).get(), "FROM", condiment), self.update_dict(condiment, my_IntVars[index])])
                        # checked_options[condiment].set(var.get())
                        # Submit Button, once clicked it will send the data of var to update dict
                        # print(choose_window.__checkbox)
                    choose_window.__submit = tkinter.Button(choose_window.__bottom, relief="raise", text="Submit", command=lambda: [print(checked_options[condiment].get()), choose_window.destroy()])
                    choose_window.__submit.pack(side="right")




        return _callback

    def update_dict(self, single_condiment, var_updated):
        old = checked_options.get(single_condiment)
        print(old.get())
        checked_options.update([[single_condiment, var_updated]])
        print("UPDATED", old.get(), checked_options[single_condiment].get())
        for index, option in enumerate(checked_options):
            list = []
            list.append(checked_options[option].get())
        print("THIS IS THE LIST:", list)
        print(checked_options)

    #def submit_order(self):
        #for


class Condiments(Management):
    def __init__(self):
        Management.__init__(self)
    global condiments
    condiments = ['Add Entry']


    def start_window(self):
        global condiment_window
        global condiment_list
        condiment_window = tkinter.Tk()
        x = self.main_window.winfo_pointerx() - self.main_window.winfo_vrootx() - 150
        y = self.main_window.winfo_pointery() - self.main_window.winfo_vrooty() - 150
        mouse_pos = "600x250"+"+"+str(x)+"+"+str(y)
        condiment_window.geometry(mouse_pos)
        condiment_window.resizable(False, False)
        condiment_window.title("Restaurant Management System (RMS) - Add New Condiments")
        condiment_window.__top = tkinter.Frame(condiment_window)
        condiment_window.__top.grid(row=0, column=0, pady=5, padx=3)
        condiment_window.__bottom = tkinter.Frame(condiment_window)
        condiment_window.__bottom.grid(row=0, column=0, pady=5, padx=3)
        condiment_window.__name_label = tkinter.Label(condiment_window.__top, width=20, height=2, relief='flat', bg='red2', text='Condiment Name:')
        condiment_window.__name_label.grid(row=0, column=1, pady=5, padx=3)
        condiment_window.__entry_box = tkinter.Entry(condiment_window.__top, width=20, relief='flat', bg='red2', bd=9)
        condiment_window.__entry_box.grid(row=0, column=2, pady=5, padx=3)
        condiment_window.__entry_box.focus()
        condiment_window.__submit = tkinter.Button(condiment_window.__top, text='Submit', width=15, height=1, relief='raised', command=lambda: [Condiments.submit_condiment(self, condiment_window.__entry_box.get()), condiment_window.__entry_box.delete(0, 'end')])
        condiment_window.__submit.grid(row=0, column=3, pady=5, padx=3)
        condiment_list = tkinter.Listbox(condiment_window.__top, bg='lightsteelblue3', width=30)
        condiment_list.grid(column=1, row=1, rowspan=1)
        selection = condiment_list.curselection()
        condiment_window.__delete = tkinter.Button(condiment_window.__top, text='Delete', width=15, height=1, relief='raised', command=lambda: [condiment_list.delete(condiment_list.curselection()), condiments.remove(condiment_list.curselection())])
        # [condiments.remove(condiment_list.get_index_selection()), condiment_list.delete(condiment_list.curselection())])
        condiment_window.__delete.grid(row=1, column=3, pady=5, padx=3)
        if condiments[0] != 'Add Entry':
            for condiment in condiments:
                condiment_list.insert(len(condiments), condiment)
        print("COMPLETE")

    def get_index_selection(self):
        for item in condiment_list.curselection():
            return item

    def submit_condiment(self, condiment):
        condiment_length = len(condiments)
        print(condiment_length)
        condiment_frame = tkinter.Frame(condiment_window, bg='black')
        condiment_frame.grid(row=1, column=1, pady=5)
        if condiments[0] == 'Add Entry' and condiment_length == 1:
            condiments[0] = condiment
            print("Set condiment.", condiments)
            condiment_list.insert(condiment_length, condiment)
        else:
            condiments.append(condiment)
            condiment_list.insert(condiment_length, condiment)
            # print("Condiment", condiment_length, "has been set to", condiment, condiments)

my_register = Management()
