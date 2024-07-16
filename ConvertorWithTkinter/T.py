from tkinter import *

window = Tk()

label_from = Label(window, text="From")
label_from.grid(row=0, column=0, sticky=tk.w)
label_to = Label(window, text="To")
label_to.grid(row=0, column=1,sticky="e")

entry_from = Entry(window)
entry_from.grid(row=1, column=0)
entry_to = Entry(window)
entry_to.grid(row=1, column=1)

list_box_from = Listbox(window)
list_box_from.grid(row=2, column=0)
list_box_to = Listbox(window)
list_box_to.grid(row=2, column=1)

button = Button(window, text='Calculate')
button.grid(row=3, column=0, columnspan=2, sticky=)

window.mainloop()
