from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# label
my_label = Label()
my_label.config(text="Miles to KM Conversion", font=("Arial", 14, "italic"))
my_label.grid(column=2, row=1)

my_label_output = Label()
my_label_output.config(text=f"Output: ", font=("Arial", 14, "italic"))
my_label_output.grid(column=3, row=2)

# button
def button_clicked():
    value = input.get()
    my_label_output.config(text=f"Output: {(int(value)*1.609).__round__(2)}: ", font=("Arial", 14, "italic"))
    print("I got clicked")


button = Button(text="Click me", command=button_clicked)
button.grid(column=2, row=3)
# Entry
input = Entry()
input.grid(column=2, row=2)
window.mainloop()
