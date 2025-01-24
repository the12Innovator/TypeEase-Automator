import pyautogui as pag
import pandas as pd
import time
import tkinter as tk
from tkinter import messagebox

# Function to read the Excel file and extract stock names
def get_stock_names(file_path):
    df = pd.read_excel(file_path)
    stock_names = df.iloc[0:20, 2].dropna().tolist()
    return df, stock_names

# Function to automate typing and interactions
def automate_typing(stock_name):
    # Click on the search bar and type the stock name
    pag.click(x=1824, y=129)
    pag.typewrite(stock_name, interval=0.1)
    time.sleep(2)  # Wait for suggestions to appear
    
    # Click on the suggested name
    pag.click(x=1035, y=295)
    time.sleep(2)
    
    # Scroll down the page
    pag.scroll(-1500)  # Increased scroll amount
    time.sleep(2)

# Main process function
def process_stocks():
    file_path = r"C:\Users\Lenovo\OneDrive\Documents\Projects\Python\TypeEase Automator\Selected_stocks.xlsx"
    df, stock_names = get_stock_names(file_path)

    # Iterate through the stock names with count
    total_stocks = len(stock_names)
    for idx, stock in enumerate(stock_names, start=1):
        print(f"{idx}/{total_stocks} {stock}")  # Print the count and stock name
        automate_typing(stock)
        
        # Ask user if they need this stock
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        user_input = messagebox.askyesno("Stock Inquiry", f"Do you need this stock: {stock}?")
        root.destroy()  # Destroy the root window

        if not user_input:
            # Remove the stock from the DataFrame
            df = df[df.iloc[:, 2] != stock]

    # Save the updated DataFrame back to the Excel file
    df.to_excel(file_path, index=False)
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Info", "Process completed and Excel file updated.")
    root.destroy()

# Initial run
process_stocks()

print("Automation completed.")
