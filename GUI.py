import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Inventory System for Blockbuster Video')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
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

# Customer Information label
tk.Label(customer, text="Customer Information").grid(row=0, column=0, columnspan=2, pady=5)

# List of customers
customer_list = tk.Listbox(customer, width=50, height=10)
customer_list.grid(row=1, column=0, padx=10, pady=5, rowspan=4)

# Buttons in customer frame
tk.Button(customer, text="Add Customer").grid(row=1, column=1, sticky="ew", padx=10, pady=5)
tk.Button(customer, text="Remove Customer").grid(row=2, column=1, sticky="ew", padx=10, pady=5)
tk.Button(customer, text="Edit Customer").grid(row=3, column=1, sticky="ew", padx=10, pady=5)
tk.Button(customer, text="Filter By").grid(row=4, column=1, sticky="ew", padx=10, pady=5)

# Video Information label
tk.Label(video, text="Video Information").grid(row=0, column=0, columnspan=2, pady=5)

#list of videos
video_list = tk.Listbox(video, width=50, height=10)
video_list.grid(row=1, column=0, padx=10, pady=5, rowspan=4)

#buttons in video frame
tk.Button(video, text="Add Video").grid(row=1, column=1, sticky="ew", padx=10, pady=5)
tk.Button(video, text="Remove Video").grid(row=2, column=1, sticky="ew", padx=10, pady=5)
tk.Button(video, text="Edit Video").grid(row=3, column=1, sticky="ew", padx=10, pady=5)
tk.Button(video, text="Filter By").grid(row=4, column=1, sticky="ew", padx=10, pady=5)

# Rental Information label
tk.Label(rental, text="Start a Rental").pack()

def on_scroll(*args):
    t1.yview(*args)
    t2.yview(*args)

# Return Information Label
tk.Label(returnn, text="Start a Return").pack()

def on_scroll(*args):
    t3.yview(*args)
    t4.yview(*args)

# list of customer name,....
t1 = tk.Listbox(rental, width=35, height=10).pack(side="left")
t1_scrollbar = tk.Scrollbar(rental, orient="vertical")
t1_scrollbar.pack(side="left", fill="y")

# list of video name, curent rental status
t2 = tk.Listbox(rental, width=35, height=10).pack(side="left")
t2_scrollbar = tk.Scrollbar(rental, orient="vertical")
t2_scrollbar.pack(side="left", fill="y")

t3 = tk.Listbox(returnn, width=35, height=10).pack(side="left")
t3_scrollbar = tk.Scrollbar(returnn, orient="vertical")
t3_scrollbar.pack(side="left", fill="y")

t4 = tk.Listbox(returnn, width=35, height=10).pack(side="left")
t4_scrollbar = tk.Scrollbar(returnn, orient="vertical")
t4_scrollbar.pack(side="left", fill="y")

tk.Button(rental, text="Rent Video").pack()
tk.Button(returnn, text="Return Video").pack()

root.mainloop()
