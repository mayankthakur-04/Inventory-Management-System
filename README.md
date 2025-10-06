# Inventory-Management-System: Overview
<br>
The Inventory Management System is a crucial tool for managing stock and keeping track of products in a business. In this system, we're using file handling to utilizing JSON and dictionaries for data storage.
<br>
Language Used: Python
<br>
# This System have some basic functionality like:
<br>
1. Displaying the Menu:
Before a user selects an item, they need to see what’s available. To do this, we will print a formatted menu displaying:
Product ID
Product Name
Price
Quantity Available
<br>
2. Generating the Bill:
<br>
Once we have the Product ID and Quantity, we can:
Retrieve the product details
Calculate the total cost
Display the final bill
<br>
3.Updating Inventory Records:
<br>
After a purchase, we need to update the inventory stored in our dictionary. For example, if a customer buys 2 chocolate cakes, we would decrease the quantity of chocolate cakes in our dictionary
<br>
4.Saving the Updated Inventory:
To ensure that the updated inventory is saved even after the program is closed, we need to write the updated dictionary to a JSON file. This allows us to keep a record of the current inventory.
