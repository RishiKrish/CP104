"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-11-21"
-------------------------------------------------------
"""
# Imports

# Constants
def customer_best(fh):
    """
    -------------------------------------------------------
    Find the customer with the largest balance.
    Assumes file is not empty.
    Use: result = customer_best(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the greatest balance (list)
    -------------------------------------------------------
    """
    best_customer = None 
    max_balance = float('-inf')
    
    for line in fh:
        values = line.strip().split(',')
        
        balance_str = values[3].replace(',','.')
        balance = float(balance_str)
        
        if balance > max_balance:
            max_balance = balance
            best_customer = values
            
    return best_customer

def customer_append(fh, fields):
    """
    -------------------------------------------------------
    Appends a customer record to a comma-delimited sequential file.
    Use: customer_append(fh, fields)
    -------------------------------------------------------
    Parameters:
        fh - file to add to (file handle - already open for appending)
        fields - a list of the field data to append to the file (list)
    Returns:
       None
    -------------------------------------------------------
    """
    
    record = ",".join(map(str, fields))
    
    fh.write(record + "\n")
    return

def append_increment(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of the fh. The number appended
    is the last number in the file plus 1.
    Assumes file is not empty.
    Use: num = append_increment(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    
    lines = fh.readlines()
    if not lines:
        last = 0
    else:
        last = int(lines[-1].strip())
        
    num = last +1
    
    fh.write(str(num) + "\n")
    
    return num


def find_shortest(fh):
    """
    -------------------------------------------------------
    Finds the first word with shortest length in fh.
    Assumes file is not empty.
    Use: word = find_shortest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the first word with the shortest length in fh (str)
    ------------------------------------------------------
    """
    
    
    line = fh.readline().strip()
    words = line.split()
    
    shortest = words[0]
    
    for  word in words:
        if len(word) <len(shortest):
            shortest = word
    fh.close()
    return shortest


def file_copy_n(fh_1, fh_2, n):
    """
    -------------------------------------------------------
    Copies n record from fh_1 (starting from the beginning of the file) to fh2
    Use: file_copy_n(fh_1, fh_2, n)
    -------------------------------------------------------
    Parameters:
        fh_1 - file to search (file handle - already open for reading)
        fh_2 - file to search (file handle - already open for appending)
        n - number of lines to copy from fh_1 to fh_2
    Returns:
        None
    ------------------------------------------------------
    """
    lines_to_copy = [fh_1.readline() for _ in range(n)]
    fh_2.writelines(lines_to_copy)
    
    return
