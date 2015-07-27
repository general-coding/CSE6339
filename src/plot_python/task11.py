'''
Created on Jul 22, 2015

@author: puneeth
'''

import pandas
from collections import Counter

df = pandas.read_csv('../6339_Dataset_1.csv')


# print(df.columns.values)

d_c_a = df[['DIAGNOSIS_CODE_1', 'AGE']].groupby(['DIAGNOSIS_CODE_1', 'AGE'],
                                                    as_index=True, sort=True)['DIAGNOSIS_CODE_1'].count()

d_c_b = df[['DIAGNOSIS_CODE_2', 'AGE']].groupby(['DIAGNOSIS_CODE_2', 'AGE'],
                                                    as_index=True, sort=True)['DIAGNOSIS_CODE_2'].count()

# print(d_c_a)
dicta = d_c_a.to_dict()
# print(dicta)

# print(d_c_b)
dictb = d_c_b.to_dict()
# print(dictb)

A = Counter(dicta)
B = Counter(dictb)
# print(A + B)
count = A + B
# print(count)
# print(count.most_common())
top_count = count.most_common()
# print(top_count)
age_list_1 = ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
age_list_2 = ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
age_list_3 = ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
for i in top_count:
#     print(i)
    diag_age, diag_count = i
    diag, age = diag_age
#     if age_list_1[int(age) - 1] == 'F':
#         age_list_1[int(age) - 1] = 'T'
#         print('top 1 diagnosis', diag, ' for ', age, ' with count ', diag_count)
#     
#     elif age_list_2[int(age) - 1] == 'F':
#         age_list_2[int(age) - 1] = 'T'
#         print('top 2 diagnosis', diag, ' for ', age, ' with count ', diag_count)
#         
#     elif age_list_3[int(age) - 1] == 'F':
#         age_list_3[int(age) - 1] = 'T'
#         print('top 3 diagnosis', diag, ' for ', age, ' with count ', diag_count)

    if (diag != ' '):
        print('diagnosis', diag, ' for ', age, ' with count ', diag_count)
    
# print(count)
# a = list(count.elements())
# a.sort()
# print(a)

# for key, value in count.items():
#     print(key, value)