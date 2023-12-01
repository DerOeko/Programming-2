#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### Made by
# Samuel Nellessen s1102282
# Rebecca Kruschka s1054733

import numpy as np
import random as rnd

# maybe you need to install matplotlib
# pip install matplotlib
import matplotlib.pyplot as plt 


def random_array(a: int, b: int, n: int):
    """
    Generate an array of n random integers between a and b (inclusive).

    Parameters
    ----------
    a : int
        Lower bound for random integers (inclusive).
    b : int
        Upper bound for random integers (inclusive).
    n : int
        Number of random integers to generate.

    Returns
    -------
    np.ndarray
        An array of n random integers between a and b.
    """
    
    if a > b:
        array = np.random.randint(b, a + 1, size = n, dtype = np.uint32)
    else:
        array = np.random.randint(a, b + 1, size = n, dtype = np.uint32)
    

    return array



def element_mult(x: np.ndarray, y: np.ndarray):
    
    """
    Multiply two arrays element-wise.

    Parameters
    ----------
    x : np.ndarray
        First array for element-wise multiplication.
    y : np.ndarray
        Second array for element-wise multiplication.

    Returns
    -------
    np.ndarray or None
        An array containing the element-wise product of `x` and `y`. 
        Returns `None` if the lengths of `x` and `y` do not match.
    """
    
    if len(x) != len(y):
        return None
    else:
        z = []
        for i in range(len(x)):
            z.append(x[i] * y[i]) 
            
    return np.asarray(z)


def find_max(x: np.ndarray):
    """
    Find the index of the maximum element in a non-negative array.

    Parameters
    ----------
    x : np.ndarray
        Array in which to find the index of the maximum element.

    Returns
    -------
    int or None
        Index of the maximum element in `x`. Returns `None` if any element in `x` is negative.
    """
    
    for n in x:
        if n < 0:
            return None
    max_number = x[0]
    max_index = 0
    for i in range(len(x)):
        if x[i] >= max_number:
            max_index = i
            max_number = x[i]       
    
    return max_index


    
def transpose(x: np.ndarray):
    """
    Transpose a 2D numpy array.

    Parameters
    ----------
    x : np.ndarray
        A 2D numpy array to transpose.

    Returns
    -------
    np.ndarray
        The transposed array.
    """
    
    y = np.zeros((x.shape[1], x.shape[0]), dtype = int)

    for row in range(x.shape[0]):
        for col in range(x.shape[1]):
            y[col, row] = x[row, col]    
    return y

def is_square(x: np.ndarray):
    """
    Check if a numpy array is square (i.e., has the same number of rows and columns).

    Parameters
    ----------
    x : np.ndarray
        Array to check.

    Returns
    -------
    bool
        `True` if `x` is a square array, `False` otherwise.
    """
    if len(x.shape) == 1:
        if len(x) == 1:
            return True
        else:
            return False
        
    for i in range(len(x.shape)):
        if x.shape[i] != x.shape[0]:
            return False

    return True

    
def is_magic(x: np.ndarray):
    """
    Check if a 2D square numpy array is a magic square.

    A magic square is a square grid filled with distinct integers such that
    the sum of the numbers in each row, column, and both main diagonals is the same.

    Parameters
    ----------
    x : np.ndarray
        A 2D numpy array to check.

    Returns
    -------
    bool or None
        `True` if `x` is a magic square, `False` otherwise. 
        Returns `None` if `x` is not a 2D square array.
    """
    
    if len(x.shape) != 2 or not is_square(x):
        return None
    
    row_sum = x[0, :].sum()

    # row check
    
    for i in range(x.shape[0]):
        if row_sum != x[i, :].sum():
            return False
    
    # column check
    
    for i in range(x.shape[1]):
        if row_sum != x[:, i].sum():
            return False
        
    # descending diag check
    diag_sum = 0
    
    for col in range(x.shape[1]):
        diag_sum += x[col, col]
    
    if diag_sum != row_sum:
        return False
    
    diag_sum = 0
    
    for i in range(x.shape[1]):
        diag_sum += x[0+i, x.shape[0]-1-i]
        
    if diag_sum != row_sum:
        return False
    
    
    return True
    
    
def main():
    """
    Main function demonstrating the use of various array operations.

    This function demonstrates the generation of a random array, finding the index
    of its maximum value, checking for magic squares, and basic plotting using matplotlib.
    """
    
    x = np.arange(10)
    
    try:
        # if your functions are working properly, you can implement changes in 
        # main() here
        
        y = random_array(0, 100, 10)
        # imax = find_max(y)
        mean = np.mean(y)
    
        plt.plot(x, y, 'ko-')
        i, = np.where(y>mean)
        plt.plot(i, y[i], 'ro')
    except:
        
        # if your functions are not working properly, you can implement changes
        # in main() here:
            
        y = np.arange(100).reshape((4,25)).T.flatten()[0:10]
        imax = 7
        plt.plot(x, y, 'ko-')
        plt.plot(x[imax], y[imax], 'ro')
            
    
    # Example of magic matrix
    x = np.array([[2,7,6],[9,5,1],[4,3,8]])        
    print(x)
    
    return None
    

# The main body of your program should only call the main() function like this:
if __name__=="__main__":    
    main()
    
    
