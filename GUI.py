import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Inventory System for Blockbuster Video')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create 2 frames
customer = ttk.Frame(notebook)
video = ttk.Frame(notebook)

customer.pack(fill='both', expand=True)
video.pack(fill='both', expand=True)

# add frames to notebook
notebook.add(customer, text='Customer')
notebook.add(video, text='Video')

#Customer Information label
tk.Label(customer, text="Customer Information").pack()

#list of customers
tk.Listbox(customer, width=50, height=10).pack()

#button in customer frame
tk.Button(customer, text="Add Customer").pack()
tk.Button(customer, text="Remove Customer").pack()
tk.Button(customer, text="Edit Customer").pack()
tk.Button(customer, text="Filter By").pack()

#button for Rental program
tk.Button(text="Rent Video").pack()
tk.Button(text="Return Video").pack()

# Video Information label
tk.Label(video, text="Video Information").pack()

#list of videos
tk.Listbox(video, width=50, height=10).pack()

#buttons in video frame
tk.Button(video, text="Add Video").pack()
tk.Button(video, text="Remove Video").pack()
tk.Button(video, text="Edit Video").pack()
tk.Button(video, text="Filter By").pack()


root.mainloop()
