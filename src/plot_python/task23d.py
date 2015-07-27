'''
Created on Jul 26"," 2015

@author: puneeth
'''

from matplotlib import pyplot
import numpy
from numpy import ndarray

data = numpy.genfromtxt('../6339_Dataset_1.csv', delimiter=',', skiprows=1)
print(data)
ndarray.sort(data, order=[8])

drg = data[:, 8]
total_charges = data[:, 9]

pyplot.plot(drg, total_charges, '-')
pyplot.title('DRG_PRICE vs TOTAL_CHARGES')
pyplot.xlabel('DRG_PRICE')
pyplot.ylabel('TOTAL_CHARGES')
pyplot.show()
pyplot.clf()
