'''
Created on Jul 20, 2015

@author: puneeth
'''

from matplotlib import pyplot
import numpy

data = numpy.genfromtxt('../6339_Dataset_1.csv', delimiter=',', skiprows=1)
lof = data[:, 7]
total_cost = data[:,9]

pyplot.plot(lof, total_cost, '.')
pyplot.title('Length of Stay vs The Total Cost')
pyplot.xlabel('Length of Stay')
pyplot.ylabel('The Total Cost')
pyplot.show()
pyplot.clf()