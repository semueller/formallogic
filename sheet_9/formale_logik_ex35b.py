import numpy as np
from itertools import *

a = np.matrix('1 -1 -1; 0 1 1; 1 0 0') # Matrix A
b = np.matrix('1 0 1; 1 -1 0; -1 -1 -1') # Matrix B

one = np.matrix('1 0 0; 0 1 0; 0 0 1') # One Matrix for initialisation

matrixdict = {'A': a, 'B': b} # a dictionary to make the step from string-permutation to numpy-matrix easier

longest_combi = 30
found_one = False

for length in range(1, longest_combi): # iterate over all combination lenghts
    if found_one: # just some breaking condition so we do not calculate unneccesary complex
        break

    for permutation in product('AB', repeat=length): # iterate over all permutation of A and B with the length length
        akt = one # initialise matrix

        for element in permutation: # iterate over all elements in a single permutation
            akt = akt.dot(matrixdict[element]) # multiply the momentary element to the right of the momentary matrix

        if len(akt.nonzero()[0]) == 0: # if there are no nonzero elements, the whole matrix has to be zero, we found a match
            print(permutation,'\n', akt)
            found_one = True
            break
    print('Iteration', length, 'done!') # for