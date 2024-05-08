import tkinter as tk
from tkinter import messagebox


# Create main application window
root = tk.Tk()
root.title("Railway Reservation System")

# Create and configure frame
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Passenger SSN label and entry
passenger_ssn_label = tk.Label(frame, text = "Passenger SSN :")
passenger_ssn_label.grid(row=0, column=0)
passenger_ssn_entry = tk.Entry(frame)
passenger_ssn_entry.grid(row=0, column=1)

# Train number label and entry
train_number_label = tk.Label(frame, text="Train Number:")
train_number_label.grid(row=1, column=0)
train_number_entry = tk.Entry(frame)
train_number_entry.grid(row=1, column=1)

# Train name label and entry
train_name_label = tk.Label(frame, text="Train Name:")
train_name_label.grid(row=2, column=0)
train_name_entry = tk.Entry(frame)
train_name_entry.grid(row=2, column=1)

# Cancel ticket button
cancel_button = tk.Button(frame, text="Cancel Ticket",) #command=on_cancel_ticket)
cancel_button.grid(row=2, column=0)

# Fetch train info button
fetch_info_button = tk.Button(frame, text="List Train Info",) #command=on_fetch_train_info)
fetch_info_button.grid(row=2, column=1)

# Run the GUI application
root.mainloop()