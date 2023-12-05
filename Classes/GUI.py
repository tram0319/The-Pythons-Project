import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
import json

import Inventory_List_Class
import Customer_List_Class
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
    elif not director.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Invalid director.")
    elif not char_limit(director, 30):
        return False
    return True

def valid_genre(g):
    genre = g.get()
    if not genre:
        messagebox.showerror("Error", "Genre cannot be empty")
        return False
    elif not char_limit(genre, 20):
        return False
    return True

def valid_rating(r):
    rating = r.get()
    valid_ratings = ["PG", "R", "PG-13", "G", "UNRATED"]
    if not rating:
        messagebox.showerror("Error", "Rating cannot be empty")
        return False
    elif rating.upper() not in valid_ratings:
        messagebox.showerror("Error", "Invalid rating. Please enter G, PG, PG-13, R, or Unrated")
        return False
    return True

def char_limit(c, limit):
    if not len(c) <= limit:
        messagebox.showerror("Error", "Character limit reached")
        return False
    return True

def isDuplicateCustomer(email):
    list = CustomerList.get_cust_list()
    if len(list) > 0:
        i = 0
        while i != len(list):
            if list[i].email == email:
                messagebox.showerror("Error", "Customer already exists")
                return True
            i += 1
        return False 
    return False

def isDuplicateVideo(title, year):
    inv = InventoryList.get_inventory()
    if len(inv) > 0:
        i = 0
        while i != len(inv):
            if inv[i].name == title and inv[i].year == year:
                messagebox.showerror("Error", "Video already exists")
                return True
            i += 1
        return False 
    return False

def update_t1_with_customer_list():
    t1.delete(0, tk.END)  # Clear the current list in t1
    for item in customer_list.get(0, tk.END):
        t1.insert(tk.END, item)

def update_t2_with_video_list():
    t2.delete(0, tk.END)  # Clear the current list in t2
    for item in video_list.get(0, tk.END):
        t2.insert(tk.END, item)

def update_t3_with_customer_list():
    t3.delete(0, tk.END)  # Clear the current list in t3
    for item in customer_list.get(0, tk.END):
        t3.insert(tk.END, item)
        
def update_t4_with_video_list():
    t4.delete(0, tk.END)  # Clear the current list in t4
    for item in video_list.get(0, tk.END):
        t4.insert(tk.END, item)

# Buttons in customer frame
def add_customer():
    # Function to be executed when "Add Customer" button is clicked
    # Create a new Toplevel window for entering customer information
    add_window = tk.Toplevel(customer)
    add_window.title("Add Customer")
    add_window.attributes('-topmost', True)

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
        if valid_fName(fName_entry) and valid_lName(lName_entry) and valid_phone(phone_entry) and valid_email(email_entry) and valid_address(address_entry) and not isDuplicateCustomer(email_entry.get()):
            first_name = fName_entry.get()
            last_name = lName_entry.get()
            customer_address = address_entry.get()
            customer_phone = phone_entry.get()
            customer_email = email_entry.get()
        
            customer_list.insert(tk.END, f"{first_name.capitalize()} - {last_name.capitalize()} - {customer_address} - {customer_phone} - {customer_email}")

            # Update the original_customer_data list
            original_customer_data.append(f"{first_name.capitalize()} - {last_name.capitalize()} - {customer_address} - {customer_phone} - {customer_email}")

            #Add customer to list class object
            CustomerList.add_cust(first_name, last_name, customer_address, customer_phone, customer_email)
            
            # Call the function to update t1 with the same data as customer_list
            update_t1_with_customer_list()
            update_t3_with_customer_list()
            
            add_window.destroy()
    tk.Button(add_window, text="Save", command=save_customer).grid(row=5, column=0, columnspan=2, pady=10)

