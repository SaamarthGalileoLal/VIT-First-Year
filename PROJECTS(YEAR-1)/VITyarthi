# Import the built-in CSV module so we can read and write csv files:)
import csv

# Define the filename where all inventory data will be stored
csvfil = "VITyarthiproject.csv"


def isthecsvfievenreal():
    """
    Checks the CSV file for its existence.
    If it exists, opens and closes it safely.
    If it does not exist, catches FileNotFoundError and creates a new file with headers.
    """
    try:
        #open the file in read mode to check if it exists
        with open(csvfil, "r") as file:
            pass  # File exists, so do nothing and exit the try block
    except FileNotFoundError:
        # If the file is missing, ALERT the user!
        print("THE FILE DOES NOT EXIST :( Creating a new one...")
        
        # Create a new file in write mode ("w") and write the header row,this also makes a new file if it doesn't exist:
        with open(csvfil, "w", newline="") as file:
            writer = csv.writer(file)
            # Write column headers to define the structure
            writer.writerow(["Name", "Category", "Price", "Quantity"])


def addtheitemstothefile():
    """
    Asking the user for item details (Name, Category, Price, Quantity)
    and appends them as a new row to the CSV file.
    """
    # Open the CSV file in append mode ("a") so existing data isn't overwritten
    with open(csvfil, "a", newline="") as file:
        writer = csv.writer(file)
        
        # Take user input for each property of the item
        name = input("Enter the name: ").strip()
        category = input("Enter the category of item: ").strip()
        price = input("Enter the price: ").strip()
        quantityofitem = input("Enter the quantity of item: ").strip()
        
        # Write the new row to the CSV file
        writer.writerow([name, category, price, quantityofitem])
        
        # Confirm addition to the user
        print("Items added to the file: Name:", name, "| Category:", category, "| Price:", price, "| Quantity:", quantityofitem)


def calcthemprices(*multipleprices):
    """
    Uses variable-length positional arguments (*args) to accept multiple price values
    and calculate their combined total.
    """
    tota = 0  # Initialize sum variable
    
    # Iterate through all price values passed into *multipleprices
    for price in multipleprices:
        tota += price  # Add each item's price to the running total
        
    return tota  # Return the grand total back to the caller


def display_inventory():
    """
    Reads all inventory records from the CSV file, prints them in a clean format,
    and calculates the total stock valuation.
    """
    try:
        # Open file in read mode ("r")
        with open(csvfil, "r") as file:
            reader = csv.reader(file)
            headers = next(reader, None)  # Skip reading the header row
            
            # Convert reader contents into a Python list of rows
            items = list(reader)
            
            # Check if the list of items is empty
            if not items:
                print("\n--- Current Main Inventory ---")
                print("No inventory items logged yet.\n")
                return

            print("\n--- Current Main Inventory ---")
            prices = []  # List to store (Price * Quantity) for each item
            
            # Loop through each item row in the CSV
            for row in items:
                if row:  # Ensure row is not an empty line
                    # Unpack the 4 columns from the row
                    name, category, price, qty = row
                    
                    # Display item details
                    print("Name:", name, "| Category:", category, "| Quantity:", qty, "| Price: $", price)
                    
                    # Calculate total value for this item (Price * Quantity) and add to list
                    prices.append(float(price) * int(qty))

            # Call calcthemprices using * unpacking on the prices list
            total_stock_value = calcthemprices(*prices)
            
            # Print total formatted to 2 decimal places
            print("-" * 55)
            print("Total Valuation of Stock: $", format(total_stock_value, ".2f"), "\n")

    except FileNotFoundError:
        # Handle case where file hasn't been created yet
        print("Inventory file not found.\n")


# MAIN CODE
if __name__ == "__main__":
    # the file exists before running the main menu or not:
    isthecsvfievenreal()
    
    # CLI main CODE:
    while True:
        print("=== INVENTORY MENU ===")
        print("1. Add Item")
        print("2. Display Inventory")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            addtheitemstothefile()
        elif choice == "2":
            display_inventory()
        elif choice == "3":
            print("Exiting project. Good luck!")
            break  # Break out of the loop!
        else:
            print("Invalid choice, try again!\n")