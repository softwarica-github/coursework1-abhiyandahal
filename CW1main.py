import tkinter as tk
from tkinter import messagebox
import random
import unittest
import os

# Function to generate random transaction data
def generate_transaction_data():
    transaction_id = random.randint(1000, 9999)
    amount = round(random.uniform(10, 500), 2)
    return transaction_id, amount

# Function to perform fraud detection
def detect_fraud(transaction_id, amount):
    # Introducing some random value for fraud detection
    random_value = random.random()
    if amount > 400 or random_value < 0.2:  # 20% probability of being flagged as fraudulent
        return True
    else:
        return False

# Function to perform text analysis and check for fraudulent words in the given description
def check_fraudulent_keywords(description):
    keywords = ['fraud', 'scam', 'fake', 'phishing']  # Example of the list of keywords
    random_value = random.random()
    if random_value < 0.2:  # 20% probability of returning a fraudulent keyword from above
        return True
    return False

# Function to calculate average amount in the last 'n' amount of transactions
def calculate_average_amount_in_time_window(transactions, n):
    if len(transactions) < n:
        return None
    last_n_transactions = transactions[-n:]
    total_amount = sum(transaction['amount'] for transaction in last_n_transactions)
    return total_amount / n

# Function to simulate online transactions 
def simulate_transactions(num_transactions):
    output = "Simulating Online Transactions:\n"
    output += "==============================\n"

    transactions = []

    for _ in range(num_transactions):
        transaction_id, amount = generate_transaction_data()
        description = "This is a sample transaction."  # Replace this with the actual transaction description

        transactions.append({'transaction_id': transaction_id, 'amount': amount})

        is_fraudulent = detect_fraud(transaction_id, amount)

        # Time Series Analysis - To Calculate the average amount in the last 5 transactions
        average_amount_in_time_window = calculate_average_amount_in_time_window(transactions, 5)

        # Text Analysis - Check for fraudulent keywords in the given description
        is_fraudulent_keywords = check_fraudulent_keywords(description)

        output += f"Transaction ID: {transaction_id}\tAmount: ${amount}\n"
        output += f"Transaction Description: {description}\n"

        if is_fraudulent:
            output += "Transaction flagged as fraudulent!\n"
            output += "Transaction refused.\n"
        else:
            output += "Transaction approved.\n"

        if is_fraudulent_keywords:
            output += "Transaction contains fraudulent keywords!\n"
        else:
            output += "Transaction does not contain any fraudulent keywords.\n"

        if average_amount_in_time_window is not None:
            output += f"Average Amount in Last 5 Transactions: ${average_amount_in_time_window}\n"
        else:
            output += "Not enough transactions for calculation.\n"

        output += "------------------------\n"

    output += "Simulation complete."
    return output

# To create the main window
window = tk.Tk()
window.title("Online Transaction Fraud Detection")
window.geometry("1000x600")  # Adjust window size as needed

# Setting background colors
login_bg_color = "#30D5C8"  # Teal blue
transaction_bg_color = "#E0CCE3"  # Light purple

# Creating the login frame
login_frame = tk.Frame(window, bg=login_bg_color)
login_frame.pack(expand=True, fill=tk.BOTH)

# Creating the abstract background elements such as the circle and rectangular
canvas = tk.Canvas(login_frame, bg=login_bg_color, width=600, height=400)
canvas.pack()

# Create the circles
canvas.create_oval(50, 50, 200, 200, fill="#FFFFFF")  # Circle on top left of white colour
canvas.create_oval(400, 250, 550, 400, fill="#FFFFFF")  # Circle on bottom right of white colour

# Creating the "XYZ Online Transaction Fraud Detection" text, the random name is given to the app so that there wont be any confusion
canvas.create_text(275, 225, text="XYZ Online Transaction Fraud Detection", font=("Helvetica", 16), fill="black")

# Creating the login elements
login_label = tk.Label(login_frame, text="Login", font=("Helvetica", 24, "bold"), bg=login_bg_color)
login_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

username_label = tk.Label(login_frame, text="Username:", bg=login_bg_color, font=("Helvetica", 14))
username_label.place(relx=0.35, rely=0.6, anchor=tk.CENTER)
username_entry = tk.Entry(login_frame, font=("Helvetica", 14))
username_entry.place(relx=0.55, rely=0.6, anchor=tk.CENTER)

