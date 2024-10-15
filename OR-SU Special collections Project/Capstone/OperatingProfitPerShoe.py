# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 23:14:19 2024

@author: porte
"""

import numpy as np
import matplotlib.pyplot as plt

# Data for Operating profit per shoe
regions = ['North America Wholesale', 'North America Internet', 'Europe-Africa Wholesale', 'Europe-Africa Internet',
           'Asia-Pacific Wholesale', 'Asia-Pacific Internet', 'Latin America Wholesale', 'Latin America Internet']

years = ['Y15', 'Y16', 'Y17', 'Y18', 'Y19']

operating_profit_data = {
    'North America Wholesale': [12.15, 8.11, 9.92, 10.25, 11.46],
    'North America Internet': [23.79, 20.76, 21.52, 19.23, 16.45],
    'Europe-Africa Wholesale': [9.33, 11.19, 4.3, 4.75, 11.01],
    'Europe-Africa Internet': [21.87, 26.39, 14.74, 13.29, 16.63],
    'Asia-Pacific Wholesale': [13.35, 15.29, 7.03, 7.11, 11.41],
    'Asia-Pacific Internet': [26.2, 19.48, 16.83, 16.57, 19.51],
    'Latin America Wholesale': [31.16, 16.39, 9.95, 7.54, 11.46],
    'Latin America Internet': [16.41, 31.73, 20.1, 16.26, 18.82]
}

# Plotting the line graph
plt.figure(figsize=(12, 6))
for region in regions:
    plt.plot(years, operating_profit_data[region], marker='o', label=region)

plt.xlabel('Years')
plt.ylabel('Operating Profit per Shoe')
plt.title('Operating Profit per Shoe by Region Over Time')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.tight_layout()
plt.show()