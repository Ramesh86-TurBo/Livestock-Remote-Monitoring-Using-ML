import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# distribution of features

df = pd.read_csv('final3.csv')

# plt.figure(figsize=(16, 5))  # Fix the typo here (flagsize to figsize)

# plt.subplot(1, 3, 1)  # Updated to 1 row, 3 columns
# sns.distplot(df['x'])

# plt.subplot(1, 3, 2)
# sns.distplot(df['y'])

# plt.subplot(1, 3, 3)
# sns.distplot(df['z'])

# plt.show()

# numerics
# print("mean: ")
# print("mean value of x: ", df['x'].mean())
# print("mean value of y: ", df['y'].mean())
# print("mean value of z: ", df['z'].mean())

# print("std: ")
# print("std value of x: ", df['x'].std())
# print("std value of y: ", df['y'].std())
# print("std value of z: ", df['z'].std())

# print("min: ")
# print("min value of x: ", df['x'].min())
# print("min value of y: ", df['y'].min())
# print("min value of z: ", df['z'].min())

# print("max: ")
# print("max value of x: ", df['x'].max())
# print("max value of y: ", df['y'].max())
# print("max value of z: ", df['z'].max())


# setting threshold
# print("highest allowed: ", df['x'].mean() + 3*df['x'].std())
# print("lower allowed: ", df['x'].mean() - 3*df['x'].std())

# print("highest allowed: ", df['y'].mean() + 3*df['x'].std())
# print("lower allowed: ", df['y'].mean() - 3*df['x'].std())

# print("highest allowed: ", df['z'].mean() + 3*df['x'].std())
# print("lower allowed: ", df['z'].mean() - 3*df['x'].std())

# calculating the z-score
df['z_score_x'] = (df['x'] - df['x'].mean())/df['x'].std()
df['z_score_y'] = (df['y'] - df['y'].mean())/df['y'].std()
df['z_score_z'] = (df['z'] - df['z'].mean())/df['z'].std()

print(df.head())



