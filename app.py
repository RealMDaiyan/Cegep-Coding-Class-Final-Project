from tkinter import *

class MainMenu:
    def __init__(self):
        
        self.main_menu_window = Tk()
        self.main_menu_window.title("Currency Converter")
        self.main_menu_window.geometry("600x480")
        
        self.converter_choice = IntVar()
        self.converter_choice.set(-1)

        self.header_label = Label(self.main_menu_window, text="Currency Converter")
        self.header_label.grid(row=0, column=0)

        self.usd_label = Label(self.main_menu_window, text="USD")
        self.usd_label.grid(row=1, column=0)
        self.usd_button = Radiobutton(self.main_menu_window, var=self.converter_choice, value=0)
        self.usd_button.grid(row=1, column=1)

        self.yen_label = Label(self.main_menu_window, text="Yen")
        self.yen_label.grid(row=2, column=0)
        self.yen_button = Radiobutton(self.main_menu_window, var=self.converter_choice, value=1)
        self.yen_button.grid(row=2, column=1)

        self.euro_label = Label(self.main_menu_window, text="Euro")
        self.euro_label.grid(row=3, column=0)
        self.euro_button = Radiobutton(self.main_menu_window, var=self.converter_choice, value=2)
        self.euro_button.grid(row=3, column=1)

        self.juan_label = Label(self.main_menu_window, text="Juan")
        self.juan_label.grid(row=4, column=0)
        self.juan_button = Radiobutton(self.main_menu_window, var=self.converter_choice, value=3)
        self.juan_button.grid(row=4, column=1)

        self.rs_label = Label(self.main_menu_window, text="RS")
        self.rs_label.grid(row=5, column=0)
        self.rs_button = Radiobutton(self.main_menu_window, var=self.converter_choice, value=4)
        self.rs_button.grid(row=5, column=1)

        self.choose_button = Button(self.main_menu_window, text="Choose", comman=self.choose)
        self.choose_button.grid(row=6, column=0)


        self.main_menu_window.mainloop()
    
    def choose(self):
        print("Hello")




main = MainMenu()