def remove_customer():
    # Function to be executed when "Remove Customer" button is clicked
    selected_indices = customer_list.curselection()

    if not selected_indices:
        messagebox.showwarning("No Customer Selected", "Please select a customer to remove.")
        return

    selected_index = selected_indices[0]

    customer_info = customer_list.get(selected_index)
    first_name = customer_info.split()[0]
    last_name = customer_info.split()[2]
    print(last_name)
    confirmation = messagebox.askokcancel("Confirm Deletion", f"Do you want to remove the customer:\n{first_name} {last_name}")

    # Remove the customer from the original_customer_data list
    if confirmation:
        index = 0
        for i in original_customer_data:
            if i == customer_info:
                original_customer_data.pop(index)
                break
            index += 1
        
        CustomerList.remove_cust(first_name, last_name)
        
        customer_list.delete(selected_index)
    
        update_t1_with_customer_list()
        update_t3_with_customer_list()

def edit_customer():
    # Function to be executed when "Edit Customer" button is clicked
    selected_indices = customer_list.curselection()

    if not selected_indices:
        messagebox.showwarning("No Customer Selected", "Please select a customer to edit.")
        return

    selected_index = selected_indices[0]

    customer_info = customer_list.get(selected_index)
    fName, lName, address, phone, email = parse_customer_info(customer_info)

    # Create a new Toplevel window for editing customer information
    edit_window = tk.Toplevel(customer)
    edit_window.title("Edit Customer")
    edit_window.attributes('-topmost', True)

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
        if valid_fName(fName_entry) and valid_lName(lName_entry) and valid_phone(phone_entry) and valid_email(email_entry) and valid_address(address_entry) and not isDuplicateCustomer(email_entry.get()):
            edited_first_name = fName_entry.get()
            edited_last_name = lName_entry.get()
            edited_address = address_entry.get()
            edited_phone = phone_entry.get()
            edited_email = email_entry.get()

            # Update the customer_list with the edited customer information
            index = 0
            for i in original_customer_data:
                if i == customer_info:    
                    original_customer_data.pop(index)
                    original_customer_data.append( f"{edited_first_name.capitalize()} - {edited_last_name.capitalize()} - {edited_address} - {edited_phone} - {edited_email}")
                    break
                index += 1
                
            CustomerList.edit_cust_info(fName, lName, edited_first_name, edited_last_name, edited_address, edited_phone, edited_email)
            
            customer_list.delete(selected_index)
            customer_list.insert(tk.END, f"{edited_first_name.capitalize()} - {edited_last_name.capitalize()} - {edited_address} - {edited_phone} - {edited_email}")

            update_t1_with_customer_list()
            update_t3_with_customer_list()
            
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
    # Create a new Toplevel window for selecting the filter option
    filter_window = tk.Toplevel(customer)
    filter_window.title("Filter Customers")
    filter_window.attributes('-topmost', True)

    # Add a dropdown menu for selecting the filter option
    filter_var = tk.StringVar()
    filter_var.set("First Name")  # Set the default filter option
    filter_label = tk.Label(filter_window, text="Select Filter Option:")
    filter_label.grid(row=0, column=0, padx=10, pady=5)

    filter_options = ["First Name", "Last Name"]
    filter_dropdown = ttk.Combobox(filter_window, values=filter_options, textvariable=filter_var)
    filter_dropdown.grid(row=0, column=1, padx=10, pady=5)

    # Add entry fields for the filter criteria
    tk.Label(filter_window, text="Filter Value:").grid(row=1, column=0, padx=10, pady=5)
    filter_value_entry = tk.Entry(filter_window)
    filter_value_entry.grid(row=1, column=1, padx=10, pady=5)

    # Function to apply the filter
    def apply_filter():
        filter_option = filter_var.get()
        filter_value = filter_value_entry.get().strip().lower()

        customer_list.delete(0, tk.END)  # Clear the current listbox

        # Iterate through the original customer data and add matching customers to the listbox
        for original_customer_info in original_customer_data:
            original_fName, original_lName, _, _, _ = parse_customer_info(original_customer_info)
            if (
                (filter_option == "First Name" and filter_value in original_fName.lower())
                or (filter_option == "Last Name" and filter_value in original_lName.lower())
            ):
                customer_list.insert(tk.END, original_customer_info)

        # Close the filter_window
        filter_window.destroy()

    # Button to apply the filter
    tk.Button(filter_window, text="Apply Filter", command=apply_filter).grid(row=2, column=0, columnspan=2, pady=10)


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
def add_video():
    # Function to be executed when "Add Video" button is clicked
    # Create a new Toplevel window for entering video information
    add_window = tk.Toplevel(video)
    add_window.title("Add Video")
    add_window.attributes('-topmost', True)

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
        if valid_title(title_entry) and valid_year(year_entry) and valid_director(director_entry) and valid_genre(genre_entry) and valid_rating(rating_entry) and not isDuplicateVideo(title_entry.get(), year_entry.get()):
            title = title_entry.get()
            year = year_entry.get()
            director = director_entry.get()
            genre = genre_entry.get()
            rating = rating_entry.get().upper()
            availability = "Available"

            video_list.insert(tk.END, f"{title} - {year} - {director} - {genre} - {rating} - {availability}")
            InventoryList.add_video(title, year, director, rating, genre, availability)

            # Update the original_video_data list
            original_video_data.append(f"{title} - {year} - {director} - {genre} - {rating} - {availability}")

            update_t2_with_video_list()
            update_t4_with_video_list()
        
            add_window.destroy()

    tk.Button(add_window, text="Save", command=save_video).grid(row=5, column=0, columnspan=2, pady=10)

