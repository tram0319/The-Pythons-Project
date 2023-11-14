import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
def add_customer():
    # Function to be executed when "Add Customer" button is clicked
    # Create a new Toplevel window for entering customer information
    add_window = tk.Toplevel(customer)
    add_window.title("Add Customer")

    # Add entry fields, labels, and other widgets for customer information
    tk.Label(add_window, text="Customer First Name:").grid(row=0, column=0, padx=10, pady=5)
    fName_entry = tk.Entry(add_window)
    fName_entry.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(add_window, text="Customer Last Name:").grid(row=1, column=0, padx=10, pady=5)
    lName_entry = tk.Entry(add_window)
    lName_entry.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(add_window, text="Customer Address:").grid(row=2, column=0, padx=10, pady=5)
    address_entry = tk.Entry(add_window)
    address_entry.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Label(add_window, text="Customer Phone:").grid(row=3, column=0, padx=10, pady=5)
    phone_entry = tk.Entry(add_window)
    phone_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Customer Email:").grid(row=4, column=0, padx=10, pady=5)
    email_entry = tk.Entry(add_window)
    email_entry.grid(row=4, column=1, padx=10, pady=5)
    
    
    def save_customer():
        first_name = fName_entry.get()
        last_name = lName_entry.get()
        customer_address = address_entry.get()
        customer_phone = phone_entry.get()
        customer_email = email_entry.get()
        
        customer_list.insert(tk.END, f"{first_name} {last_name} {customer_address} {customer_phone} {customer_email}")
        
        add_window.destroy()
    
    tk.Button(add_window, text="Save", command=save_customer).grid(row=5, column=0, columnspan=2, pady=10)

def remove_customer():
    # Function to be executed when "Remove Customer" button is clicked
    selected_index = customer_list.curselection()

    if not selected_index:
        messagebox.showwarning("No Customer Selected", "Please select a customer to remove.")
        return

    customer_name = customer_list.get(selected_index)
    confirmation = messagebox.askokcancel("Confirm Deletion", f"Do you want to remove the customer:\n{customer_name}")

    if confirmation:
        customer_list.delete(selected_index)

def edit_customer():
    # Functionality to be executed when "Edit Customer" button is clicked
    messagebox.showinfo("Edit Customer", "Edit Customer functionality to be implemented here")

def filter_by():
    # Functionality to be executed when "Filter By" button is clicked
    messagebox.showinfo("Filter By", "Filter By functionality to be implemented here")
    
tk.Button(customer, text="Add Customer", command=add_customer).grid(row=1, column=1, sticky="ew", padx=10, pady=5)
tk.Button(customer, text="Remove Customer", command=remove_customer).grid(row=2, column=1, sticky="ew", padx=10, pady=5)
tk.Button(customer, text="Edit Customer", command=edit_customer).grid(row=3, column=1, sticky="ew", padx=10, pady=5)
tk.Button(customer, text="Filter By", command=filter_by).grid(row=4, column=1, sticky="ew", padx=10, pady=5)

# Video Information label
tk.Label(video, text="Video Information").grid(row=0, column=0, columnspan=2, pady=5)

#list of videos
video_list = tk.Listbox(video, width=50, height=10)
video_list.grid(row=1, column=0, padx=10, pady=5, rowspan=4)

#buttons in video frame
# Buttons in customer frame
def add_video():
    # Function to be executed when "Add Video" button is clicked
    # Create a new Toplevel window for entering video information
    add_window = tk.Toplevel(video)
    add_window.title("Add Video")

    # Add entry fields, labels, and other widgets for customer information
    tk.Label(add_window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
    title_entry = tk.Entry(add_window)
    title_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Year:").grid(row=1, column=0, padx=10, pady=5)
    year_entry = tk.Entry(add_window)
    year_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Director:").grid(row=2, column=0, padx=10, pady=5)
    director_entry = tk.Entry(add_window)
    director_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Genre:").grid(row=3, column=0, padx=10, pady=5)
    genre_entry = tk.Entry(add_window)
    genre_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Rating:").grid(row=4, column=0, padx=10, pady=5)
    rating_entry = tk.Entry(add_window)
    rating_entry.grid(row=4, column=1, padx=10, pady=5)

    def save_video():
        title = title_entry.get()
        year = year_entry.get()
        director = director_entry.get()
        genre = genre_entry.get()
        rating = rating_entry.get()

        video_list.insert(tk.END, f"{title} {year} {director} {genre} {rating}")

        add_window.destroy()

    tk.Button(add_window, text="Save", command=save_video).grid(row=5, column=0, columnspan=2, pady=10)

def remove_video():
    # Function to be executed when "Remove Video" button is clicked
    selected_index = video_list.curselection()

    if not selected_index:
        messagebox.showwarning("No Video Selected", "Please select a video to remove.")
        return

    video_name = video_list.get(selected_index)
    confirmation = messagebox.askokcancel("Confirm Deletion", f"Do you want to remove the customer:\n{video_name}")

    if confirmation:
        video_list.delete(selected_index)

tk.Button(video, text="Add Video", command=add_video).grid(row=1, column=1, sticky="ew", padx=10, pady=5)
tk.Button(video, text="Remove Video", command=remove_video).grid(row=2, column=1, sticky="ew", padx=10, pady=5)
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
    
#list of customer name,....
t1=tk.Listbox(rental, width=35, height=10).pack(side="left")
t1_scrollbar = tk.Scrollbar(rental, orient="vertical")
t1_scrollbar.pack(side="left", fill="y")

#list of video name, curent rental status
t2=tk.Listbox(rental, width=35, height=10).pack(side="left")
t2_scrollbar = tk.Scrollbar(rental, orient="vertical")
t2_scrollbar.pack(side="left", fill="y")

t3=tk.Listbox(returnn, width=35, height=10).pack(side="left")
t3_scrollbar = tk.Scrollbar(returnn, orient="vertical")
t3_scrollbar.pack(side="left", fill="y")

t4=tk.Listbox(returnn, width=35, height=10).pack(side="left")
t4_scrollbar = tk.Scrollbar(returnn, orient="vertical")
t4_scrollbar.pack(side="left", fill="y")

tk.Button(rental, text="Rent Video").pack()
tk.Button(returnn, text="Return Video").pack()


root.mainloop()
