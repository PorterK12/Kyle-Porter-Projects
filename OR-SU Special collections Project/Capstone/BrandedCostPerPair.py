# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:44:22 2024

@author: porte
"""

import numpy as np
import matplotlib.pyplot as plt

# Data for branded cost per pair
regions = ['North America', 'Europe-Africa', 'Asia-Pacific', 'Latin America']
years = ['Y15', 'Y16', 'Y17', 'Y18', 'Y19']

branded_cost_data = {
    'North America': [33.88, 35.36, 32.32, 30.98, 29.65],
    'Europe-Africa': [36.07, 34.65, 34.08, 34.04, 30.69],
    'Asia-Pacific': [26.85, 26.12, 26.39, 26.08, 25.03],
    'Latin America': [26.08, 25.45, 26.58, 26.12, 25.3]
}

# Plotting the line graph
plt.figure(figsize=(10, 6))
for region in regions:
    plt.plot(years, branded_cost_data[region], marker='o', label=region)

plt.xlabel('Years')
plt.ylabel('Branded Cost per Pair')
plt.title('Branded Cost per Pair by Region Over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()