import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

import Inventory_List_Class
import Customer_List_Class
import Video_Class
import Customer_Class

InventoryList = Inventory_List_Class.Inventory_List()
CustomerList = Customer_List_Class.Customer_List()

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
customer_list = tk.Listbox(customer, width=75, height=20)
customer_list.grid(row=1, column=0, padx=10, pady=5, rowspan=4)

# Original customer data (for filtering purposes)
original_customer_data = []

regex1 = r'^[1-9]\d{2}\d{3}\d{4}$'
def valid_phone(x):
    phone = x.get()
    if not phone:
        messagebox.showerror("Error", "Phone number cannot be empty")
        return False
    elif not(re.match(regex1, phone)):
        messagebox.showerror("Error", "Invalid phone number.")
        return False
    return True


regex = r"^\S+@\S+\.\S+$"
def valid_email(e):
    email = e.get()
    if not email:
        messagebox.showerror("Error", "Email cannot be empty")
        return False
    elif not (re.fullmatch(regex, email)):
        messagebox.showerror("Error", "Invalid email address.")
        return False
    elif not char_limit(email, 30):
        return False
    return True

def valid_address(addr):
    address = addr.get()
    if not address:
        messagebox.showerror("Error", "Address cannot be empty")
        return False
    elif not char_limit(address, 30):
        return False
    return True

def valid_fName(fn):
    fName = fn.get()
    if not fName:
        messagebox.showerror("Error", "First name cannot be empty")
        return False
    elif not fName.isalpha() or " " in fName:
        messagebox.showerror("Error", "Invalid first name.")
        return False
    elif not char_limit(fName, 20):
        return False
    return True


def valid_lName(ln):
    lName = ln.get()
    if not lName:
        messagebox.showerror("Error", "Last name cannot be empty")
        return False
    elif not lName.isalpha() or " " in lName:
        messagebox.showerror("Error", "Invalid last name.")
        return False
    elif not char_limit(lName, 20):
        return False
    return True
    
def valid_title(t):
    title=t.get()
    if not title:
        messagebox.showerror("Error", "Title cannot be empty")
        return False
    elif not char_limit(title, 30):
        return False
    return True

def valid_year(y):
    year = y.get()
    if not year:
        messagebox.showerror("Error", "Year cannot be empty")
        return False
    elif not re.match(r"^(19\d{2}|20\d{2})$", year):
        messagebox.showerror("Error", "Invalid year.")
        return False
    return True

def valid_director(d):
    director = d.get()
    if not director:
        messagebox.showerror("Error", "Director cannot be empty")
        return False
    elif not char_limit(director, 30):
        return False
    return True

def valid_genre(g):
    genre = g.get()
    if not genre:
        messagebox.showerror("Error", "Genre cannot be empty")
        return False
    elif not genre.isalpha() or " " in genre:
        messagebox.showerror("Error", "Invalid genre.")
        return False
    elif not char_limit(genre, 20):
        return False
    return True

def valid_rating(r):
    rating = r.get()
    valid_ratings = ["PG", "R", "PG-13", "G"]
    if not rating:
        messagebox.showerror("Error", "Rating cannot be empty")
        return False
    elif rating not in valid_ratings:
        messagebox.showerror("Error", "Invalid rating. Please enter G, PG, PG-13, or R.")
        return False
    return True

def char_limit(c, limit):
    if not len(c) <= limit:
        messagebox.showerror("Error", "Character limit reached")
        return False
    return True

def update_t1_with_customer_list():
    t1.delete(0, tk.END)  # Clear the current list in t1
    for item in customer_list.get(0, tk.END):
        t1.insert(tk.END, item)

def update_t2_with_video_list():
    t2.delete(0, tk.END)  # Clear the current list in t2
    for item in video_list.get(0, tk.END):
        t2.insert(tk.END, item)

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
        if valid_fName(fName_entry) and valid_lName(lName_entry) and valid_phone(phone_entry) and valid_email(email_entry) and valid_address(address_entry):
            first_name = fName_entry.get()
            last_name = lName_entry.get()
            customer_address = address_entry.get()
            customer_phone = phone_entry.get()
            customer_email = email_entry.get()
        
            customer_list.insert(tk.END, f"{first_name.capitalize()} - {last_name.capitalize()} - {customer_address} - {customer_phone} - {customer_email}")

            # Update the original_customer_data list
            original_customer_data.append(f"{first_name.capitalize()} - {last_name.capitalize()} - {customer_address} - {customer_phone} - {customer_email}")

            # Call the function to update t1 with the same data as customer_list
            update_t1_with_customer_list()
            
            add_window.destroy()
    tk.Button(add_window, text="Save", command=save_customer).grid(row=5, column=0, columnspan=2, pady=10)

