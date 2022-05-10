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


"""
CURRENT PROBLEMS:
1. After hitting submit on the entry form with inputs in the fields, those values seem to be stuck in a variable (py_var)
While trying to retrieve those values I.E .get() methods... Buttons do not allow for a .get method as they dont have the attribute
2. With the code just like this, if you set one entry it shows py_var which can be resolved. but when you set a second one sometimes it sets a almost random (maybe not random) button's text
to the next py_variable
3. Does StringVar() hold the entire value of the text entry when called? Should I create a placeholder to store that value right after its called?
4. Names/Prices parralel list? Dictionary? Which best suits it? Would it be better to get the index of the button's name it is trying to change and since the default price is 0, then set that
to the user entered price?
5. Row3... Do I have to make a new frame like top_left in order to make a third row? Or is there an easier way like writing side="right" somewhere?

"""


class Management:
    def __init__(self):
        # Creating Main Window
        self.main_window = tkinter.Tk()
        self.main_window.config(bg="royal blue4")
        # Creates minimum window size instead of auto-sizing
        self.main_window.geometry("1600x800+0+0")
        self.main_window.title("Restaurant Management System (RMS)")
        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(size=20)
        # Setting up time to display
        self.__time = time.asctime(time.localtime(time.time()))
        # Creating Frame layout (Register at the top, food items on the left side, total calculations on the right side, time at bottom)
        # Colors are used to test out the zones of the frames
        self.__top = tkinter.Frame(self.main_window)
        self.__top.pack(side="top")
        self.__bottom = tkinter.Frame(self.main_window)
        self.__bottom.pack(side="bottom")
        self.__left_main = tkinter.Frame(self.main_window, bg="blue")
        self.__left_main.pack(side="left", anchor="nw")
        # Creating frame inside frame (top_left inside left_main)
        self.__row1 = tkinter.Frame(self.__left_main, bg="royal blue4")
        self.__row1.pack(side="left", in_=self.__left_main)
        self.__row2 = tkinter.Frame(self.__left_main, bg="green")
        self.__row2.pack(side="right", in_=self.__left_main)
        self.__row3 = tkinter.Frame(self.__left_main, bg="blue")
        self.__row3.pack(side="right", in_=self.__left_main, anchor="e")
        self.__register_label = tkinter.Label(self.__top, text="Register 1", width=1600, height=1, relief="raised",
                                              bg="White")
        self.__register_label.pack(pady=5)
        self.__time_label = tkinter.Label(self.__bottom, text=self.__time, width=1600, relief="raised",
                                          bg="OrangeRed2")
        self.__time_label.pack(pady=5)

        # https://stackoverflow.com/questions/7137636/how-can-i-add-a-lot-of-buttons-to-the-tkinter-frame-efficiently
        # Credit to Unutbu on StackOverflow for the idea of looping to create the buttons, with the following code:
        # names = tkinter.StringVar()
        names = ('Add Entry', 'Add Entry', 'Add Entry', 'Add Entry', 'Add Entry', 'Add Entry', 'Add Entry', 'Add Entry',
                 'Add Entry', 'Add Entry', 'Add Entry', 'Add Entry', 'Add Entry', 'Add Entry', 'Add Entry')
        prices = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        self.button = []
        for i, name in enumerate(names):
            if i < 5:
                # Adds new button to list (frame of placement, default name, width, height, callback to allow changing entry name and price)
                self.button.append(
                    tkinter.Button(self.__row1, text=name, width=15, height=3, command=self.callback(i + 1, name)))
                # self.button[i].pack(pady=5, padx=5)
                self.button[i].grid(column=0, row=i, padx=5, pady=5)
            elif i < 10:
                self.button.append(
                    tkinter.Button(self.__row1, text=name, width=15, height=3, command=self.callback(i + 1, name)))
                self.button[i].grid(column=2, row=i-5, padx=5, pady=5)
                # self.button[i].pack(pady=5, padx=5)
            else:
                self.button.append(
                    tkinter.Button(self.__row1, text=name, width=15, height=3, command=self.callback(i + 1, name)))
                self.button[i].grid(column=3, row=i-10, padx=5, pady=5)
                # self.button[i].pack(pady=5, padx=5)
        tkinter.mainloop()
    # Replacing default entry button values with user created ones
    def set_entry(self, price, name_revision, c):
        print("Setting entry to: ", name_revision)
        self.button[c-1].config(text=name_revision)
        # HAVE TO SET THE NAME IN NAMES ARRAY, MIGHT HAVE TO USE RETURN
        global names
        names[c-1] = name_revision
        print("Set to: ", self.button[c-1].cget("text"))
        print("In names: ", names[c-1])
        # print(name_revision.get())
        # print(self.button[c].set(price))     TESTING SETTING... but button object has no attribute set?


    def callback(self, i, name):  # This is the callback factory. Calling it returns a function.

        def _callback():
            print(i, name)  # I tells you which button has been pressed.
            if name == "Add Entry":
                # Creating New Entry Window
                entry_window = tkinter.Tk()
                entry_window.geometry("400x150+0+0")
                entry_window.resizable(False, False)
                entry_window.title("Restaurant Management System (RMS) - Add New Entry")
                # Creating frames for labels and inputs
                entry_window.__top = tkinter.Frame(entry_window)
                entry_window.__top.pack(side="top")
                entry_window.__bottom = tkinter.Frame(entry_window)
                entry_window.__bottom.pack(side="bottom")
                entry_window.__name_label = tkinter.Label(entry_window.__top, text="Enter entry name:", width=15,
                                                          height=5, relief="flat", bg="OrangeRed2")
                entry_window.__name_label.pack(side="left")
                # Creating string variable I can use to return to main window to set the text of said button
                name_entered = tkinter.StringVar()
                entry_window.__name_entrybox = tkinter.Entry(entry_window.__top, width=20, relief="flat",
                                                             bg="OrangeRed2", bd=8, textvariable=name_entered)
                entry_window.__name_entrybox.pack(side="left", padx=10)
                entry_window.__name_entrybox.focus()
                entry_window.__price_label = tkinter.Label(entry_window.__bottom, text="Enter entry price:", width=15,
                                                           height=5, relief="flat", bg="OrangeRed2")
                entry_window.__price_label.pack(side="left")
                price_entered = tkinter.IntVar()
                entry_window.__price_entrybox = tkinter.Entry(entry_window.__bottom, textvariable=price_entered,
                                                              width=20, relief="flat", bg="OrangeRed2", bd=8)
                entry_window.__price_entrybox.pack(side="left", padx=10)
                entry_window.__entry_cancel_button = tkinter.Button(entry_window.__top, text="Cancel", width=50,
                                                                    height=3, command=lambda: entry_window.destroy())
                entry_window.__entry_cancel_button.pack(pady=5, padx=5)
                entry_window.__entry_exit_button = tkinter.Button(entry_window.__bottom, text="Save & Exit", width=50,
                                                                  height=3, command=lambda c=i: [name_entered.set(entry_window.__name_entrybox.get()), self.set_entry(price_entered, name_entered.get(), c), entry_window.destroy()])
                                                                                    # lambda forces to wait for input, c temporarily holds that value.
                # Got the idea of C=i and temporary storage from Ethan Field on StackOverflow: https://stackoverflow.com/questions/45728548/how-can-i-get-the-button-id-when-it-is-clicked
                entry_window.__entry_exit_button.pack(pady=5, padx=5)
            else:
                print("THIS COMMAND", self.button[i].cget("text"))





                """
                ORIGINAL CODE
                name_entered = tkinter.StringVar()
                entry_window.__name_entrybox = tkinter.Entry(entry_window.__top, width=20, relief="flat",
                                                             bg="OrangeRed2", bd=8, textvariable=name_entered)
                entry_window.__name_entrybox.pack(side="left", padx=10)
                entry_window.__name_entrybox.focus()
                entry_window.__price_label = tkinter.Label(entry_window.__bottom, text="Enter entry price:", width=15,
                                                           height=5, relief="flat", bg="OrangeRed2")
                entry_window.__price_label.pack(side="left")
                price_entered = tkinter.IntVar()
                entry_window.__price_entrybox = tkinter.Entry(entry_window.__bottom, textvariable=price_entered,
                                                              width=20, relief="flat", bg="OrangeRed2", bd=8)
                entry_window.__price_entrybox.pack(side="left", padx=10)
                entry_window.__entry_cancel_button = tkinter.Button(entry_window.__top, text="Cancel", width=50,
                                                                    height=3, command=lambda: entry_window.destroy())
                entry_window.__entry_cancel_button.pack(pady=5, padx=5)
                entry_window.__entry_exit_button = tkinter.Button(entry_window.__bottom, text="Save & Exit", width=50,
                                                                  height=3, command=lambda c=i: [print(name_entered), self.set_entry(price_entered, name_entered, name, c), entry_window.destroy()])
                                                                                    # lambda forces to wait for input, c temporarily holds that value.
                                                                                                # Prints Py_var (Which holds the value of name_entered) how do I get it when it is a button and not label?
                                                                                                # Review Line 75, value is still Py_var"""

        return _callback

    # Credit of Unutbu ends, some code has been modified to fit project


my_register = Management()
