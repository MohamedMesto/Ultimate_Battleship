# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
"https://www.googleapis.com/auth/spreadsheets",
"https://www.googleapis.com/auth/drive.file",
"https://www.googleapis.com/auth/drive"
]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_cake')

 

# Get sales figures input from the user

def get_cake_sales_data():
    """
    Get sales figures input from the user.
    """
    while True:
        print("Please enter cake sales data from the last market.")
        print("Data should be five numbers, separated by commas.")
        print("Example: 10,20,30,40,50\n")

        data_str = input("Enter your data here: ")
        cake_sales_data = data_str.split(",")
        if validate_cake_data(cake_sales_data):
           print("Cake Data Insertion is valid!")
           break

    return cake_sales_data


 

# Get sales figures input from the user
    
def validate_cake_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 5 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 5:
            raise ValueError(
                f"Exactly 5 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

 



# Update cake sales worksheet, add new row with the list data provided

def update_cake_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating Cake sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Cake Sales worksheet updated successfully.\n")


# Comparison Method 
def calculate_cake_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the cake surplus for each item type.

    The surplus is defined as the sales figure subtracted from the stock:
    - Positive cake surplus indicates waste
    - Negative cake surplus indicates extra made when stock was sold out.
    """
    print("Calculating cake surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    # to only the last row in the stock
    stock_row = stock[-1]
    print(stock_row)


#  Run the main program functions
def main_cake_run():
    """
    Run the main program functions
    """
    data = get_cake_sales_data()
    cake_sales_data = [int(num) for num in data]
    update_cake_sales_worksheet(cake_sales_data)
    calculate_cake_surplus_data(cake_sales_data)

 
if __name__ == '__main__':
    print("Welcome to Love Cake Data Automation")
    main_cake_run()