# Importing the Libraries
import json
import time

# Opening the file in reading mode
fd = open('Records.json','r')
js =fd.read()
fd.close()

# Loading the json file data in Records(Dct format) 
Records = json.loads(js)
sale =''

# Displaying MENU
print("-"*10,"MENU","-"*10)
for key in Records:
    print(Records[key]["Name"],Records[key]["Price"],Records[key]["Qn"])

# Taking input from user    
print("-"*25)
ur_name  =  str(input("Enter your Name     : "))
ur_em    =  str(input("Enter your email id : "))
ur_phone =  str(input("Enter your phone No : "))
ur_pi    =  str(input("Enter Product ID    : "))
ur_qn    =  int(input("Enter Quantity      : "))

# Checking if we have enough quantity
if(Records[ur_pi]["Qn"] >= ur_qn):
    
# If we're having enough quantity
     #Generating Bill
     print("-"*25)
     print(" "*10,"BILL"," "*10)
     # Updating quantity
     Records[ur_pi]["Qn"] = Records[ur_pi]["Qn"] - ur_qn
     print("Name        : ",Records[ur_pi]["Name"])
     print("Price       : ",Records[ur_pi]["Price"],"Rs")
     print("Quantity    : ",ur_qn)
     
     # Calculating final Amount
     total_amount = ur_qn *Records[ur_pi]["Price"]  # Calculate total bill

     # Applying Discount
     if total_amount > 7000:
        discount = total_amount * 0.10  # 10% discount
        print("You got a 10% discount of ₹", discount)
     elif total_amount > 5000:
        discount = 500  # Flat ₹500 discount
        print("You got a ₹500 discount!")
     else:
        discount = 0  # No discount applied

     final_amount = total_amount - discount  # Final bill after discount
     print("-----------------------------")
     print("Total Amount      : ₹", total_amount)
     print("Discount Applied  : ₹", discount)
     print("Final Amount      : ₹", final_amount)
     print("-----------------------------")
     sale = ur_name+","+ur_em+","+ur_phone+","+ur_pi+","+str(ur_qn)+","+str(final_amount)+","+Records[ur_pi]["Name"]+","+time.ctime()+'\n'
else:
     #If we're not having enough quantity
     print("-"*25)
     print("Sorry we're not having enough quantity \nwe're having only "+str(Records[ur_pi]["Qn"]))
     print("-"*25)
     ch = input("Press Y/y if you want to purchase: ")
     if(ch=='y' or ch=='Y'):
         print("-"*25)
         print(" "*10,"BILL"," "*10)
         print("Name        : ",Records[ur_pi]["Name"])
         print("Price       : ",Records[ur_pi]["Price"],"Rs")
         print("Quantity    : ",Records[ur_pi]["Qn"])
         
         # Calculating final Amount
         total_amount = Records[ur_pi]["Qn"] *Records[ur_pi]["Price"]  # Calculate total bill
         # Applying Discount
         if total_amount > 7000:
              discount = total_amount * 0.10  # 10% discount
              print("You got a 10% discount of ₹", discount)
         elif total_amount > 5000:
             discount = 500  # Flat ₹500 discount
             print("You got a ₹500 discount!")
         else:
           discount = 0  # No discount applied

         final_amount = total_amount - discount  # Final bill after discount
         print("-----------------------------")
         print("Total Amount      : ₹", total_amount)
         print("Discount Applied  : ₹", discount)
         print("Final Amount      : ₹", final_amount)
         print("-----------------------------")
          
         # Updating quantity
         Records[ur_pi]["Qn"] = 0
         # creating sales
         sale = ur_name+","+ur_em+","+ur_phone+","+ur_pi+","+str(Records[ur_pi]["Qn"])+","+str(final_amount)+","+Records[ur_pi]["Name"]+","+time.ctime()+'\n'
     else:
         print("Thanks!")


# Updating Inventory
js = json.dumps(Records)
fd = open("Records.json","w")
fd.write(js)
fd.close()

# Saving Sales
fd = open("Sale.txt","a")
fd.write(sale)
fd.close()