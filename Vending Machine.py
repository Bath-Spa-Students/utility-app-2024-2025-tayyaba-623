print(""" \n \033[33m
     
 ██╗       ██╗ ███████╗ ██╗      ██╗     █████╗   █████╗   ███╗   ███╗ ███████╗      ████████╗  █████╗      ███╗   ███╗ ██╗   ██╗
 ██║  ██╗  ██║ ██╔════╝ ██║      ██║     ██╔══██╗ ██╔══██╗ ████╗ ████║ ██╔════╝      ╚══██╔══╝ ██╔══██╗     ████╗ ████║ ╚██╗ ██╔╝
 ╚██╗████╗██╔╝ █████╗   ██║      ██║     ██║  ╚═╝ ██║  ██║ ██╔████╔██║ █████╗           ██║    ██║  ██║     ██╔████╔██║  ╚████╔╝
  ████╔═████║  ██╔══╝   ██║      ██║     ██║  ██╗ ██║  ██║ ██║╚██╔╝██║ ██╔══╝           ██║    ██║  ██║     ██║╚██╔╝██║   ╚██╔╝
  ╚██╔╝ ╚██╔╝  ███████╗ ███████╗ ███████╗ █████╔╝ ╚█████╔╝ ██║ ╚═╝ ██║ ███████╗         ██║    ╚█████╔╝     ██║ ╚═╝ ██║    ██║
   ╚═╝   ╚═╝   ╚══════╝ ╚══════╝ ╚══════╝ ╚════╝   ╚════╝  ╚═╝     ╚═╝ ╚══════╝         ╚═╝     ╚════╝      ╚═╝     ╚═╝    ╚═╝

██╗   ██╗ ███████╗ ███╗  ██╗ ██████╗  ██╗ ███╗  ██╗  ██████╗      ███╗   ███╗  █████╗   █████╗  ██╗  ██╗ ██╗ ███╗  ██╗ ███████╗
██║   ██║ ██╔════╝ ████╗ ██║ ██╔══██╗ ██║ ████╗ ██║ ██╔════╝      ████╗ ████║ ██╔══██╗ ██╔══██╗ ██║  ██║ ██║ ████╗ ██║ ██╔════╝
╚██╗ ██╔╝ █████╗   ██╔██╗██║ ██║  ██║ ██║ ██╔██╗██║ ██║  ██╗      ██╔████╔██║ ███████║ ██║  ╚═╝ ███████║ ██║ ██╔██╗██║ █████╗
 ╚████╔╝  ██╔══╝   ██║╚████║ ██║  ██║ ██║ ██║╚████║ ██║  ╚██╗     ██║╚██╔╝██║ ██╔══██║ ██║  ██╗ ██╔══██║ ██║ ██║╚████║ ██╔══╝
  ╚██╔╝   ███████╗ ██║ ╚███║ ██████╔╝ ██║ ██║ ╚███║ ╚██████╔╝     ██║ ╚═╝ ██║ ██║  ██║ ╚█████╔╝ ██║  ██║ ██║ ██║ ╚███║ ███████╗
   ╚═╝    ╚══════╝ ╚═╝  ╚══╝ ╚═════╝  ╚═╝ ╚═╝  ╚══╝  ╚═════╝      ╚═╝     ╚═╝ ╚═╝  ╚═╝  ╚════╝  ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚══╝ ╚══════╝ \033[0m\n""")
Menu = {
"Drinks" :[
    {"Code" : "X1" , "Item" : "Water" , "Price" : "£1" , "Stock" : "20"},
    {"Code" : "X2" , "Item" : "Strawberry juice" , "Price" : "£2" , "Stock" : "20"},
    {"Code" : "X3" , "Item" : "Cold coffee" , "Price" : "£4" , "Stock" : "20"},
    {"Code" : "X4" , "Item" : "Coca-Cola" , "Price" : "£1" , "Stock" : "20"},
    {"Code" : "X5" , "Item" : "Hot chocolate" , "Price" : "£3" , "Stock" : "20"}
],

"Snacks" :[
    {"Code" : "Y1" , "Item" : "Protein Bars" , "Price" : "£2" , "Stock" : "20"},
    {"Code" : "Y2" , "Item" : "Doritos" , "Price" : "£1" , "Stock" : "20"},
    {"Code" : "Y3" , "Item" : "Lays" , "Price" : "£3" , "Stock" : "20"},
    {"Code" : "Y4" , "Item" : "M&MS" , "Price" : "£2" , "Stock" : "20"},
    {"Code" : "Y5" , "Item" : "Twix" , "Price" : "£2" , "Stock" : "20"}
],

"Desserts" :[
    {"Code" : "Z1" , "Item" : "Brownies" , "Price" : "£3" , "Stock" : "20"},
    {"Code" : "Z2" , "Item" : "Chocolate icecream" , "Price" : "£5" , "Stock" : "20"},
    {"Code" : "Z3" , "Item" : "Macrons" , "Price" : "£4" , "Stock" : "20"},
    {"Code" : "Z4" , "Item" : "Choccolate Donuts" , "Price" : "£5" , "Stock" : "20"},
    {"Code" : "Z5" , "Item" : "Caramel Pudding" , "Price" : "£6" , "Stock" : "20"}
]
}

