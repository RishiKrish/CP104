"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-11-29"
-------------------------------------------------------
"""
# Imports

# Constants
def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """

    k = 0
    while k < count:
        line_num = file_handle.read().strip()
        if not line_num:
            break
        print(line_num)
        k += 1 
    return

def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    number_list = []
    for line in file_handle:
        file_token = line.split(',')
        
        for token in file_token:
            if token.strip().isdigit():
                number_list.append(int(token.strip()))
            
    return number_list


def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    rcount = 0
    
    for line in file_handle:
        for char in line:
            if char.isupper():
                ucount +=1
            elif char.islower():
                lcount +=1
            elif char.isdigit():
                dcount +=1 
            elif char.isspace():
                wcount +=1 
            else:
                rcount +=1
                
    return ucount, lcount, dcount, wcount, rcount


def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    '''
    for j, line in enumerate(fh_read):
        fh_write.write(f"[{j}] {line}")
    return
    '''
    lines = fh_read.readlines()
    for j, line in enumerate(lines, start=0):
        fh_write.write(f'[{j}]{line}')
    return

def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    T_MARKS = 0
    MINIMUM_MARK = float('inf')
    MAXIMUM_MARK = float('-inf')
    count = 0
    l_id = h_id = None 
    for line in file_handle:
        _, _, student_id, mark_str = line.strip().split(',')
        mark = float(mark_str)
        
        T_MARKS += mark 
        count += 1
        
        if mark < MINIMUM_MARK:
            MINIMUM_MARK = mark 
            l_id = student_id 
        if mark > MAXIMUM_MARK:
            MAXIMUM_MARK = mark 
            h_id = student_id 
    avg = T_MARKS / count if count > 0 else 0
    return l_id, h_id, avg
    
    
    

    