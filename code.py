# Importing Libraries
import json
import time
import os

# -------------------------------------------
# Load Inventory from JSON
# -------------------------------------------
def load_inventory():
    if not os.path.exists("Records.json"):
        return {}
    with open("Records.json", "r") as f:
        return json.load(f)

# -------------------------------------------
# Save Inventory to JSON
# -------------------------------------------
def save_inventory(records):
    with open("Records.json", "w") as f:
        json.dump(records, f, indent=4)

# -------------------------------------------
# Save Sales to Sale.txt
# -------------------------------------------
def save_sale(sale_entry):
    with open("Sale.txt", "a") as f:
        f.write(sale_entry + "\n")

# -------------------------------------------
# Display all products
# -------------------------------------------
def display_inventory(records):
    print("\n" + "-" * 10, "INVENTORY", "-" * 10)
    for pid, item in records.items():
        print(f"ID: {pid} | Name: {item['Name']} | Price: ₹{item['Price']} | Qty: {item['Qn']}")
    print("-" * 35)

# -------------------------------------------
# Add a new product
# -------------------------------------------
def add_product(records):
    print("\n--- Add New Product ---")

    new_id = input("Enter Product ID: ").strip()

    if new_id in records:
        print(" Product ID already exists!")
        return

    name = input("Enter Product Name: ")
    
    # Validate price
    while True:
        try:
            price = float(input("Enter Price: "))
            break
        except:
            print("Enter a valid number for price!")

    # Validate quantity
    while True:
        try:
            qn = int(input("Enter Quantity: "))
            break
        except:
            print("Enter a valid number for quantity!")

    records[new_id] = {"Name": name, "Price": price, "Qn": qn}
    save_inventory(records)
    print(" Product added successfully!")

# -------------------------------------------
# View all sales
# -------------------------------------------
def view_sales():
    print("\n--- SALES REPORT ---")
    if not os.path.exists("Sale.txt"):
        print("No sales yet!")
        return

    with open("Sale.txt", "r") as f:
        data = f.read()
        print(data if data else "No sales recorded.")

# -------------------------------------------
# Handle purchase process
# -------------------------------------------
def purchase(records):
    display_inventory(records)

    print("\n--- Purchase Product ---")
    name = input("Enter your Name: ")
    email = input("Enter your Email: ")
    phone = input("Enter Phone Number: ")

    product_id = input("Enter Product ID: ")

    if product_id not in records:
        print(" Invalid Product ID!")
        return

    # Validate quantity input
    while True:
        try:
            qn = int(input("Enter Quantity to Buy: "))
            break
        except:
            print("Enter a valid number!")

    product = records[product_id]

    # Check stock availability
    if product["Qn"] < qn:
        print(f"Only {product['Qn']} available. Do you want to buy all?")
        choice = input("Press Y to continue: ").lower()

        if choice != "y":
            print("Purchase cancelled.")
            return

        qn = product["Qn"]

    # BILL CALCULATION
    print("\n--- BILL ---")
    total = qn * product["Price"]

    # Apply discounts
    if total > 7000:
        discount = total * 0.10
    elif total > 5000:
        discount = 500
    else:
        discount = 0

    final = total - discount

    print(f"Name       : {product['Name']}")
    print(f"Price      : ₹{product['Price']}")
    print(f"Quantity   : {qn}")
    print(f"Total      : ₹{total}")
    print(f"Discount   : ₹{discount}")
    print(f"Final Bill : ₹{final}")

    # Update inventory
    product["Qn"] -= qn
    save_inventory(records)

    # Save sale entry
    sale_data = f"{name},{email},{phone},{product_id},{qn},{final},{product['Name']},{time.ctime()}"
    save_sale(sale_data)

    print(" Purchase Successful!")

# -------------------------------------------
# Main Menu Loop
# -------------------------------------------
def main():
    records = load_inventory()

    while True:
        print("\n" + "-" * 12 + " MENU " + "-" * 12)
        print("1. View Inventory")
        print("2. Add Product")
        print("3. Purchase Product")
        print("4. View Sales Report")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            display_inventory(records)
        elif choice == "2":
            add_product(records)
        elif choice == "3":
            purchase(records)
        elif choice == "4":
            view_sales()
        elif choice == "5":
            print("Thank You!")
            break
        else:
            print(" Invalid choice! Try again.")

# Run the program
main()
