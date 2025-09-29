'''
File: Load CSV Example
(based on code by Chris Piech)
----------------------
This is some sample code meant to both give
you some useful pieces to use on the assignment
and show you what some python code looks like.
'''

# A useful library for reading files
# with "comma-separated values".
import csv


def main():
    '''
    The main method (called at the bottom).
    '''
    prior = load_csv_data('prior.csv')
    print_data(prior)


def load_csv_data(filename):
    '''
    Reads in a 2D array of values separated by commas
    from a file (named filename). There are other ways
    to do this (numpy also has some useful functions
    for this), but this also shows you a bit about file
    reading in Python.
    '''
    matrix = []
    # open a file
    with open(filename) as f:
        reader = csv.reader(f)

        # loop over each row in the file
        for row in reader:

            # cast each value to a float
            float_row = []
            for value in row:
                float_row.append(float(value))

            # store the row into our matrix
            matrix.append(float_row)
    return matrix


def print_data(matrix):
    '''
    Prints out a 2D array.
    '''
    for row in matrix:
        print row


# This if statement passes if this was the file that was executed (allows you
# to import functions defined in this file without running it).
if __name__ == '__main__':
    main()
