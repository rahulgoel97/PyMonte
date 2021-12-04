import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Simulation Variables
NUM_EXPERIMENTS = 100
NUM_TRIALS = 100

# Random Variables
bg = [0]*3
lg = [0]*3
ng = [0]*3
zg = [0]*3
bkg = [0]*3
var_set=[bg, lg, ng, zg, bkg]

# Experimental variables
exp_sum_means = []
exp_sum_25 = []
exp_sum_75 = []


for exp in range(NUM_EXPERIMENTS):

    # Variables to capture
    trial_sum_results = []

    # + == Simulation Universe ==+
    for trial in range(NUM_TRIALS):
    
        # This year
        bg[0] = 25.8
        lg[0] = 5.2
        ng[0] = 0.0
        zg[0] = 2.0
        bkg[0] = 8.2


        # Next eyar
        bg[1] = bg[0] * (1+np.random.triangular(-0.03, 0.02, 0.08,1)[0])
        lg[1] = np.random.normal(lg[0], 0.15*lg[0])
        ng[1] = random.choice([1,6.5, 2.5, 5, 6])
        zg[1] =2* random.choice([0,0,0,0,1,1,1,1,1,1])
        bkg[1]=bkg[0]-np.random.normal((bkg[0]*0.12), (bkg[0]*0.06))

        # Year after
        bg[2] = bg[1]* (1+np.random.triangular(-0.03, 0.02, 0.08, 1)[0])
        lg[2] = np.random.normal(lg[1], 0.15*lg[1])
        ng[2] = random.choice([1,6.5, 2.5, 5, 6])
        zg[2] = 2*random.choice([0,0,0,0,1,1,1,1,1,1])
        bkg[2] = bkg[1]-np.random.normal((bkg[1]*0.12), (bkg[1]*0.06))

        # Sum all variables
        sum = 0 
    
        for var in var_set:
            sum+=var[0]
            sum+=var[1]
            sum+=var[2]
    
        # Append to sum list
        trial_sum_results.append(sum)

    # Display the results
    print(f"Mean is {np.mean(trial_sum_results)} | Stdev is {np.std(trial_sum_results)}| 80%p is {np.percentile(trial_sum_results, 80)}")

    print("== Percentile Results ==")
    for percentile in range(0,100,10):
        print(f"{percentile}%: {np.percentile(trial_sum_results, percentile)}")

    # Add to experimental variable
    exp_sum_means.append(np.mean(trial_sum_results))
    exp_sum_25.append(np.percentile(trial_sum_results, 25))
    exp_sum_75.append(np.percentile(trial_sum_results, 75))

plt.hist(exp_sum_means)
plt.show()

