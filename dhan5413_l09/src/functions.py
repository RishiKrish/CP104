"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports

# Constants
def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """
    if len(password) < 8:
        print("Not long enough")
    if not any(char.isdigit() for char in password):
        print("no digits")
        
    if not any(char.isupper() for char in password):
        print("no upper case")
    if not any(char.islower() for char in password):
        print("no lower case")
    return 
    
def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    count = 0
    
    for character in s:
        if (character in "aeiouAEIOU"):
            count = count + 1
    return count
    
def count_special_chars(s):
    """
    -------------------------------------------------------
    Counts the number of special characters in s.
    The special characters are: "#", "@", "$", "%", "&", "!".
    Use: count = count_special_chars(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - number of special characters in s (int)
    ------------------------------------------------------
    """
    special_character = "#", "@", "$", "%", "&", "!"
    COUNT = 0
    for char in s:
        if char in special_character:
            COUNT += 1
            
    return COUNT
    
def comma_period_replace(string):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        out - string with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    swap = string.replace(',', '.')
    return swap

def total_digits(string):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in string.
    Use: total = total_digits(string)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in string (int)
    ------------------------------------------------------
    """
    total = 0
    for k in string:
        if k.isdigit():
            total = total + int(k)
    return total