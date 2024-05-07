import sqlite3
import pandas as pd
import tkinter as tk
import tkinter import messagebox

data_Booked = r'C:\Users\MikeA\Desktop\DBMS\booked.csv'
data_Train = r'C:\Users\MikeA\Desktop\DBMS\Train.csv'
data_Train_Status = r'C:\Users\MikeA\Desktop\DBMS\Train_status.csv'
data_Passenger = r'C:\Users\MikeA\Desktop\DBMS\Passenger.csv'

table_map = {
    data_Booked : 'Booked_Table',
    data_Train : 'Train_Table',
    data_Train_Status : 'TrainStatus_Table',
    data_Passenger : 'Passenger_Table'
}


# Function to cnnect to SQLite database
def connect_to_database():
    try: 
        conn = sqlite3.connect("")
        return conn
    except sqlite3.Error as e :
        messagebox.showerror("Error", f"Error connecting to database : {e}")
        return None


# Function to cancel a ticket and update waiting list
def cancel_ticket(passenger_ssn, train_number, conn) :
    try :
        cursor = conn.cursor()

        # Delete the ticket record for the passenger
        cursor.execute("DELETE FROM Booked WHERE Passenger_SSN = ? AND Train_Number = ?", (passenger_ssn, train_number))

        # Retrieve passengers from the waiting list for the same train
        cursor.execute("SELECT Passenger_SSN FROM Booked WHERE Train_Number = ? AND Status = 'Waiting' LIMIT 2", (train_number,))
        waiting_passengers = cursor.fetchall()

        # Update status of waiting list passengers to 'Confirmed'
        for passenger in waiting_passengers :
            cursor.execute("UPDATE Booked SET Status = 'Confirmed' WHERE Passenger_SSN = ? AND Train_Number = ?", (passenger[0], train_number))

        # Commit changes to the database
        conn.commit()
        messagebox.showinfo("Success", "Ticket canceled successfully.")

# Function to fetch train information
def get_train_info() :
    try :
        conn = connect_to_database()
        if conn :
            cursor = conn.cursor()

            # Query to list all train names along with the count of passengers
            cursor.execute("SELECT Train_name, COUNT(Passenger_SSN) AS Passenger_Count FROM Train LEFT JOIN Booked ON Train.Train_Number = Booked.Train_Number GROUP BY Train.Train_Name")
            train_info = cursor.fetchall()
            conn.close()
            return train_info
    
    except sqlite3.Error as e :
        messagebox.showerror("Error", f"Error fetching train information : {e}")
        return None
    
# Function to handle cancel ticket button click event
def on_cancel_ticket() :
    passenger_ssn = passenger_ssn_entry.get()
    train_number = train_number_entry.get()

    if not passenger_ssn or not train_number : 
        messagebox.showerrror("Error", "Please enter passenger SSN and train number.")
        return
    
    # Connect to the SQLite database
    conn = connect_to_database()
    if conn :
        # Call cancel_ticket function with passenger SSN and train number
        cancel_ticket(passenger_ssn, train_number, conn)
        conn.close()

# Function to handle fetch train info button click event
def on_fetch_train_info() :
    # Fetch train information
    train_info = get_train_info()

    if train_info :
        messagebox.showinfo("Train Information", "\n".join([f"Train Name : {row[0]}, Passenger Count: {row[1]}" for row in train_info]))
    else :
        messagebox.showerror("Error", "Train information not found.")

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

# Cancel ticket button
cancel_button = tk.Button(frame, text="Cancel Ticket", command=on_cancel_ticket)
cancel_button.grid(row=2, column=0)

# Fetch train info button
fetch_info_button = tk.Button(frame, text="List Train Info", command=on_fetch_train_info)
fetch_info_button.grid(row=2, column=1)

# Run the GUI application
root.mainloop()

