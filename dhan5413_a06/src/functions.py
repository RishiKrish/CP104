"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-11-10"
-------------------------------------------------------
"""
# Imports


# Constants
def total_wins():
    """
    -------------------------------------------------------
    it requests the user to enter a series of strings that show the output of a game with a loop
    Use: 
    total_wins uses while loop to check how many times the user enters which team is winning until its false and it adds the respective entered team and stores it in the variable
    -------------------------------------------------------
    Parameters:
    None
    -------------------------------------------------------
    Returns:
    purple_c , gold_c
    -------------------------------------------------------
    """
    purple_c = 0
    gold_c = 0
    while True:
        team = input("Enter the team thats winning: ")
        
        if not team:
            break
        if team == "purple":
            purple_c += 1
        elif team == "gold":
            gold_c += 1
    return purple_c, gold_c



def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    divisor = 2
    
    if number <= 1:
        output = False
        
    while divisor * divisor <= number:
        if number % divisor == 0:
            output = False
        divisor += 1
        output = True
        
    return output


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    monthly_rate = interest_rate / 100 / 12
    MONTH = 1
    bal = principal_amount
    
    print(f"Principal: ${principal_amount:.2f}")
    print(f"Interest Rate: {interest_rate:.2f}%")
    print(f"Monthly payment: ${payment:.2f}")
    print("----------------------------------")
    print("Month Interest   Payment   Balance")
    print("----------------------------------")

    while bal > 0:
        monthly_interest = bal * monthly_rate
        new_payment = min(payment, bal + monthly_interest)
        bal -= new_payment - monthly_interest
        print(
            f"   {MONTH:<3d}    {monthly_interest:.2f}    {new_payment:.2f}    {bal:.2f}")
        MONTH +=1
    return


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    
    DIGITS = 0
    num1 = abs(number)
    while num1 > 0:
        num1 = num1 // 10
        DIGITS += 1
        
    return DIGITS

def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    
    total = 0
    div = 1
    
    while div < number:
        if number % div ==0:    
            total += div
        div += 1
    return total
    
    