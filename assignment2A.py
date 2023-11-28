#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random as rnd

# maybe you need to install matplotlib
# pip install matplotlib
import matplotlib.pyplot as plt 


def random_array(a: int, b: int, n: int):
    """
    DESCRIPTION

    Parameters
    ----------
    a: int
        DESCRIPTION.
    b: int
        DESCRIPTION.
    n: int
        DESCRIPTION.

    Returns
    -------
    random_array: int
        DESCRIPTION.

    """
    if a > b:
        array = rnd.randint(b, a + 1, size = n)
    else:
        array = rnd.randint(a, b+1, size= n)
    

    return array



def element_mult(x: np.ndarray, y: np.ndarray):
    if len(x) != len(y):
        return None
    else:
        z = []
        for i in range(len(x)):
            z.append(x[i] * y[i]) 
            
    return None


def find_max(x: np.ndarray):
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
    y = np.zeros((x.shape[1], x.shape[0]), dtype = int)

    for row in range(x.shape[0]):
        for col in range(x.shape[1]):
            y[col, row] = x[row, col]    
    return y

def is_square(x: np.ndarray):
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
    Main function
    """
    x = np.arange(10)
    
    try:
        # if your functions are working properly, you can implement changes in 
        # main() here
        
        y = random_array(0, 100, 10)
        imax = find_max(y)
        plt.plot(x, y, 'ko-')
        plt.plot(x[imax], y[imax], 'ro')
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
    
    
