"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Imports
from random import randint
# Constants
def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    
    target_number = randint(1, high)
    target_number = 45
    count = 0
    
    while True:
        user_guess = int(input(f"Guess the number between 1 and {high}: "))
        count += 1
        
        if user_guess == target_number:
            print(f"Congratulations! You guessed the number in {count} attempts.")
            break
        elif user_guess < target_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    
    return count


def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    if target < 0:
        raise ValueError("Target value must be >= 0")
    
    current_num = 1
    sum_of_squares = 0
    
    while True:
        sum_of_squares += current_num ** 2
        
        if sum_of_squares >= target:
            return sum_of_squares
        
        current_num += 1
        
        
def num_categories():
    """
    -------------------------------------------------------
    Asks a user to enter a series of numbers, then counts and returns
    how may positives, negatives, and zeroes there are.
    Stop processing values when the user enters -999.
    Use: negatives, zeroes, positives = num_categories()
    -------------------------------------------------------
    Returns:
        negatives - number of negative values (int)
        zeroes - number of zero values (int)
        positives - number of positive values (int)
    ------------------------------------------------------
    """
    negatives = 0
    zeroes = 0
    positives = 0
    
    while True:
        num = float(input("Enter a number (-999 to stop): "))
        
        if num == -999:
            break
        
        if num < 0:
            negatives += 1
        elif num == 0:
            zeroes += 1
        else:
            positives += 1
    return negatives, zeroes, positives
def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    b_total = 0.0
    l_total = 0.0
    s_total = 0.0
    a_total = 0.0

    another_day = True

    while another_day:
        b_cost = float(input("Enter cost of breakfast for the day: "))
        l_cost = float(input("Enter cost of lunch for the day: "))
        s_cost = float(input("Enter cost of supper for the day: "))
        TOTAL_MEAL = b_cost+ l_cost + s_cost
        print(f"Your total for the day was ${TOTAL_MEAL}")
        b_total += b_cost
        l_total += l_cost
        s_total += s_cost
        a_total += (b_cost + l_cost + s_cost)

        another_day_input = input("Do you want to enter data for another day? (y for yes/n for no): ")
        another_day = another_day_input.lower() == 'y'

    return b_total, l_total, s_total, a_total    
    
    

    
 
    
def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the highest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    while True:
        try:
            value = int(input(f"Enter a value between {low} and {high}: "))
            if low <= value <= high:
                return value
            elif value < low:
                print("Value entered is too low")
            else:
                print("Value entered is too high")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        
        
        
        
        
        
        
        