def remove_customer():
    # Function to be executed when "Remove Customer" button is clicked
    selected_indices = customer_list.curselection()

    if not selected_indices:
        messagebox.showwarning("No Customer Selected", "Please select a customer to remove.")
        return

    selected_index = selected_indices[0]

    customer_name = customer_list.get(selected_index)
    first_name = customer_name.split()[0]
    confirmation = messagebox.askokcancel("Confirm Deletion", f"Do you want to remove the customer:\n{first_name}")

    if confirmation:
        customer_list.delete(selected_index)

        # Remove the customer from the original_customer_data list
        original_customer_data.pop(selected_index)

        update_t1_with_customer_list()

def edit_customer():
    # Function to be executed when "Edit Customer" button is clicked
    selected_indices = customer_list.curselection()

    if not selected_indices:
        messagebox.showwarning("No Customer Selected", "Please select a customer to remove.")
        return

    selected_index = selected_indices[0]

    customer_info = customer_list.get(selected_index)
    fName, lName, address, phone, email = parse_customer_info(customer_info)

    # Create a new Toplevel window for editing customer information
    edit_window = tk.Toplevel(customer)
    edit_window.title("Edit Customer")

    # Add entry fields, labels, and other widgets for customer information

    tk.Label(edit_window, text="Customer First Name:").grid(row=0, column=0, padx=10, pady=5)
    fName_entry = tk.Entry(edit_window, textvariable=tk.StringVar(value=fName))
    fName_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(edit_window, text="Customer Last Name:").grid(row=1, column=0, padx=10, pady=5)
    lName_entry = tk.Entry(edit_window, textvariable=tk.StringVar(value=lName))
    lName_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(edit_window, text="Customer Address:").grid(row=2, column=0, padx=10, pady=5)
    address_entry = tk.Entry(edit_window, textvariable=tk.StringVar(value=address))
    address_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(edit_window, text="Customer Phone:").grid(row=3, column=0, padx=10, pady=5)
    phone_entry = tk.Entry(edit_window, textvariable=tk.StringVar(value=phone))
    phone_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(edit_window, text="Customer Email:").grid(row=4, column=0, padx=10, pady=5)
    email_entry = tk.Entry(edit_window, textvariable=tk.StringVar(value=email))
    email_entry.grid(row=4, column=1, padx=10, pady=5)

    # Function to save edited customer information
    def save_edited_customer():
        # Get values from entry fields
        if valid_fName(fName_entry) and valid_lName(lName_entry) and valid_phone(phone_entry) and valid_email(email_entry) and valid_address(address_entry):
            edited_first_name = fName_entry.get()
            edited_last_name = lName_entry.get()
            edited_address = address_entry.get()
            edited_phone = phone_entry.get()
            edited_email = email_entry.get()

            # Perform any validation or processing needed

            # Update the customer_list with the edited customer information
            customer_list.delete(selected_index)
            customer_list.insert(tk.END, f"{edited_first_name.capitalize()} - {edited_last_name.capitalize()} - {edited_address} - {edited_phone} - {edited_email}")

            original_customer_data.pop(selected_index)
            original_customer_data.append( f"{edited_first_name.capitalize()} - {edited_last_name.capitalize()} - {edited_address} - {edited_phone} - {edited_email}")

            update_t1_with_customer_list()
            
            # Close the edit_window
            edit_window.destroy()

    # Button to save edited customer information
    tk.Button(edit_window, text="Save", command=save_edited_customer).grid(row=5, column=0, columnspan=2, pady=10)

def parse_customer_info(customer_info):
    # Helper function to parse customer information from the listbox entry
    parts = customer_info.split(" - ", 4)
    return parts[0], parts[1], parts[2], parts[3], parts[4] if len(parts) > 4 else ""

def filter_by():
    # Function to be executed when "Filter By" button is clicked
    # Create a new Toplevel window for entering the initial letter
    filter_window = tk.Toplevel(customer)
    filter_window.title("Filter By Initial Letter")

    # Add entry field and label for the initial letter
    tk.Label(filter_window, text="Filter by Initial Letter:").grid(row=0, column=0, padx=10, pady=5)
    filter_entry = tk.Entry(filter_window, width=5)
    filter_entry.grid(row=0, column=1, padx=10, pady=5)

    # Function to apply the filter
    def apply_filter():
        initial_letter = filter_entry.get().strip().lower()
        customer_list.delete(0, tk.END)  # Clear the current listbox

        # Iterate through the original customer data and add matching customers to the listbox
        for original_customer_info in original_customer_data:
            original_fName, _, _, _, _, = parse_customer_info(original_customer_info)
            if original_fName.lower().startswith(initial_letter):
                customer_list.insert(tk.END, original_customer_info)

        # Close the filter_window
        filter_window.destroy()

    # Button to apply the filter
    tk.Button(filter_window, text="Apply Filter", command=apply_filter).grid(row=1, column=0, columnspan=2, pady=10)

