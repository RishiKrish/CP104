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

# Constants

def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    if number > 0:
        product = 1
    for i in range(1, number + 1):
        product *= i
    
    return product

def calories_treadmill(per_min, minutes):
    """
    -----------------------------------------------------
    Prints the amount of calories burned every five minutes and gives the number 
    of calories burned per minute (per_min) and the total nuumber of minutes run (minutes)
    Uses: Calories_treadmill(per_min, minutes)
    -----------------------------------------------------
    Parameters:
    per_min - number of calories burned per minute (float)
    minutes - total number of minutes run (float)

    Returns:
    None
    -----------------------------------------------------
    """
    print(f"{'Time':<7}  {'Calories Burned':<15}")
    print("--------------------------")

    for time_elapsed in range(5, minutes + 1, 5):
        calories_burned = per_min * time_elapsed
        print(f"{time_elapsed} min  |  {calories_burned:.1f}")
    return

def arrow_up(Rows):
    """
    -----------------------------------------------------
    Use arrow_up(Rows) function takes a integer and prints a arrow of '#' characters that points upwards
    -----------------------------------------------------
    Parameters:
    Rows - the number of rows that will have the '#'
    
    Returns:
    None
    -----------------------------------------------------
    """
    """
    for i in range(Rows):
        gap = " " * (Rows - i -1)
        
        if i == 0:
            print(gap + "#")
        elif i == Rows -1:
            print("#" * (2 *i + 1))
            
        else:
            print(gap + "#" + " " * (2 *i -1) + "#")
    return 

"""

    for i in range(Rows):
        for k in range(Rows - i -1):
            print(" ", end="")
            
        print("#", end="")
        
        for l in range(2 * i -1):
            print(" " if i> 0 else "", end="")
        if i > 0:
            print("#", end ="")
        print()
    return
def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    if start_num <= 0 or stop_num <=0:
        print("Start and stop should be positive numbers")
        return
    
    print("", end="\t")
    for i in range(start_num, stop_num +1):
        print(f"{i}\t", end="")
    print("\n", end="")
    
    print("  " + "-" * (8 *(stop_num + 1)))
    
    for i in range(start_num, stop_num +1):
        print(f"{i} |", end="")
        for k in range(start_num, stop_num + 1):
            print(f"{i * k}\t", end="")
        print("")
    return
def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    
    total = 0
    for i in range (count):
            total = total + start
            start = start + increment
    return total
