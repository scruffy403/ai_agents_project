import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import gymnasium as gym

# Test numpy
array = np.array([1,2.3])
print("NumPy Array:", array)

# Test Pandas
df = pd.DataFrame({'A':[1,2,3], 'B':[4,5,6]})
print("Pandas DataFrame:\n", df)

# Test Matplotlib
plt.plot([1,2,3], [4,5,6])
plt.title("Test Plot")
plt.show()

# test skikit-learn
from sklearn.linear_model import LinearRegression
model = LinearRegression()
print("Scikit-learn Model:\n", model)

# Test gym
env = gym.make('CartPole-v1')
print("Environment Created:\n", env)