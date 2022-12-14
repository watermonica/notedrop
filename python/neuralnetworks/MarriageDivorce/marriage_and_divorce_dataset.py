# -*- coding: utf-8 -*-
"""Marriage and Divorce Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tx6qio4PdpGhd-acmG-OD6bQ6JEkxrzK
"""

import numpy as np
import pandas as pd

import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import mplcyberpunk
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from imblearn.over_sampling import RandomOverSampler

df = pd.read_csv('/content/Marriage_Divorce_DB.csv', usecols=['Age Gap', 
'Divorce Probability'])

df.sort_values(by=['Divorce Probability'], inplace=True)

df.dropna(subset=['Age Gap', 
'Divorce Probability'])

df = df.rename(columns = {'Divorce Probability':'DP'})
df = df.rename(columns = {'Age Gap':'AG'})

df.loc[df.DP>1.5,'Outcome']=1
df.loc[df.DP<=1.5, 'Outcome']=0

print("likely to stay engaged: {}".format(len(df[df['Outcome'] == 0]))) #prints num of neg- patients
print("not likely to stay engaged: {}".format(len(df[df['Outcome'] == 1])))

x = df[df.columns[:-1]].values
y = df[df.columns[-1]].values

scalar = StandardScaler()

x = scalar.fit_transform(x)

over = RandomOverSampler()
x, y = over.fit_resample(x,y)
data = np.hstack((x, np.reshape(y, (-1, 1))))
transformed_df = pd.DataFrame(data, columns=df.columns)

x_train, x_temp, y_train, y_temp = train_test_split(x, y, test_size=0.4, random_state = 0)
x_valid, x_test, y_valid, y_test = train_test_split(x_temp, y_temp, test_size=0.5, random_state=0)

model = tf.keras.Sequential([
                              tf.keras.layers.Dense(32, activation='relu'), 
                              tf.keras.layers.Dense(32, activation='relu6'),
                              tf.keras.layers.Dense(32, activation='tanh'),
                              tf.keras.layers.Dense(1, activation="sigmoid")
])

model.compile(
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy']
)

model.evaluate(x, y)
model.evaluate(x_train, y_train)
model.evaluate(x_valid, y_valid)

history = model.fit(x_train, y_train, batch_size=16, epochs=20, validation_data=(x_valid, y_valid))

model.evaluate(x_test, y_test)

acc = history.history['accuracy']
loss = history.history['loss']

plt.figure(figsize=(12, 6))
plt.style.use('cyberpunk')
plt.subplot(1, 2, 1)
plt.plot(acc, label='Training Acc')
plt.title('Training Acc')
plt.legend()
mplcyberpunk.add_glow_effects()

plt.subplot(1, 2, 2)
plt.plot(loss, label='Training Loss')
plt.title('Training Loss')
plt.legend()
mplcyberpunk.add_glow_effects()
plt.show()