from prettytable import PrettyTable  # Displaying Menu through prettytable
def display_menu():
    first_Table = PrettyTable(["\033[36m Code" , "Drinks" , "Price" , "Stock"])  # Printing Columns of the first table
    Second_Table = PrettyTable(["\033[36m Code" , "Snacks" , "Price" , "Stock"]) # Printing Columns of the second table
    Third_Table = PrettyTable(["\033[36m Code" , "Desserts" , "Price" , "Stock"]) # Printing Columns of the third table 
    for item in Menu["Drinks"]:
        first_Table.add_row([item["Code"], item["Item"], item["Price"], item["Stock"]])
    for item in Menu["Snacks"]:
        Second_Table.add_row([item["Code"], item["Item"], item["Price"], item["Stock"]])
    for item in Menu["Desserts"]:
        Third_Table.add_row([item["Code"], item["Item"], item["Price"], item["Stock"]])
    first_Table.align = "l"
    Second_Table.align = "l"
    Third_Table.align = "l"
    print(first_Table)
    print(Second_Table)
    print(Third_Table)
display_menu()

def V_Machine():
      while True:
        user_answer = input("\n\033[33m Enter the code of the item that you want to buy, Enter E to End: \033[0m") # Taking input from the user
        if user_answer == "E":
           print("\n\033[35m Thank You for using the Vending Machine \033[0m")
           break
        valid_code = False
        for Item in Menu:
            for item in Menu[Item]:
                if user_answer == item["Code"]:
                   valid_code = True
                   item['Stock'] = int(item['Stock'])
                   if item['Stock'] > 0:
                      print(f"\n\033[35m Item: {item['Item']} || You have to pay: {item['Price']} \033[0m")
                      Stock(item)  # Calling the function to update the stock
                      answer = input("\n\033[31m Enter Payment: £\033[0m").strip().replace('£', '')
                      answer = float(answer)  # Converting the string into a float
                      Payment_Management(answer, item)
                   else:
                       print(f"\n\033[34m {item['Item']} is out of stock \033[0m")
                   break
        if not valid_code:   # Using if statement to check the invalid code
         print("\n\033[37m Invalid code. Please choose any code from the menu \033[0m")

def Payment_Management(answer, item):
    Price = int(item['Price'].strip('£'))
    if answer < Price:
       Total_Payment = Price - answer
       print(f"\n\033[36m Insufficient amount. You have to pay furtur £{Total_Payment :.0f} \033[0m")
       answer = input("\n\033[31m Enter Payment: £\033[0m")
       print("\n\033[36m Payment has been successfully done || Item has been dispensed \033[0m")
       displaying_Messages(item) # Calling the function to ask the user about their decision 
    elif answer > Price:
        Change = answer - Price
        print(f"\n\033[35m £{Change :.0f} is your change \033[0m")
        displaying_Messages(item) # Calling the function to ask the user about their decision 
    elif answer == Price:
        print("\n\033[36m Payment has been successfully done || Item has been dispensed \033[0m")
        displaying_Messages(item) 
        return

def displaying_Messages(item):
    print(f"\n\033[33m Would you like to buy something with {item['Item']} ? \033[0m")
    user_choice = input("\n\033[34m Enter Yes or No: \033[0m")
    if user_choice == "No":
       print("\n\033[35m Thank you for using the Vending Machine. \033[0m")
       exit()

def Stock(item):
    if item['Stock'] > 0:
       Remaining_Stock = item['Stock'] -1 # Checking the remaining stock
       item['Stock'] = Remaining_Stock
       print(f"\n\033[35m Reamining Stock: {Remaining_Stock} \033[0m")

V_Machine()
    