def remove_video():
    # Function to be executed when "Remove Customer" button is clicked
    selected_indices = video_list.curselection()

    if not selected_indices:
        messagebox.showwarning("No Video Selected", "Please select a video to remove.")
        return

    selected_index = selected_indices[0]

    video_info = video_list.get(selected_index)
    video_title = video_info.split()[0]
    confirmation = messagebox.askokcancel("Confirm Deletion", f"Do you want to remove the video:\n{video_title}")

    if confirmation:
        index = 0
        for i in original_video_data:
            if i == video_info:
                original_video_data.pop(index)
                break
            index += 1

        InventoryList.remove_video(video_title)
        video_list.delete(selected_index)

        update_t2_with_video_list()
        update_t4_with_video_list()

def edit_video():
    # Function to be executed when "Edit Video" button is clicked
    selected_indices = video_list.curselection()

    if not selected_indices:
        messagebox.showwarning("No Video Selected", "Please select a video to edit.")
        return

    selected_index = selected_indices[0]

    video_info = video_list.get(selected_index)
    title, year, director, genre, rating, availability = parse_video_info(video_info)

    # Create a new Toplevel window for editing video information
    edit_window = tk.Toplevel(video)
    edit_window.title("Edit Video")
    edit_window.attributes('-topmost', True)

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
        if valid_title(title_entry) and valid_year(year_entry) and valid_director(director_entry) and valid_genre(genre_entry) and valid_rating(rating_entry) and not isDuplicateVideo(title_entry.get(), year_entry.get()):
            edited_title = title_entry.get()
            edited_year = year_entry.get()
            edited_director = director_entry.get()
            edited_genre = genre_entry.get()
            edited_rating = rating_entry.get().upper()
            availability = "Available"

            # Update the video_list with the edited video information
            video_title = video_info.split()[0]

            # Removes video from original_video_data, works when the list is filtered
            index = 0
            for i in original_video_data:
                if i == video_info:
                    original_video_data.pop(index)
                    original_video_data.append( f"{edited_title} - {edited_year} - {edited_director} - {edited_genre} - {edited_rating} - {availability}")
                    break
                index += 1

            InventoryList.remove_video(video_title)
            video_list.delete(selected_index)
        
            video_list.insert(tk.END, f"{edited_title} - {edited_year} - {edited_director} - {edited_genre} - {edited_rating} - {availability}")

            InventoryList.add_video(title, year, director, rating, genre, availability)

            update_t2_with_video_list()
            update_t4_with_video_list()
        
            # Close the edit_window
            edit_window.destroy()

    # Button to save edited video information
    tk.Button(edit_window, text="Save", command=save_edited_video).grid(row=5, column=0, columnspan=2, pady=10)