password_label = tk.Label(login_frame, text="Password:", bg=login_bg_color, font=("Helvetica", 14))
password_label.place(relx=0.35, rely=0.7, anchor=tk.CENTER)
password_entry = tk.Entry(login_frame, show="*", font=("Helvetica", 14))
password_entry.place(relx=0.55, rely=0.7, anchor=tk.CENTER)

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "abhiyan123" and password == "aviyan123456":
        login_frame.pack_forget()
        transaction_frame.pack()
    else:
        messagebox.showerror("Invalid Credentials", "Invalid username or password")

login_button = tk.Button(login_frame, text="Login", command=validate_login, font=("Helvetica", 14))
login_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Creating the transaction frame
transaction_frame = tk.Frame(window, bg=transaction_bg_color)

# Creating the transaction elements in the transaction frame
num_transactions_label = tk.Label(transaction_frame, text="Number of Transactions:", font=("Helvetica", 14), bg=transaction_bg_color)
num_transactions_label.pack(pady=10)

num_transactions_entry = tk.Entry(transaction_frame, font=("Helvetica", 14))
num_transactions_entry.pack(pady=10)

def simulate_transactions_gui():
    num_transactions = int(num_transactions_entry.get())
    output = simulate_transactions(num_transactions)

    # To Clear the output area and display the results
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output)

    # To Save the output as a .txt file on the desktop of my local PC of Abhiyan
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    output_file_path = os.path.join(desktop_path, 'fraud_detection_results.txt')
    with open(output_file_path, 'w') as file:
        file.write(output)

    messagebox.showinfo("Simulation Results", f"Simulation complete! Results saved as {output_file_path}")

    # To Save the output as a .txt file on the desktop
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    output_file_path = os.path.join(desktop_path, 'fraud_detection_results.txt')
    with open(output_file_path, 'w') as file:
        file.write(output)

    # To Clear the output area and display a message box
    output_text.delete("1.0", tk.END)
    messagebox.showinfo("Simulation Results", f"Simulation complete! Results saved as {output_file_path}")

# Creating the simulate button
simulate_button = tk.Button(transaction_frame, text="Simulate Transactions", command=simulate_transactions_gui, font=("Helvetica", 14))
simulate_button.pack(pady=10)

# Modify the output_text widget to fill the whole window and expand with available space
output_text = tk.Text(transaction_frame, wrap=tk.WORD, width=1080, height=80)
output_text.pack(fill=tk.BOTH, expand=True)  # The code Fills the whole window and expand with available space

# Run the GUI event loop
window.mainloop()

# Unit testing for generate_transaction_data() and detect_fraud()
class TestTransactionFunctions(unittest.TestCase):
    def test_generate_transaction_data(self):
        transaction_id, amount = generate_transaction_data()
        self.assertTrue(1000 <= transaction_id <= 9999)
        self.assertTrue(10 <= amount <= 500)

    def test_detect_fraud(self):
        # Test case for non-fraudulent transaction
        self.assertFalse(detect_fraud(1234, 100))

        # Test case for fraudulent transaction with a high amount
        self.assertTrue(detect_fraud(5678, 600))

        # Test case for a random non-fraudulent transaction (run the test multiple times)
        for _ in range(100):
            random_transaction_id = random.randint(1000, 9999)
            random_amount = round(random.uniform(10, 500), 2)
            self.assertFalse(detect_fraud(random_transaction_id, random_amount))

# Integration test for simulate_transactions()
class TestSimulateTransactions(unittest.TestCase):
    def test_simulate_transactions(self):
        # Test case for simulating 1 transaction
        output = simulate_transactions(1)
        self.assertIn("Transaction ID:", output)
        self.assertIn("Amount:", output)
        self.assertIn("Transaction Description:", output)
        self.assertIn("Transaction approved.", output)
        self.assertIn("Transaction does not contain any fraudulent keywords.", output)

        # Test case for simulating 5 transactions
        output = simulate_transactions(5)
        self.assertIn("Transaction ID:", output)
        self.assertIn("Amount:", output)
        self.assertIn("Transaction Description:", output)
        self.assertIn("Transaction approved.", output)
        self.assertIn("Transaction does not contain any fraudulent keywords.", output)

if __name__ == '__main__':
    # To Run the unit tests and integration test
    unittest.main()