tk.Button(customer, text="Add Customer", command=add_customer).grid(row=1, column=1, sticky="ew", padx=10, pady=5)
tk.Button(customer, text="Remove Customer", command=remove_customer).grid(row=2, column=1, sticky="ew", padx=10, pady=5)
tk.Button(customer, text="Edit Customer", command=edit_customer).grid(row=3, column=1, sticky="ew", padx=10, pady=5)
tk.Button(customer, text="Filter By", command=filter_by).grid(row=4, column=1, sticky="ew", padx=10, pady=5)

# Video Information label
tk.Label(video, text="Video Information").grid(row=0, column=0, columnspan=2, pady=5)

#list of videos
video_list = tk.Listbox(video, width=75, height=20)
video_list.grid(row=1, column=0, padx=10, pady=5, rowspan=4)

# Original video data (for filtering purposes)
original_video_data = []

#buttons in video frame
# Buttons in video frame
def add_video():
    # Function to be executed when "Add Video" button is clicked
    # Create a new Toplevel window for entering video information
    add_window = tk.Toplevel(video)
    add_window.title("Add Video")

    # Add entry fields, labels, and other widgets for customer information
    tk.Label(add_window, text="Title:").grid(row=0, column=0, padx=10, pady=5)
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
        if valid_title(title_entry) and valid_year(year_entry) and valid_director(director_entry) and valid_genre(genre_entry) and valid_rating(rating_entry):
            title = title_entry.get()
            year = year_entry.get()
            director = director_entry.get()
            genre = genre_entry.get()
            rating = rating_entry.get()

            video_list.insert(tk.END, f"{title} - {year} - {director} - {genre} - {rating}")
            InventoryList.add_video(title, year, director, rating, genre, "Available")

            # Update the original_video_data list
            original_video_data.append(f"{title} - {year} - {director} - {genre} - {rating}")

            update_t2_with_video_list()
        
            add_window.destroy()

    tk.Button(add_window, text="Save", command=save_video).grid(row=5, column=0, columnspan=2, pady=10)

def remove_video():
    # Function to be executed when "Remove Customer" button is clicked
    selected_indices = video_list.curselection()

    if not selected_indices:
        messagebox.showwarning("No Video Selected", "Please select a video to remove.")
        return

    selected_index = selected_indices[0]

    video_name = video_list.get(selected_index)
    video_title = video_name.split()[0]
    confirmation = messagebox.askokcancel("Confirm Deletion", f"Do you want to remove the video:\n{video_title}")

    if confirmation:
        InventoryList.remove_video(video_title)
        video_list.delete(selected_index)

        # Remove the video from the original_video_data list
        original_video_data.pop(selected_index)

        update_t2_with_video_list()

def edit_video():
    # Function to be executed when "Edit Video" button is clicked
    selected_indices = video_list.curselection()

    if not selected_indices:
        messagebox.showwarning("No Video Selected", "Please select a video to remove.")
        return

    selected_index = selected_indices[0]

    video_info = video_list.get(selected_index)
    title, year, director, genre, rating = parse_video_info(video_info)

    # Create a new Toplevel window for editing video information
    edit_window = tk.Toplevel(video)
    edit_window.title("Edit Video")

    # Add entry fields, labels, and other widgets for video information

    tk.Label(edit_window, text="Title:").grid(row=0, column=0, padx=10, pady=5)
    title_entry = tk.Entry(edit_window, textvariable=tk.StringVar(value=title))
    title_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(edit_window, text="Year:").grid(row=1, column=0, padx=10, pady=5)
    year_entry = tk.Entry(edit_window, textvariable=tk.StringVar(value=year))
    year_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(edit_window, text="Director:").grid(row=2, column=0, padx=10, pady=5)
    director_entry = tk.Entry(edit_window, textvariable=tk.StringVar(value=director))
    director_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(edit_window, text="Genre:").grid(row=3, column=0, padx=10, pady=5)
    genre_entry = tk.Entry(edit_window, textvariable=tk.StringVar(value=genre))
    genre_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(edit_window, text="Rating:").grid(row=4, column=0, padx=10, pady=5)
    rating_entry = tk.Entry(edit_window, textvariable=tk.StringVar(value=rating))
    rating_entry.grid(row=4, column=1, padx=10, pady=5)

    # Function to save edited video information
    def save_edited_video():
        if valid_title(title_entry) and valid_year(year_entry) and valid_director(director_entry) and valid_genre(genre_entry) and valid_rating(rating_entry):
            edited_title = title_entry.get()
            edited_year = year_entry.get()
            edited_director = director_entry.get()
            edited_genre = genre_entry.get()
            edited_rating = rating_entry.get()

            # Update the video_list with the edited video information
            video_info = video_list.get(selected_index)
            video_title = video_info.split()[0]
            InventoryList.remove_video(video_title)
            video_list.delete(selected_index)
        
            video_list.insert(tk.END, f"{edited_title} - {edited_year} - {edited_director} - {edited_genre} - {edited_rating}")
            InventoryList.add_video(edited_title, edited_year, edited_director, edited_rating, edited_genre, "Available")

            original_video_data.pop(selected_index)
            original_video_data.append( f"{edited_title} - {edited_year} - {edited_director} - {edited_genre} - {edited_rating}")

            update_t2_with_video_list()
        
            # Close the edit_window
            edit_window.destroy()

    # Button to save edited video information
    tk.Button(edit_window, text="Save", command=save_edited_video).grid(row=5, column=0, columnspan=2, pady=10)

