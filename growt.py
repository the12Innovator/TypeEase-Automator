import pyautogui as pag
import pandas as pd
import time

# Function to read the Excel file and extract stock names from cells C2 to C4
def get_stock_names(file_path):
    df = pd.read_excel(file_path, usecols="C", skiprows=1, nrows=11)  # Read only the required range (C2 to C4)
    stock_names = df.dropna().iloc[:, 0].tolist()  # Drop any empty cells and convert to list
    return stock_names

# Function to automate typing and interactions
def automate_typing(stock_name):
    # Click on the search bar and type the stock name
    pag.click(x=1387, y=332)
    pag.typewrite(stock_name, interval=0.1)
    time.sleep(1)  # Wait for the typing to finish
 
    # Click on the save button
    pag.click(x=1717, y=395)
    time.sleep(1)  # Wait for the click to register

    # Click on the clear button
    pag.click(x=1728, y=333)
    time.sleep(1)  # Wait for the click to register

# Main function to process the stock names
def process_stocks():
    file_path = r"C:\Users\Lenovo\OneDrive\Documents\Projects\Python\TypeEase Automator\Selected_stocks.xlsx"
    stock_names = get_stock_names(file_path)

    for stock in stock_names:
        print(f"Processing stock: {stock}")
        automate_typing(stock)
        time.sleep(2)  # Wait between processing each stock name

    print("Automation completed.")

# Initial run
process_stocks()
