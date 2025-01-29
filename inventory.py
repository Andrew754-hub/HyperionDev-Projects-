
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self, shoe_code):
        '''
        Add the code to return the cost of the shoe in this method.
        '''

        if self.code == shoe_code:
            return self.cost

        else:
            return "Shoe code input invalid"

    def get_quantity(self, shoe_code):
        '''
        Add the code to return the quantity of the shoes.
        '''
        
        if self.code == shoe_code:
            return self.quantity

        else:
            return "Shoe code input invalid"

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return(
f"Code: {self.country} \n"
f"Country: {self.code} \n"
f"Product: {self.product} \n"
f"Cost: {self.cost} \n"
f"Quantity: {self.quantity} \n")

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

    try:
        with open("inventory.txt", "r") as file:

            for line in file:
               data = line.strip().split(",")

            if len(data) == 5:
                    country, code, product, cost, quantity = data
                    cost = float(cost)
                    quantity = int(quantity)

        shoe_list.append(Shoe(code, country, product, cost, quantity))
            
    except FileNotFoundError:
        print(f"Error: the file was not found.")

    except ValueError:
        print("Value error: Please check the data format")

    except Exception:
        print("An unexpected error occured")

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    
    country = input("Enter the country where the shoe is stored: ")
    code = input("Enter the code of the shoe: ")
    product = input("Enter the name of the product shoe: ")
    cost = float(input("Enter the cost of the shoe: "))
    quantity = int(input("Enter the total number of shoes in warehouse: "))

    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)

    with open("inventory.txt", "a") as file:
        for shoe in shoe_list:
            file.write(str(shoe))

        print(f"{new_shoe} added to inventory.")
        
    main()

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

    for shoe in shoe_list:
        print(shoe)

    main()

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

    
    lowest_shoe = min(shoe_list, key = lambda shoe: shoe.quantity)
    print(f"The shoe which is lowest in quantity is {lowest_shoe.product} with quantity of {lowest_shoe.quantity}")

    restock = input(f"Do you want to restock {lowest_shoe.product}? input yes if you want to restock and no if not. ").lower()

    if restock == "yes":

        adding_quantity = int(input("Enter number of shoes to be restocked"))
        lowest_shoe.quantity += adding_quantity
        print(f"After restocking, the new shoe quantity for {lowest_shoe.product} is {lowest_shoe.quantity}")

        with open("inventory.txt", "a") as file:
            file.write(f"Updated {lowest_shoe.product} with code {lowest_shoe.code} to quantity {lowest_shoe.quantity}")

    else: 
        print("Please enter a valid number for restock. No restocking done")

    main()

def seach_shoe(shoe_list, code):
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    
    shoe_code = input("Enter code for shoe you want to search.")
    for shoe in shoe_list:
        if shoe_code == code:
            return shoe
    
        else:
            print("Invalid code entered. Try again")

        main()

def value_per_item(self):
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

    for shoe in shoe_list:
        value = self.cost * self.quantity
        
        print(
f"Product: {shoe.product}"
f"value: R{value}")

        main()

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    highest_shoe = shoe_list[0]

    for shoe in shoe_list:
        if int(shoe.quantity) > highest_shoe:
            highest_shoe_quanity = shoe
        
        print(f"{shoe} is for sale")
        return highest_shoe_quanity.product

    main()

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
def main():

    menu = input(
'''Enter any of the following options:
gc = Get the cost of a particular shoe product.
gq = Get the quantity of a particular shoe product.
cs = Enter new shoe object into the inventory.
va = View all shoe objects in the inventory.
rs = See lowest quantity item and request restock quantity. 
ss = Search for a partuclar shoe and get its information.
vpi = Gives the total value of each item on the list where value means cost by quantity
hq = Indicates shoe with highest quantity and marks status as for sale'
e = Exit the program
''')

    while True:

        read_shoes_data()

        if menu == "gc":
            input("Enter shoe code to get cost").get_cost()
        
        elif menu == "gq":
            input("Enter shoe code to get quantity").get_quantity()

        elif menu == "cs":
            capture_shoes()

        elif menu == "va":
            view_all()

        elif menu == "rs":
            re_stock()

        elif menu == "ss":
            seach_shoe()

        elif menu == "vpi":
            value_per_item()

        elif menu == "hq":
            highest_qty()

        elif menu == "e":
            break

        else:
            print("invalid input please select a valid menu option.")
    
main()