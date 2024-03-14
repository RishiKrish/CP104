"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-10-20"
-------------------------------------------------------
"""
# Imports

# Constants

def day_name(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is "Sunday", day 7 is "Saturday".
    Returns "Error" if the number is not valid.
    Use: day = day_name(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """
    
    if  1 <= day_num <= 7:
        days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days_of_week[day_num - 1]

def pollution_ranking(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy" for Sensitive Groups - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution = pollution_ranking(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """
    if air_quality_index >= 0:
        if air_quality_index <= 50:
            pollution = "Good"
        elif air_quality_index <= 100:
            pollution = "Moderate"
        elif air_quality_index <= 150:
            pollution = "Unhealthy for Sensitive Groups"
        elif air_quality_index <= 200:
            pollution = "Unhealthy"
        elif air_quality_index <= 300:
            pollution = "Very Unhealthy"
        else:
            pollution = "Hazardous"

        return pollution


def largest_average(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the average of the two largest values of
    val1, val2, and val3.
    Use: average = largest_average(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        average - the average of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    largest = max(val1, val2, val3)
    
    if largest == val1:
        second_largest = max(val2, val3)
        
    elif largest == val2:
        second_largest = max(val1, val3)
    else:
        second_largest = max(val1, val2)
    
    average = (largest + second_largest) / 2
    return average



def colour_combine(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """
    
    
    
    if (rgb_colour1 == "red" and rgb_colour2 == "blue") or (rgb_colour1 == "blue" and rgb_colour2 == "red"):
            color = "fuchsia"
    elif (rgb_colour1 == "red" and rgb_colour2 == "green") or (rgb_colour1 == "green" and rgb_colour2 == "red"):
            color = "yellow"
    elif (rgb_colour1 == "green" and rgb_colour2 == "blue") or (rgb_colour1 == "blue" and rgb_colour2 == "green"):
            color = "aqua"
    elif rgb_colour1 == rgb_colour2:
            color = rgb_colour1
    return color



'''
def hoo_rah(number):
    
    if number % 2 == 0 and number % 7 ==0:
        result = "Hoo Rah"
    elif number % 2 == 0:
        result = "Hoo"
    elif number % 7 ==0:
        result = "Rah"
    else:
        result = "Zip"
    return result
'''

def hoo_rah(number):
    """
    -------------------------------------------------------
    Use hoo_rah(number) takes an integer parameter and returns one of the following strings:
    Parameters:
    "Hoo" if number is evenly divisible by 2
    "Rah" if number is evenly divisible by 7
    "Hoo Rah" if number is evenly divisible by both 2 and 7
    "Zip" if number is none of the above
    Returns:
    ans
    -------------------------------------------------------
    """
    divisible_by_2 = (number // 2) * 2 == number
    divisible_by_7 = (number // 7) * 7 == number
    ans = 0

    if divisible_by_2 and divisible_by_7:
        ans = "Hoo Rah"
    elif divisible_by_2:
        ans = "Hoo"
    elif divisible_by_7:
        ans = "Rah"
    else:
        ans = "Zip"
    return ans