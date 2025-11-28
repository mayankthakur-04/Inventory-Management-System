# Inventory Management System (Python + JSON)

A simple beginner-friendly inventory management system built using **Python** and **JSON**.  
You can run it directly in **Jupyter Notebook** or as a normal Python script.

This project allows you to **manage products**, **generate bills**, **apply discounts**, **save sales history**, and **update inventory automatically**.

------------------------------------------------------------------
## Features

### View Inventory  
Displays all available products with ID, name, price, and stock.

### Add New Products  
Easily expand your inventory by adding new product IDs, names, prices, and quantities.

### Purchase Items  
Generates a bill, applies discounts, and updates inventory.

### Discount System  
- 10% discount for bills above ₹7000  
- Flat ₹500 discount for bills above ₹5000  

###  Sales Report  
All sales are saved in **Sale.txt**, giving a complete purchase history.

### Input Validation  
Prevents errors by restricting invalid inputs.

### Main Menu Loop  
Program keeps running until you choose to exit.

-----------------------------------------------------------------------------

##  Project Structure

 Inventory-Management-System
│
├── code.py # Main Python program
├── Records.json # Inventory database (auto updated)
├── Sale.txt # Sales history (auto updated)
├── README.md # Project documentation
└── requirements.txt # Python dependencies

------------------------------------------------------------------------
##  How to Run the Project

### **1. Install Python (if not installed)**  
Download from: https://www.python.org/downloads/

### **2. Install required libraries**
pip install -r requirements.txt

### **3. Run the program**
python code.py

Or run inside Jupyter Notebook.

-----------------------------------------------------------------

## Files Explanation

### **Records.json**
Stores all products like:
```json
{
    "101": {"Name": "Pen", "Price": 10, "Qn": 50},
    "102": {"Name": "Notebook", "Price": 40, "Qn": 20}
}

Sale.txt
Stores every purchase:

Rahul,rahul@gmail.com,9876543210,101,2,20,Pen,Mon Nov 25 14:20:40 2024

code.py
The main program containing:
Inventory loading/saving
Purchase system
Sales tracking
Add product feature
Menu system


Author
Created by : MAYANK THAKUR
