from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, StringVar


class calcgui:
    def __init__(self, master):
        self.master = master
        self.total = 0
        self.result = StringVar()
        self.totalstring = "0"
        self.parcel = ""
        self.number = 0
        self.result.set(self.totalstring)
        master.title("Calculator")

        total_label = Label(master, textvariable=self.result)
        total_label.grid(row=0, column=1)

        # gui options
        h = 6  # buttons height
        w = 6  # buttons width
        color = "azure"

        # buttons
        button_zero = Button(master, text="0", height=h,
                             width=w, bd=0, bg='azure')
        button_one = Button(master, text="1", height=h,
                            width=w, bd=0, bg=color, command=lambda: self.update("one"))
        button_two = Button(master, text="2", height=h,
                            width=w, bd=0, bg='azure')
        button_three = Button(master, text="3", height=h,
                              width=w, bd=0, bg='azure')
        button_four = Button(master, text="4", height=h,
                             width=w, bd=0, bg='azure')
        button_five = Button(master, text="5", height=h,
                             width=w, bd=0, bg='azure')
        button_six = Button(master, text="6", height=h,
                            width=w, bd=0, bg='azure')
        button_seven = Button(master, text="7", height=h,
                              width=w, bd=0, bg='azure')
        button_eight = Button(master, text="8", height=h,
                              width=w, bd=0, bg='azure')
        button_nine = Button(master, text="9", height=h,
                             width=w, bd=0, bg='azure')
        button_equal = Button(master, text="=", height=12,
                              width=w, bd=0, bg='azure')
        button_plus = Button(master, text="+", height=h,
                             width=w, bd=0, bg='azure')
        button_minus = Button(master, text="-", height=h,
                              width=w, bd=0, bg='azure')
        button_multiply = Button(
            master, text="x", height=h, width=w, bd=0, bg='azure')
        button_divide = Button(master, text="/", height=h,
                               width=w, bd=0, bg='azure')

        # interface
        button_zero.grid(row=6, column=1, sticky=W+E)
        button_one.grid(row=3, column=0, sticky=W+E)
        button_two.grid(row=3, column=1, sticky=W+E)
        button_three.grid(row=3, column=2, sticky=W+E)
        button_four.grid(row=4, column=0, sticky=W+E)
        button_five.grid(row=4, column=1, sticky=W+E)
        button_six.grid(row=4, column=2, sticky=W+E)
        button_seven.grid(row=5, column=0, sticky=W+E)
        button_eight.grid(row=5, column=1, sticky=W+E)
        button_nine.grid(row=5, column=2, sticky=W+E)
        button_plus.grid(row=3, column=3, sticky=W+E)
        button_minus.grid(row=4, column=3, sticky=W+E)
        button_multiply.grid(row=1, column=1, sticky=W+E)
        button_divide.grid(row=1, column=2, sticky=W+E)
        button_equal.grid(row=5, column=3, rowspan=2, sticky=W+E)

    def update(self, method):
        if method == "one":
            self.parcel += "1"
            if self.totalstring == "0":
                self.totalstring = self.parcel
        self.totalstring = self.parcel
        self.result.set(self.totalstring)


root = Tk()
calc = calcgui(root)
root.mainloop()
