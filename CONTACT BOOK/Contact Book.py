import json
import csv
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog


CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from JSON file or return an empty dictionary."""
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts():
    """Save contacts to JSON file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    """Prompt user to add a new contact."""
    name = simpledialog.askstring("Add Contact", "Enter Contact Name:")
    if not name:
        return
    
    phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
    if not phone:
        messagebox.showwarning("Input Error", "Phone number is required!")
        return

    email = simpledialog.askstring("Add Contact", "Enter Email Address (Optional):") or "N/A"
    address = simpledialog.askstring("Add Contact", "Enter Address (Optional):") or "N/A"

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    save_contacts()
    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
    view_contacts()

def view_contacts():
    """Display all saved contacts in the list."""
    contact_list.delete(0, tk.END)
    sorted_contacts = dict(sorted(contacts.items()))
    
    if not sorted_contacts:
        contact_list.insert(tk.END, "No contacts found.")
    else:
        for name, info in sorted_contacts.items():
            contact_list.insert(tk.END, f"{name} - {info['Phone']}")

def search_contact():
    """Search for a contact by name or phone number."""
    query = simpledialog.askstring("Search Contact", "Enter Name or Phone:")
    if not query:
        return
    
    contact_list.delete(0, tk.END)
    results = {name: info for name, info in contacts.items() if query.lower() in name.lower() or query in info["Phone"]}

    if not results:
        contact_list.insert(tk.END, "No matching contacts found.")
    else:
        for name, info in results.items():
            contact_list.insert(tk.END, f"{name} - {info['Phone']}")

def update_contact():
    """Allow user to update an existing contact's details."""
    name = simpledialog.askstring("Update Contact", "Enter Contact Name:")
    if name not in contacts:
        messagebox.showwarning("Not Found", f"Contact '{name}' not found.")
        return

    phone = simpledialog.askstring("Update Contact", "Enter New Phone:", initialvalue=contacts[name]["Phone"])
    email = simpledialog.askstring("Update Contact", "Enter New Email:", initialvalue=contacts[name]["Email"])
    address = simpledialog.askstring("Update Contact", "Enter New Address:", initialvalue=contacts[name]["Address"])

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    save_contacts()
    messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
    view_contacts()

def delete_contact():
    """Allow user to delete a contact."""
    name = simpledialog.askstring("Delete Contact", "Enter Contact Name:")
    if name in contacts:
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{name}'?"):
            del contacts[name]
            save_contacts()
            messagebox.showinfo("Success", f"Contact '{name}' deleted.")
            view_contacts()
    else:
        messagebox.showwarning("Not Found", f"Contact '{name}' not found.")

def export_to_csv():
    """Export contacts to a CSV file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if file_path:
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email", "Address"])
            for name, info in contacts.items():
                writer.writerow([name, info["Phone"], info["Email"], info["Address"]])
        messagebox.showinfo("Export Successful", "Contacts exported successfully!")

def import_from_csv():
    """Import contacts from a CSV file."""
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) == 4:
                    name, phone, email, address = row
                    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts()
        messagebox.showinfo("Import Successful", "Contacts imported successfully!")
        view_contacts()


contacts = load_contacts()


root = tk.Tk()
root.title("Contact Book")
root.geometry("420x550")
root.configure(bg="#2C2F33")  # Dark Mode


tk.Label(root, text="📞 Contact Book", font=("Arial", 16, "bold"), bg="#2C2F33", fg="white").pack(pady=10)

# Contact List
contact_list = tk.Listbox(root, width=50, height=15, bg="#23272A", fg="white")
contact_list.pack(pady=10)
view_contacts()


btn_frame = tk.Frame(root, bg="#2C2F33")
btn_frame.pack(pady=10)


button_data = [
    ("➕ Add Contact", add_contact),
    ("🔍 Search Contact", search_contact),
    ("✏️ Update Contact", update_contact),
    ("❌ Delete Contact", delete_contact),
    ("📤 Export to CSV", export_to_csv),
    ("📥 Import from CSV", import_from_csv),
    ("🔄 Refresh List", view_contacts),
]

for text, command in button_data:
    tk.Button(btn_frame, text=text, width=22, command=command, font=("Arial", 10), bg="#7289DA", fg="white").pack(pady=5)

root.mainloop()
