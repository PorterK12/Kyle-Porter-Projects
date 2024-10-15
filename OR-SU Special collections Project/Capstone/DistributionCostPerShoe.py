# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:56:36 2024

@author: porte
"""

import numpy as np
import matplotlib.pyplot as plt

# Data for Distribution
regions = ['North America', 'Europe-Africa', 'Asia-Pacific', 'Latin America']
years = ['Y15', 'Y16', 'Y17', 'Y18', 'Y19']

distribution_data = {
    'North America': [7.48, 7.31, 8.21, 9.96, 10.86],
    'Europe-Africa': [8.89, 7.29, 7.93, 7.86, 9.56],
    'Asia-Pacific': [4.84, 4.08, 4.43, 6.22, 6.06],
    'Latin America': [5.56, 4.74, 5.59, 6.32, 6.1]
}

# Plotting the line graph
plt.figure(figsize=(10, 6))
for region in regions:
    plt.plot(years, distribution_data[region], marker='o', label=region)

plt.xlabel('Years')
plt.ylabel('Distribution Cost Per Shoe')
plt.title('Distribution Cost Per Shoe by Region Over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
