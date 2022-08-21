from tkinter import *

M_COL = "light blue"


class Fetcher:

    def __init__(self, x):
        self.window = Tk()
        self.window.title('eBird data fetcher')
        self.window.geometry("300x300")
        self.window.config(bg=M_COL, pady=20, padx=20)

        self.x = int(x)

        self.num = Label(text="How many: ", fg="black", bg=M_COL)
        self.num.grid(row=0, column=0)

        self.num_entry = Entry(self.window)
        self.num_entry.grid(row=0, column=1)

        self.add_button = Button(text="Add", command=self.fetch_num)
        self.add_button.grid(row=0, column=2)

        self.canvas = Canvas(self.window, width=200, height=200, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.label = self.canvas.create_text(50, 50, text="test species", fill="black")

        self.button = Button(text="Fetch data", command=self.generate)
        self.button.grid(row=2, column=0)

        self.window.mainloop()

    def generate(self):
        self.canvas.itemconfig(self.label, text="new")

    def fetch_num(self):
        self.x = int(self.num_entry.get())
        self.num_entry.delete(0, END)

