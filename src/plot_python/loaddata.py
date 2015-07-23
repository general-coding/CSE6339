'''
Created on Jul 20, 2015

@author: puneeth
'''

import csv
import pymysql

mydb = pymysql.connect(host='localhost',
                       user='root',
                       passwd='root',
                       db='hospital')
cursor = mydb.cursor()

with open('../6339_Dataset_1.csv') as csvfile:
    csv_data = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 1
    for row in csv_data:
        if count != 1:
            cursor.execute('INSERT INTO patient(AGE,SEX,RACE,DAY_OF_ADMISSION,DISCHARGE_STATUS,STAY_INDICATOR,DRG_CODE,LENGTH_OF_STAY,DRG_PRICE,TOTAL_CHARGES,COVERED_CHARGES,POA_DIAGNOSIS_INDICATOR_1,POA_DIAGNOSIS_INDICATOR_2,DIAGNOSIS_CODE_1,DIAGNOSIS_CODE_2,PROCEDURE_CODE_1,PROCEDURE_CODE_2,DISCHARGE_DESTINATION,SOURCE_OF_ADMISSION,TYPE_OF_ADMISSION,ADMITTING_DIAGNOSIS_CODE) values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")', row)
            print(row)
        count = count + 1

mydb.commit()
cursor.close()
print("Done")