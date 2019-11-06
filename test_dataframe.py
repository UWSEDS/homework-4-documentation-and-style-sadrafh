""" Testing the Homwork 3 Module"""

import numpy as np
import hw3_module as hw3


#Testing the the types in  each column
def test_val():
    """ Testing the types of the values in each columns"""
    values = [type(i) for i in hw3.DF_HW['Fremont Bridge East Sidewalk']]
    assert values[222] == values[1]

#Testing whetehr there is any null value
def test_nan():
    """Testing whther there is any null value"""
    for j in list(hw3.DF_HW.columns):
        for i in range(len(hw3.DF_HW[j])):
            try:
                np.isnan(hw3.DF_HW[j][i])
            except TypeError:
                pass

#Testing the length of datafram
def test_len():
    """Testing  whether the  number of rows are less than 1"""
    rows = hw3.DF_HW.shape[0]
    try:
        rows > 1
        print('DataFrame has more than one row')
    except:
        print('DataFrame has less than one row')