def parse_video_info(video_info):
    # Helper function to parse video information from the listbox entry
    parts = video_info.split(" - ", 5)
    return parts[0], parts[1], parts[2], parts[3], parts[4], parts[5] if len(parts) > 5 else ""

def vFilter_by():
    filter_window = tk.Toplevel(video)
    filter_window.title("Filter Videos")

    filter_options = ["Title", "Year", "Director", "Genre", "Rating"]
    filter_var = tk.StringVar(value=filter_options[0])
    tk.Label(filter_window, text="Select Filter Option:").grid(row=0, column=0, padx=10, pady=5)
    filter_dropdown = ttk.Combobox(filter_window, values=filter_options, textvariable=filter_var)
    filter_dropdown.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(filter_window, text="Filter Value:").grid(row=1, column=0, padx=10, pady=5)
    filter_value_entry = tk.Entry(filter_window)
    filter_value_entry.grid(row=1, column=1, padx=10, pady=5)

        # Function to apply the filter
    def vapply_filter():
        filter_option = filter_var.get()
        filter_value = filter_value_entry.get().strip().lower()

        video_list.delete(0, tk.END)  # Clear the current listbox

            # Iterate through the original video data and add matching videos to the listbox
        for original_video_info in original_video_data:
            if filter_option == "Title":
                title, _, _, _, _, _ = parse_video_info(original_video_info)
                if filter_value.lower() in title.lower():
                    video_list.insert(tk.END, original_video_info)
            elif filter_option == "Year":
                _, year, _, _, _, _ = parse_video_info(original_video_info)
                if filter_value in year:
                    video_list.insert(tk.END, original_video_info)
            elif filter_option == "Director":
                _, _, director, _, _, _ = parse_video_info(original_video_info)
                if filter_value.lower() in director.lower():
                    video_list.insert(tk.END, original_video_info)
            elif filter_option == "Genre":
                _, _, _, genre, _, _ = parse_video_info(original_video_info)
                if filter_value.lower() in genre.lower():
                    video_list.insert(tk.END, original_video_info)
            elif filter_option == "Rating":
                _, _, _, _, rating, _ = parse_video_info(original_video_info)
                if filter_value.lower() in rating.lower():
                    video_list.insert(tk.END, original_video_info)

        # Close the filter_window
        filter_window.destroy()

    # Button to apply the filter
    tk.Button(filter_window, text="Apply Filter", command=vapply_filter).grid(row=2, column=0, columnspan=2, pady=10)


tk.Button(video, text="Add Video", command=add_video).grid(row=1, column=1, sticky="ew", padx=10, pady=5)
tk.Button(video, text="Remove Video", command=remove_video).grid(row=2, column=1, sticky="ew", padx=10, pady=5)
tk.Button(video, text="Edit Video", command=edit_video).grid(row=3, column=1, sticky="ew", padx=10, pady=5)
tk.Button(video, text="Filter By", command=vFilter_by).grid(row=4, column=1, sticky="ew", padx=10, pady=5)

# Rental Information label
tk.Label(rental, text="Start a Rental").pack()

def on_scroll(*args):
    t1.yview(*args)
    t2.yview(*args)
    t3.yview(*args)
    t4.yview(*args)
    
#list of customer name,....
t1 = tk.Listbox(rental, width=50, height=20, exportselection=False)
t1.pack(side="left")
t1_scrollbar = tk.Scrollbar(rental, orient="vertical", command=t1.yview)
t1_scrollbar.pack(side="left", fill="y")
t1.config(yscrollcommand=t1_scrollbar.set)

#list of video name, curent rental status
t2=tk.Listbox(rental, width=50, height=20, exportselection=False)
t2.pack(side="left")
t2_scrollbar = tk.Scrollbar(rental, orient="vertical", command=t2.yview)
t2_scrollbar.pack(side="left", fill="y")
t2.config(yscrollcommand=t2_scrollbar.set)

t3=tk.Listbox(returnn, width=50, height=20, exportselection=False)
t3.pack(side="left")
t3_scrollbar = tk.Scrollbar(returnn, orient="vertical", command=t3.yview)
t3_scrollbar.pack(side="left", fill="y")
t3.config(yscrollcommand=t3_scrollbar.set)

