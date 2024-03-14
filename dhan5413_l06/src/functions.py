"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-10-23"
-------------------------------------------------------
"""
# Imports

# Constants
def draw_rectangle(height, width, char):
    """
    -------------------------------------------------------
    Prints a rectangle of height and width characters using
    the char character.
    Use: draw_rectangle(height, width, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(height):
        for j in range(width):
            print(char, end = '')
        print()
    return
def draw_hollow_triangle(width, char):
    """
    -------------------------------------------------------
    Prints a hollow triangle of width characters using
    the char character.
    Use: draw_hollow_triangle(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    print (char)
    if width > 1:
        for i in range(width-2):
            print("{}{}{}". format (char, " " * i, char))
        for i in range(width):
            print("{}".format (char), end="")
    print()
    return

def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    if burnt_per_minute <= 0 or start <= 0 or end < start or inc <= 0:
        print("Invalid input. Please enter valid values.")
        return
    
    print("Time (minutes) \t Calories Burnt")
    print("---------------------------------")
    
    for current_time in range(start, end + 1, inc):
        calories_burnt = burnt_per_minute * current_time
        print(f"{current_time} \t\t\t {calories_burnt}")
        
def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print("Age         Salary")
    print("------------------")
    
    if age <= 0 or salary <= 0 or increase < 0:
        print("Invalid input. Please enter valid values.")
        return
    
    
    for i in range(age, 66):
        print(f"{age}      {salary:10,.2f}")
        salary += salary * (increase / 100)
        age = age + 1

def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """

    total = 0.0
    minimum = float('inf')  # set minimum to positive infinity initially
    maximum = float('-inf')  # set maximum to negative infinity initially
    
    for i in range(n):
            value = float(input(f"Value #{i + 1}: "))
            minimum = min(minimum, value)
            maximum = max(maximum, value)
            
            total += value
    
    average = total / n
    return (minimum, maximum, total, average)