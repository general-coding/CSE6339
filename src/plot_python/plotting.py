'''
Created on Jul 20, 2015

@author: puneeth
'''

from matplotlib import pyplot
import csv

def q2():
    sex = []
    discharge_status = []
    
    
    pyplot.plot_date(sex, discharge_status, '*')
    pyplot.title('in-hospital mortality of men and women')
    pyplot.xlabel('Sex 1-male, 2-female')
    pyplot.ylabel('A-patient discharged alive B-patient discharged dead')
    pyplot.savefig('mortality.pdf', dpi=100)
#     pyplot.show()
    pyplot.clf()

q2()
