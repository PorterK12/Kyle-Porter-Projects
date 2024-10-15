# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 12:22:23 2024

@author: porte
"""

import matplotlib.pyplot as plt

# Years
years = ['Y17', 'Y18', 'Y19']

# Data for each region
regions = ['North America', 'Latin America', 'Asia-Pacific', 'Europe-Africa']
data = {
    'North America': [13.00, 14.70, 19.20],
    'Latin America': [14.00, 21.20, 26.00],
    'Asia-Pacific': [13.90, 20.40, 22.00],
    'Europe-Africa': [12.70, 14.90, 18.80]
}

# Plotting the graph
plt.figure(figsize=(10, 6))

for region in regions:
    plt.plot(years, data[region], label=region)

# Labeling the points

plt.title(' Wholesale Market Share Growth (Y17-Y18) by Region')
plt.xlabel('Year')
plt.ylabel('Market Share (%)')
plt.legend()
plt.grid(True)
plt.show()