def parse_video_info(video_info):
    # Helper function to parse video information from the listbox entry
    parts = video_info.split(" - ", 4)
    return parts[0], parts[1], parts[2], parts[3], parts[4] if len(parts) > 4 else ""

def vFilter_by():
    # Function to be executed when "Filter By" button is clicked
    # Create a new Toplevel window for entering the initial letter
    filter_window = tk.Toplevel(video)
    filter_window.title("Filter By Initial Letter")

    # Add entry field and label for the initial letter
    tk.Label(filter_window, text="Filter by Initial Letter:").grid(row=0, column=0, padx=10, pady=5)
    filter_entry = tk.Entry(filter_window, width=5)
    filter_entry.grid(row=0, column=1, padx=10, pady=5)

    # Function to apply the filter
    def apply_filter():
        initial_letter = filter_entry.get().strip().lower()
        video_list.delete(0, tk.END)  # Clear the current listbox

        # Iterate through the original video data and add matching videos to the listbox
        for original_video_info in original_video_data:
            original_title, _, _, _, _, = parse_video_info(original_video_info)
            if original_title.lower().startswith(initial_letter):
                video_list.insert(tk.END, original_video_info)

        # Close the filter_window
        filter_window.destroy()

    # Button to apply the filter
    tk.Button(filter_window, text="Apply Filter", command=apply_filter).grid(row=1, column=0, columnspan=2, pady=10)

tk.Button(video, text="Add Video", command=add_video).grid(row=1, column=1, sticky="ew", padx=10, pady=5)
tk.Button(video, text="Remove Video", command=remove_video).grid(row=2, column=1, sticky="ew", padx=10, pady=5)
tk.Button(video, text="Edit Video", command=edit_video).grid(row=3, column=1, sticky="ew", padx=10, pady=5)
tk.Button(video, text="Filter By", command=vFilter_by).grid(row=4, column=1, sticky="ew", padx=10, pady=5)

# Rental Information label
tk.Label(rental, text="Start a Rental").pack()

def on_scroll(*args):
    t1.yview(*args)
    t2.yview(*args)
    
# Return Information Label
tk.Label(returnn, text="Start a Return").pack()

def on_scroll2(*args):
    t3.yview(*args)
    t4.yview(*args)
    
#list of customer name,....
t1 = tk.Listbox(rental, width=35, height=20, exportselection=False)
t1.pack(side="left")
t1_scrollbar = tk.Scrollbar(rental, orient="vertical", command=t1.yview)
t1_scrollbar.pack(side="left", fill="y")
t1.config(yscrollcommand=t1_scrollbar.set)

#list of video name, curent rental status
t2=tk.Listbox(rental, width=35, height=20, exportselection=False)
t2.pack(side="left")
t2_scrollbar = tk.Scrollbar(rental, orient="vertical", command=t2.yview)
t2_scrollbar.pack(side="left", fill="y")
t2.config(yscrollcommand=t2_scrollbar.set)

t3=tk.Listbox(returnn, width=35, height=10).pack(side="left")
t3_scrollbar = tk.Scrollbar(returnn, orient="vertical")
t3_scrollbar.pack(side="left", fill="y")

t4=tk.Listbox(returnn, width=35, height=10).pack(side="left")
t4_scrollbar = tk.Scrollbar(returnn, orient="vertical")
t4_scrollbar.pack(side="left", fill="y")

def rent_video():
    selected_customer_index = t1.curselection()
    selected_video_index = t2.curselection()

    if not selected_customer_index or not selected_video_index:
        messagebox.showwarning("Selection Required", "Please select a customer and a video to rent.")
        return
    customer_selected = t1.get(selected_customer_index[0])
    video_selected = t2.get(selected_video_index[0])

    customer_name, _, _, _, _= customer_selected.split(" - ")
    video_name, _, _, _, _, = video_selected.split(" - ")

    messagebox.showinfo("Rental Processed", f"Rented '{video_name}' to {customer_name}")

tk.Button(rental, text="Rent Video", command=rent_video).pack()
tk.Button(returnn, text="Return Video").pack()


root.mainloop()
