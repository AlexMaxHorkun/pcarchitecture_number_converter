__author__ = 'Alexander Gorkun'
__email__ = 'mindkilleralexs@gmail.com'

import tkinter as tk
from tkinter import messagebox
from alexander_gorkun.number_converter import converter
from alexander_gorkun.number_converter import validator


class AGNumberConverterGui(tk.Frame):
    title = "Alexander Gorkun's Numbers Converter"
    __converter=None
    __from_system=None
    __to_system=None
    quit_button = None
    title_label=None
    fromnumeration_label = None
    tonumeration_label = None
    convert_button = None
    number_entry = None
    result_label = None
    __last_row=5
    __last_col=3

    def __init__(self, conv):
        """
        :param converter: Converter instance to convert numbers from one system to another.
        """
        super().__init__(tk.Tk())
        assert isinstance(conv, converter.Converter)
        self.__converter=conv
        self.__from_system=tk.StringVar(self)
        self.__to_system=tk.StringVar(self)
        self.__from_system.set(converter.NUMERATION_BINARY)
        self.__to_system.set(converter.NUMERATION_DECIMAL)

    def __create_quit_button(self):
        """
        Put a quit button on window.
        """
        self.quit_button = tk.Button(self, text='Quit', command=self.quit)
        self.quit_button.grid(row=self.__last_row, column=self.__last_col, pady=5)

    def __create_title(self):
        """
        Create label widget 'title'.
        """
        self.title_label=tk.Label(self, text="Welcome to Alexander Gorkun's number converter\n"
                                             "Click \"Convert\" to convert "
                                             "a number from one numeration to another")
        self.title_label.grid(row=1, column=1, columnspan=self.__last_col)

    def __create_fromnumeration_select(self):
        """
        Create listbox widget to select which numeration system to convert from.
        """
        if not self.fromnumeration_label:
            self.__create_fromnumeration_label()
        from1=tk.Radiobutton(self.fromnumeration_label, variable=self.__from_system,
                             value=converter.NUMERATION_BINARY, text="Binary system")
        from2=tk.Radiobutton(self.fromnumeration_label, variable=self.__from_system,
                             value=converter.NUMERATION_DECIMAL, text="Decimal system")
        from3=tk.Radiobutton(self.fromnumeration_label, variable=self.__from_system,
                             value=converter.NUMERATION_HEXADECIMAL, text="Hexadecimal system")
        from1.grid()
        from2.grid()
        from3.grid()

    def __create_fromnumeration_label(self):
        self.fromnumeration_label=tk.LabelFrame(self, text="From system")
        self.fromnumeration_label.grid(row=2, column=1)

    def __create_tonumeration_select(self):
        """
        Create listbox widget to select which numeration system to convert to.
        """
        if not self.tonumeration_label:
            self.__create_tonumeration_label()
        to1=tk.Radiobutton(self.tonumeration_label, variable=self.__to_system,
                             value=converter.NUMERATION_BINARY, text="Binary system")
        to2=tk.Radiobutton(self.tonumeration_label, variable=self.__to_system,
                             value=converter.NUMERATION_DECIMAL, text="Decimal system")
        to3=tk.Radiobutton(self.tonumeration_label, variable=self.__to_system,
                             value=converter.NUMERATION_HEXADECIMAL, text="Hexadecimal system")
        to1.grid()
        to2.grid()
        to3.grid()

    def __create_tonumeration_label(self):
        self.tonumeration_label=tk.LabelFrame(self, text="To system")
        self.tonumeration_label.grid(row=2, column=3)

    def __create_convert_button(self):
        """
        Create button widget, when clicked converting starts.
        """
        conv=self.__converter
        number_entry_widget=self.number_entry
        fromsystem_container=self.__from_system
        tosystem_container=self.__to_system
        result_widget=self.result_label
        def onclick():
            fromsystem=int(fromsystem_container.get())
            tosystem=int(tosystem_container.get())
            number=number_entry_widget.get()
            if not number:
                messagebox.showerror("Number field is empty",
                                     "Number field cannot be empty")
                return
            if conv.can_convert(fromsystem, tosystem):
                if validator.validate_number(number, fromsystem):
                    converted_number=conv.convert(number, fromsystem, tosystem)
                    result_widget['text']=converted_number
                else:
                    messagebox.showerror("Given number invalid",
                                         "Given number is not a valid number of given numeration system")
            else:
                messagebox.showerror("Impossible to convert",
                                     "No converter available to convert "
                                     "from given system to another")

        self.convert_button=tk.Button(self, text="Convert", command=onclick)
        self.convert_button.grid(row=3, column=2, pady=5, padx=3)

    def __create_number_entry(self):
        """
        Creates entry widget 'number' to put number to convert.
        """
        self.number_entry = tk.Entry(self)
        self.number_entry.grid(row=3, column=1)

    def __create_result_label(self):
        """
        Creates label widget 'result' where result of converting will be shown.
        """
        labelframe=tk.LabelFrame(self, text="Result of converting")
        labelframe.grid(column=3, row=3)
        self.result_label=tk.Label(labelframe)
        self.result_label.grid()

    def __create_widgets(self):
        """
        Sets up widgets for window.
        """
        self.__create_title()
        self.__create_fromnumeration_select()
        self.__create_tonumeration_select()
        self.__create_number_entry()
        self.__create_result_label()
        self.__create_quit_button()
        self.__create_convert_button()

    def start(self):
        """
        Starts the GUI app.
        """
        self.master.wm_title(self.title)
        self.grid(padx=10, pady=6)
        self.__create_widgets()
        self.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.master.resizable(width=False, height=False)
        self.mainloop()