### Made by
# Samuel Nellessen s1102282
# Rebecca Kruschka s1054733

import numpy as np

def sum_even_rec(n : int) -> int: 
    """
    Recursively calculates the sum of all even numbers from 0 to n.

    Parameters
    ----------
    n : int
        The upper bound of the range (inclusive).

    Returns
    -------
    int
        The sum of even numbers from 0 to n. 
        
    Notes
    -----
    The function handles negative values by returning 0. For positive values, it 
    recursively adds even numbers, decrementing by 2 if n is even, or by 1 if n is odd.
    """
    
    if n <= 0:
        return 0
    else:
        if n % 2 == 0:
            x = n + sum_even_rec(n-2)
            return x
        else:
            x = sum_even_rec(n-1)
            return x
    
def array_product_rec(numbers : np.ndarray[int]) -> int: 
    """
    Recursively calculates the product of elements in a numpy array.

    Parameters
    ----------
    numbers : np.ndarray[int]
        An array of integers whose product is to be calculated.

    Returns
    -------
    int
        The product of all elements in the array.
        
    Notes
    -----
    The base case is when the array has only one element. The function multiplies 
    the first element with the product of the remaining array elements.
    """
    # Base case:
    if numbers.shape[0] == 1:
        return numbers[0]
    else:
        return numbers[0] * array_product_rec(numbers[1:])

    
def concat_rec(words : list[str]) -> str:
    """
    Recursively concatenates a list of strings into a single string, separated by spaces.

    Parameters
    ----------
    words : list[str]
        A list of strings to be concatenated.

    Returns
    -------
    str
        A single string formed by concatenating all strings in `words`, separated by spaces.
        
    Notes
    -----
    The base case is when the list contains only one string. The function concatenates 
    the first string with the result of recursively concatenating the rest of the list.
    """
    if len(words) == 1:
        return words[0]
    else:
        return words[0] + " " + concat_rec(words[1:])
        
def half_christmas_tree_rec(height : int) -> str: 
    
    """
    Recursively generates a string representation of a half-Christmas tree.

    Parameters
    ----------
    height : int
        The height of the Christmas tree.

    Returns
    -------
    str
        A string representing a half-Christmas tree of the given height.
        
    Notes
    -----
    Each level of the tree has a number of asterisks (*) equal to its level number. 
    The base case is a single asterisk. The function builds the tree from top to bottom.
    """
    
    
    if height == 1:
        return "*"
    else:
        return half_christmas_tree_rec(height-1) + "\n" + height * "*"
    
def find_max(llist : list[int]) -> int:

    max_value = llist.pop()
    
    for value in llist:
        if value>max_value:
            max_value = value
            
    return max_value

def find_max_rec(llist : list[int]) -> int:
    """
    Recursively finds the maximum value in a list of integers.

    Parameters
    ----------
    llist : list[int]
        A list of integers.

    Returns
    -------
    int
        The maximum integer in the list.
        
    Notes
    -----
    The base case is when the list has only one element. The function compares the 
    first element with the maximum of the rest of the list (found recursively).
    """
    if len(llist) == 1:
        return llist[0]
    
    else:
        if llist[0] > find_max_rec(llist[1:]):
            return llist[0]
        else:
            return find_max_rec(llist[1:])