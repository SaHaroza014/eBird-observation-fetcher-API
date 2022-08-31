from tkinter import *

M_COL = "light blue"


class Fetcher:

    def __init__(self, x):
        self.window = Tk()
        self.window.title('eBird data fetcher')
        self.window.geometry("400x400")
        self.window.config(bg=M_COL, pady=20, padx=20)

        self.x = int(x)

        self.num = Label(text="How many species: ", fg="black", bg=M_COL)
        self.num.grid(row=0, column=0)

        self.num_entry = Entry(self.window)
        self.num_entry.grid(row=0, column=1)
        self.num_entry.focus()

        self.add_button = Button(text="Add", command=self.fetch_num)
        self.add_button.grid(row=0, column=2)

        self.info = Label(text="Press 'Add' button to update file!", bg=M_COL, pady=20)
        self.info.grid(row=1, column=0)

        self.window.mainloop()

    def fetch_num(self):
        self.x = int(self.num_entry.get())
        self.num_entry.delete(0, END)
        self.info.config(text="Added data to a file!", bg="white", pady=0)

