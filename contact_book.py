#task 3
#contact book
import tkinter as tk
from tkinter import messagebox
import uuid

# In-memory dictionary to store contacts
contacts = {}

# --- Functions ---
def add_contact():
    store = store_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not store or not phone:
        messagebox.showwarning("Input Error", "Store Name and Phone Number are required.")
        return

    contact_id = str(uuid.uuid4())
    contacts[contact_id] = {
        "store": store,
        "phone": phone,
        "email": email,
        "address": address
    }

    clear_fields()
    display_contacts()
    messagebox.showinfo("Success", "Contact added successfully!")

def display_contacts():
    contact_list.delete(0, tk.END)
    for cid, data in contacts.items():
        contact_list.insert(tk.END, f"{data['store']} - {data['phone']}")

def load_selected_contact(event):
    selection = contact_list.curselection()
    if not selection:
        return
    value = contact_list.get(selection[0])
    for cid, data in contacts.items():
        if f"{data['store']} - {data['phone']}" == value:
            store_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            address_entry.delete(0, tk.END)

            store_entry.insert(0, data['store'])
            phone_entry.insert(0, data['phone'])
            email_entry.insert(0, data['email'])
            address_entry.insert(0, data['address'])
            return

def update_contact():
    selection = contact_list.curselection()
    if not selection:
        messagebox.showwarning("No selection", "Select a contact to update.")
        return

    value = contact_list.get(selection[0])
    for cid, data in contacts.items():
        if f"{data['store']} - {data['phone']}" == value:
            contacts[cid] = {
                "store": store_entry.get(),
                "phone": phone_entry.get(),
                "email": email_entry.get(),
                "address": address_entry.get()
            }
            display_contacts()
            messagebox.showinfo("Updated", "Contact updated successfully.")
            return

def delete_contact():
    selection = contact_list.curselection()
    if not selection:
        messagebox.showwarning("No selection", "Select a contact to delete.")
        return

    value = contact_list.get(selection[0])
    for cid, data in list(contacts.items()):
        if f"{data['store']} - {data['phone']}" == value:
            del contacts[cid]
            display_contacts()
            clear_fields()
            messagebox.showinfo("Deleted", "Contact deleted.")
            return

def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for cid, data in contacts.items():
        if query in data['store'].lower() or query in data['phone']:
            contact_list.insert(tk.END, f"{data['store']} - {data['phone']}")

def clear_fields():
    store_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("Contact Manager")
root.geometry("500x600")
root.config(bg="#f7f7f7")

tk.Label(root, text="📇 Contact Manager", font=("Arial", 18, "bold"), bg="#f7f7f7").pack(pady=10)

# Entry fields
form = tk.Frame(root, bg="#f7f7f7")
form.pack()

tk.Label(form, text="Store Name:", bg="#f7f7f7").grid(row=0, column=0, sticky='e')
store_entry = tk.Entry(form, width=30)
store_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(form, text="Phone:", bg="#f7f7f7").grid(row=1, column=0, sticky='e')
phone_entry = tk.Entry(form, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(form, text="Email:", bg="#f7f7f7").grid(row=2, column=0, sticky='e')
email_entry = tk.Entry(form, width=30)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(form, text="Address:", bg="#f7f7f7").grid(row=3, column=0, sticky='e')
address_entry = tk.Entry(form, width=30)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#f7f7f7")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Contact", width=15, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", width=15, command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", width=15, command=delete_contact).grid(row=0, column=2, padx=5)

# Search bar
search_frame = tk.Frame(root, bg="#f7f7f7")
search_frame.pack(pady=10)

search_entry = tk.Entry(search_frame, width=30)
search_entry.grid(row=0, column=0, padx=10)
tk.Button(search_frame, text="Search", command=search_contact).grid(row=0, column=1)

# Contact List
contact_list = tk.Listbox(root, width=50, height=12)
contact_list.pack(pady=10)
contact_list.bind("<<ListboxSelect>>", load_selected_contact)

# Run App
root.mainloop()
