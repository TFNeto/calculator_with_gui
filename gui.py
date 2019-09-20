from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E


class calcgui:
    def __init__(self, master):
        self.master = master
        h = 6
        w = 6
        master.title("Calculator")
        button_one = Button(master, text="1", height=h, width=w)
        button_two = Button(master, text="2", height=h, width=w)
        button_three = Button(master, text="3", height=h, width=w)
        button_four = Button(master, text="4", height=h, width=w)
        button_five = Button(master, text="5", height=h, width=w)
        button_six = Button(master, text="6", height=h, width=w)
        button_seven = Button(master, text="7", height=h, width=w)
        button_eight = Button(master, text="8", height=h, width=w)
        button_nine = Button(master, text="9", height=h, width=w)
        button_equal = Button(master, text="=", height=8, width=w)
        # layout
        Label(master, text="0").grid(
            row=0, rowspan=2, columnspan=5, sticky=W+E)
        button_one.grid(row=3, column=0, sticky=W+E)
        button_two.grid(row=3, column=1, sticky=W+E)
        button_three.grid(row=3, column=2, sticky=W+E)
        button_four.grid(row=4, column=0, sticky=W+E)
        button_five.grid(row=4, column=1, sticky=W+E)
        button_six.grid(row=4, column=2, sticky=W+E)
        button_seven.grid(row=5, column=0, sticky=W+E)
        button_eight.grid(row=5, column=1, sticky=W+E)
        button_nine.grid(row=5, column=2, sticky=W+E)
        button_equal.grid(row=4, column=3, rowspan=2, sticky=W+E)


root = Tk()
calc = calcgui(root)
root.mainloop()
