import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulation variables
NUM_TRIALS  = 100

# Random variables
revenue = np.random.normal(1000, 175, NUM_TRIALS)
margin = np.random.normal(0.30, 0.05, NUM_TRIALS)
profit = revenue*margin

# Print out summary statistics
print(np.mean(profit))
print(np.median(profit))
print(np.std(profit))

# Plots
plt.plot(profit)
plt.show()
