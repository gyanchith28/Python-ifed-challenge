import time
import pandas as pd
import numpy as np

def forLoopCall(lst1, lst2):
    '''
    prints common elements from both list in arguments.
    
    For loop is used which takes one element from lst1 and checks whether it is in lst2. If yes, it appends to a empty list named verified_elements.
    
    PARAMETERS:
    -------------
    lst1 : list of strings
    lst2 : list of strings
    
    RETURNS:
    -------------
    NONE
    '''
    
    start = time.time() 
    verified_elements = []

    for element in lst1:
        if element in lst2:
            verified_elements.append(element)

    print(len(verified_elements))
    print('When using for loop, duration: {} seconds'.format(time.time() - start))

#Making a function to use intersect1d from numPy module
def numPyCall(lst1, lst2):
    '''
    prints common elements from both list in arguments.
    
    From numPy module we use intersect1d which provides the common element from both lists and are stored.
    
    PARAMETERS:
    -------------
    lst1 : list of strings
    lst2 : list of strings
    
    RETURNS:
    -------------
    NONE
    '''
    
    start = time.time()
    verified_elements = np.intersect1d(lst1, lst2)

    print(len(verified_elements))
    print('When using numpy, duration: {} seconds'.format(time.time() - start))

#Making a function to find intersection in the two given input.
def intersectCall(lst1, lst2):
    '''
    prints common elements from both list in arguments.
    
    We find intersection by converting both list to set and then stored.
    
    PARAMETERS:
    -------------
    lst1 : list of strings
    lst2 : list of strings
    
    RETURNS:
    -------------
    NONE
    '''
    start = time.time()
    verified_elements = set(lst1).intersection(set(lst2))

    print(len(verified_elements))
    print('While using set intersection, duration: {} seconds'.format(time.time() - start))

def main():
    with open('subset_elemets.txt') as f:
        subset_elements = f.read().split('\n')

    with open('all_elements.txt') as f:
        all_elements = f.read().split('\n')

    forLoopCall(subset_elements, all_elements)
    numPyCall(subset_elements, all_elements)
    intersectCall(subset_elements, all_elements)


if __name__ == "__main__":
    main()