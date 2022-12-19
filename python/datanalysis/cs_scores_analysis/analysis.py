from gettext import npgettext

import numpy as np
import pandas as pd

df = pd.read_csv('scores.csv', usecols=['Python', 'Sql', 'ML', 'Student Placed'])

passed = len(df[df['Student Placed'] == 'Yes'])
failed = len(df[df['Student Placed'] == 'No'])

pythonp, sqlp, mlp = 0, 0, 0
pythonf, sqlf, mlf = 0, 0, 0

passed_array, failed_array = [], []
np_array = np.array(df.values)

for i in range(len(np_array)):
    if np_array[i][-1] == 'Yes':
        passed_array.append(np_array[i])

    else:
        failed_array.append(np_array[i])

for x in passed_array:
    pythonp += float(x[0])
    sqlp += float(x[1])
    mlp += float(x[2])


for y in failed_array:
    pythonf += float(y[0])
    sqlf += float(y[1])
    mlf += float(y[2])


def display_pass():
    print('\nAverage Passed Python Score: {}'.format(pythonp/passed))
    print('Average Passed SQL Score: {}'. format(sqlp/passed))
    print('Average Passed ML Score: {}'. format(mlp/passed))

def display_failed():
    print('\nAverage Failed Python Score: {}'.format(pythonf/failed))
    print('Average Failed SQL Score: {}'. format(sqlf/failed))
    print('Average Failed ML Score: {}'. format(mlf/failed))

def display_dif():
    pydif = abs(float((pythonp/passed) - (pythonf/failed)))
    sqldif = abs(float((sqlp/passed) - (sqlf/failed)))
    mldif = abs(float((mlp/passed) - (mlf/failed)))

    print('\nPython Difference in Score: {}'.format(pydif))
    print('SQL Difference in Score: {}'.format(sqldif))
    print('ML Difference in Score: {}'.format(mldif))

display_pass()
display_failed()
display_dif()


