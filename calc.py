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
        self.oper = ""
        master.title("Calculator")

        total_label = Label(master, textvariable=self.result)
        total_label.grid(row=0, column=1)

        # gui options
        h = 6  # buttons height
        w = 6  # buttons width
        color = "azure"

        # buttons
        button_zero = Button(master, text="0", height=h,
                             width=w, bd=0, bg='azure', command=lambda: self.update("zero"))
        button_one = Button(master, text="1", height=h,
                            width=w, bd=0, bg=color, command=lambda: self.update("one"))
        button_two = Button(master, text="2", height=h,
                            width=w, bd=0, bg='azure', command=lambda: self.update("two"))
        button_three = Button(master, text="3", height=h,
                              width=w, bd=0, bg='azure', command=lambda: self.update("three"))
        button_four = Button(master, text="4", height=h,
                             width=w, bd=0, bg='azure', command=lambda: self.update("four"))
        button_five = Button(master, text="5", height=h,
                             width=w, bd=0, bg='azure', command=lambda: self.update("five"))
        button_six = Button(master, text="6", height=h,
                            width=w, bd=0, bg='azure', command=lambda: self.update("six"))
        button_seven = Button(master, text="7", height=h,
                              width=w, bd=0, bg='azure', command=lambda: self.update("seven"))
        button_eight = Button(master, text="8", height=h,
                              width=w, bd=0, bg='azure', command=lambda: self.update("eight"))
        button_nine = Button(master, text="9", height=h,
                             width=w, bd=0, bg='azure', command=lambda: self.update("nine"))
        button_equal = Button(master, text="=", height=12,
                              width=w, bd=0, bg='azure', command=lambda: self.equal())
        button_plus = Button(master, text="+", height=h,
                             width=w, bd=0, bg='azure', command=lambda: self.operation("add"))
        button_minus = Button(master, text="-", height=h,
                              width=w, bd=0, bg='azure', command=lambda: self.operation("minus"))
        button_multiply = Button(
            master, text="x", height=h, width=w, bd=0, bg='azure', command=lambda: self.operation("times"))
        button_divide = Button(master, text="/", height=h,
                               width=w, bd=0, bg='azure', command=lambda: self.operation("divide"))

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
            if self.totalstring == "0" or self.oper == "new":
                self.totalstring = self.parcel
                self.oper = "none"
                self.result.set(self.totalstring)
                return
            self.totalstring += "1"
            self.result.set(self.totalstring)
        elif method == "two":
            self.parcel += "2"
            if self.totalstring == "0" or self.oper == "new":
                self.totalstring = self.parcel
                self.oper = "none"
                self.result.set(self.totalstring)
                return
            self.totalstring += "2"
            self.result.set(self.totalstring)
        elif method == "three":
            self.parcel += "3"
            if self.totalstring == "0" or self.oper == "new":
                self.totalstring = self.parcel
                self.oper = "none"
                self.result.set(self.totalstring)
                return
            self.totalstring += "3"
            self.result.set(self.totalstring)
        elif method == "four":
            self.parcel += "4"
            if self.totalstring == "0" or self.oper == "new":
                self.totalstring = self.parcel
                self.oper = "none"
                self.result.set(self.totalstring)
                return
            self.totalstring += "4"
            self.result.set(self.totalstring)
        elif method == "five":
            self.parcel += "5"
            if self.totalstring == "0" or self.oper == "new":
                self.totalstring = self.parcel
                self.oper = "none"
                self.result.set(self.totalstring)
                return
            self.totalstring += "5"
            self.result.set(self.totalstring)
        elif method == "six":
            self.parcel += "6"
            if self.totalstring == "0" or self.oper == "new":
                self.totalstring = self.parcel
                self.oper = "none"
                self.result.set(self.totalstring)
                return
            self.totalstring += "6"
            self.result.set(self.totalstring)
        elif method == "seven":
            self.parcel += "7"
            if self.totalstring == "0" or self.oper == "new":
                self.totalstring = self.parcel
                self.oper = "none"
                self.result.set(self.totalstring)
                return
            self.totalstring += "7"
            self.result.set(self.totalstring)
        elif method == "eight":
            self.parcel += "8"
            if self.totalstring == "0" or self.oper == "new":
                self.totalstring = self.parcel
                self.oper = "none"
                self.result.set(self.totalstring)
                return
            self.totalstring += "8"
            self.result.set(self.totalstring)
        elif method == "nine":
            self.parcel += "9"
            if self.totalstring == "0" or self.oper == "new":
                self.totalstring = self.parcel
                self.oper = "none"
                self.result.set(self.totalstring)
                return
            self.totalstring += "9"
            self.result.set(self.totalstring)
        elif method == "zero":
            if self.totalstring == "0" or self.oper == "new":
                self.oper = "none"
                return
            self.parcel += "0"
            self.totalstring += "0"
            self.result.set(self.totalstring)

    def operation(self, op):
        self.oper = op
        if op == "add":
            self.totalstring += "+"
        elif op == "minus":
            self.totalstring += "-"
        elif op == "times":
            self.totalstring += "x"
        elif op == "divide":
            self.totalstring += "/"

        self.total = int(self.parcel)
        self.result.set(self.totalstring)
        self.parcel = ""

    def equal(self):
        if self.oper == "add":
            self.total += int(self.parcel)
            self.parcel = ""
            self.totalstring = self.total
            self.result.set(self.totalstring)
            self.total = 0
            self.oper = "new"
            return
        elif self.oper == "minus":
            self.total -= int(self.parcel)
            self.parcel = ""
            self.totalstring = self.total
            self.result.set(self.totalstring)
            self.total = 0
            self.oper = "new"
            return
        elif self.oper == "times":
            self.total *= int(self.parcel)
            self.parcel = ""
            self.totalstring = self.total
            self.result.set(self.totalstring)
            self.total = 0
            self.oper = "new"
            return
        elif self.oper == "divide":
            self.total /= int(self.parcel)
            self.parcel = ""
            self.totalstring = self.total
            self.result.set(self.totalstring)
            self.total = 0
            self.oper = "new"
            return


root = Tk()
calc = calcgui(root)
root.mainloop()
