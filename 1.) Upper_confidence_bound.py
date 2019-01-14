#upper confidence bound

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

#importing data
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")

#implementing UCB
N = 10000
d = 10
ads_selected = []
numbers_of_selections = [0] * d
sums_of_rewords = [0] * d
total_reward = 0
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if numbers_of_selections[i] > 0:
            average_reword = sums_of_rewords[i]/numbers_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n+1) / numbers_of_selections[i])
            upper_bound = average_reword + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    numbers_of_selections[ad] = numbers_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    sums_of_rewords[ad] = sums_of_rewords[ad] + reward
    total_reward = total_reward + reward

print(total_reward)
print(sums_of_rewords)

#visualizing the results
plt.hist(ads_selected)
plt.title("Histogram of selected ads")
plt.xlabel('Ads')
plt.ylabel('Number of times the ad was selected')
plt.show()