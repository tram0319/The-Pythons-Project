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
rental = ttk.Frame(notebook)
returnn = ttk.Frame(notebook)

customer.pack(fill='both', expand=True)
video.pack(fill='both', expand=True)
rental.pack(fill='both', expand=True)
returnn.pack(fill='both', expand=True)

# add frames to notebook
notebook.add(customer, text='Customer')
notebook.add(video, text='Video')
notebook.add(rental, text='Rental')
notebook.add(returnn, text='Return')

#Customer Information label
tk.Label(customer, text="Customer Information").pack()

#list of customers
tk.Listbox(customer, width=50, height=10).pack()

#button in customer frame
tk.Button(customer, text="Add Customer").pack()
tk.Button(customer, text="Remove Customer").pack()
tk.Button(customer, text="Edit Customer").pack()
tk.Button(customer, text="Filter By").pack()

# Video Information label
tk.Label(video, text="Video Information").pack()

#list of videos
tk.Listbox(video, width=50, height=10).pack()

#buttons in video frame
tk.Button(video, text="Add Video").pack()
tk.Button(video, text="Remove Video").pack()
tk.Button(video, text="Edit Video").pack()
tk.Button(video, text="Filter By").pack()

# Rental Information label
tk.Label(rental, text="Rental Information").pack()

def on_scroll(*args):
    t1.yview(*args)
    t2.yview(*args)
#list of customerId, customer name,
t1=tk.Listbox(rental, width=35, height=10).pack(side="left")
t1_scrollbar = tk.Scrollbar(rental, orient="vertical")
t1_scrollbar.pack(side="left", fill="y")

#list of videoid, name video, curent rental status
t2=tk.Listbox(rental, width=35, height=10).pack(side="left")
t2_scrollbar = tk.Scrollbar(rental, orient="vertical")
t2_scrollbar.pack(side="left", fill="y")


#button for Rental program
tk.Button(rental,text="Rent Video").pack(side="top")
tk.Button(rental,text="Return Video").pack(side="top")


root.mainloop()
