"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-10-16"
-------------------------------------------------------
"""
# Imports

# Constants
RAISE_PERCENTAGE = 5/100
FULLTIME_10 = 1.05
FULLTIME_4 = 1.015
PART_10 = 1.03
PART_4 = 1.01
ALL = 1.02
YEAR_MAX = 10
YEAR_MIN = 4

OFF = 0.05
ONE = 0.95
TWO = 0.9
THREE_OR_MORE = 0.85
    
def gym_cost(cost, friends):
    """
    -------------------------------------------------------
    Calculates total cost of a gym membership. A member gets a
    discount according to the number of friends they sign up.
        0 friends: 0% discount
        1 friend: 5% discount
        2 friends: 10% discount
        3 or more friends: 15% discount
    Use: final_cost = gym_cost(cost, friends)
    -------------------------------------------------------
    Parameters:
        cost - a gym membership base cost (float > 0)
        friends - number of friends signed up (int >= 0)
    Returns:
        final_cost - cost of membership after discount (float)
    ------------------------------------------------------
    """
    

    
    if friends == 0:
        final_cost = cost
    
    elif friends == 1:
        final_cost = cost * ONE
    
    elif friends == 2:
        final_cost = cost * TWO

    else:
        final_cost = cost * THREE_OR_MORE
         
    return final_cost
        
        
def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    year_ans=0
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    
        year_ans= True
    
    else:
        year_ans= False
        
    return year_ans

def get_pay(hourly_rate, hours_worked):
    """
    -------------------------------------------------------
    Calculates an employee's net wage given hours and pay.
    Each employee is paid 1.5 times their regular hourly rate for
    all hours over 40. A tax amount of 3.625 percent of gross salary
    is deducted.
    Use: net_payment = get_pay(hourly_rate, hours_worked)
    -------------------------------------------------------
    Parameters:
        hourly_rate - hourly rate of pay (float)
        hours_worked - total hours worked (float)
    Returns:
        net_payment - description (float)
    ------------------------------------------------------
    """
    TAX = 3.625 / 100
    OVERTIME_RATE = 1.5 - 1
    OVERTIME_HOURS = 40
    
    if hours_worked > OVERTIME_HOURS:
        more_hours = hours_worked - OVERTIME_HOURS
        additional = (more_hours * hours_worked) * OVERTIME_RATE
        total_payment = (hourly_rate * hours_worked) + additional
        net_payment =  total_payment - (total_payment * TAX)
    else:
        total_payment = (hourly_rate * hours_worked)
        net_payment = total_payment - (total_payment * TAX)
        
    return net_payment

def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    PRICE_B = float(6.00)
    PRICE_W = float(8.00)
    PRICE_FRIES = float(1.5)
    PRICE_SALAD = float(2.00)

    choice = input("Enter your choice (B for Burger, W for Wings): ")
    if choice == "B":
        item_price = PRICE_B 
    elif choice == "W":
        item_price = PRICE_W  
    else:
        print("Invalid choice")
        
    
    combo_choice = input("Do you want a combo? (Y/N): ")
    
    if combo_choice == "Y":
        combo_item = input("Enter your combo side (Fries or Salad): ")
        if combo_item == "F":
            item_price = item_price + PRICE_FRIES
        elif combo_item == "S":
            item_price =  item_price + PRICE_SALAD
        else:
            print("Invalid combo choice")
             
    
    return item_price    

def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time greater than or equal to 10 years service
        1.5% for full time less than 4 years service
        3% for part time greater than 10 years service
        1% for part time less than 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """

    if status == "F":
        if years >= YEAR_MAX:
            new_salary = salary * (1 + RAISE_PERCENTAGE)
        elif years < YEAR_MIN:
            new_salary = salary * FULLTIME_4
        else:
            new_salary = salary * ALL

    elif status == "P":
        if years >= YEAR_MAX:
            new_salary = salary * PART_10
        elif years < YEAR_MIN:
            new_salary = salary * PART_4
        else:
            new_salary = salary * ALL

    return new_salary
            
        
        
        


        