t4=tk.Listbox(returnn, width=50, height=20, exportselection=False)
t4.pack(side="left")
t4_scrollbar = tk.Scrollbar(returnn, orient="vertical", command=t4.yview)
t4_scrollbar.pack(side="left", fill="y")
t4.config(yscrollcommand=t4_scrollbar.set)

def rent_video():
    selected_customer_index = t1.curselection()
    selected_video_index = t2.curselection()

    if not selected_customer_index or not selected_video_index:
        messagebox.showwarning("Selection Required", "Please select a customer and a video to rent.")
        return
    customer_selected = t1.get(selected_customer_index[0])
    video_selected = t2.get(selected_video_index[0])

    customer_parts = customer_selected.split(" - ")
    video_parts = video_selected.split(" - ")
    customer_name = f"{customer_parts[0]} - {customer_parts[1]}"
    video_name = video_parts[0]
    messagebox.showinfo("Rental Processed", f"Rented '{video_name}' to {customer_name}")
    
def return_video():
    selected_customer_index = t3.curselection()
    selected_video_index = t4.curselection()

    if not selected_customer_index or not selected_video_index:
        messagebox.showwarning("Selection Required", "Please select a customer and a video to return.")
        return
    customer_selected = t3.get(selected_customer_index[0])
    video_selected = t4.get(selected_video_index[0])

    customer_parts = customer_selected.split(" - ")
    video_parts = video_selected.split(" - ")
    customer_name = f"{customer_parts[0]} {customer_parts[1]}"
    video_name = video_parts[0]
    messagebox.showinfo("Return Processed", f"{customer_name} returned {video_name}")

def read_cust_list():
    with open("customer.json", "r") as f:
        # Load the JSON data from the file
        data = json.load(f)
        #Gather variables from each item in the JSON data
        for item in data:
            first = item['firstName']
            last = item['lastName']
            address = item['address']
            phone = item['phoneNumber']
            email = item['email'],
            
            #Display Customer List on the window
            customer_list.insert(tk.END, f"{first.capitalize()} - {last.capitalize()} - {address} - {phone} - {email}")

            #Add customer list to original customer data
            original_customer_data.append(f"{first.capitalize()} - {last.capitalize()} - {address} - {phone} - {email}")

        #Update the customer list on the rental/return tabs
        update_t1_with_customer_list()
        update_t3_with_customer_list()
    
def write_cust_list():
    with open("customer.json", "w") as f:
        # Convert the object to a JSON serializable format
        serializable_list = [video.__dict__ for video in CustomerList.cust_list]
        # Write the JSON serializable object to the file
        json.dump(serializable_list, f)

def read_inventory():
    with open("inventory.json", "r") as f:
        # Load the JSON data from the file
        data = json.load(f)
        #Gather variables from each item in the JSON data
        for item in data:
            title = item['name']
            year = item['year']
            director = item['director']
            genre = item['genre']
            rating = item['rating']
            
            #Display inventory on the window
            video_list.insert(tk.END, f"{title} - {year} - {director} - {genre} - {rating}")
    
            #Add inventory to original video data
            original_video_data.append(f"{title} - {year} - {director} - {genre} - {rating}")
        
        #Update video list on rental/return tabs
        update_t2_with_video_list()
        update_t4_with_video_list()

def write_inventory():
    with open("inventory.json", "w") as f:
        # Convert the object to a JSON serializable format
        serializable_list = [video.__dict__ for video in InventoryList.inventory_list]
        # Write the JSON serializable object to the file
        json.dump(serializable_list, f)

#Saves the data from each list to their respective json file
def save_data_lists():
        write_cust_list()
        write_inventory()
        root.destroy()
    

tk.Button(rental, text="Rent Video", command=rent_video).pack()
tk.Button(returnn, text="Return Video", command=return_video).pack()

#Reads the date from the json files and loads them to the window
read_inventory()
read_cust_list()

#Saves the lists when the program closes
root.protocol("WM_DELETE_WINDOW", save_data_lists)

root.mainloop()

