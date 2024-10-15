# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:46:34 2024

@author: porte
"""

import numpy as np
import matplotlib.pyplot as plt

# Data for Marketing per shoe
regions = ['North America Wholesale', 'North America Internet', 'Europe-Africa Wholesale', 'Europe-Africa Internet',
           'Asia-Pacific Wholesale', 'Asia-Pacific Internet', 'Latin America Wholesale', 'Latin America Internet']

years = ['Y15', 'Y16', 'Y17', 'Y18', 'Y19']

marketing_data = {
    'North America Wholesale': [9.47, 9.87, 10.4, 13.58, 14.4],
    'North America Internet': [15.3, 15.99, 17.28, 23.01, 26.61],
    'Europe-Africa Wholesale': [9.57, 10.86, 11.26, 14.66, 16.09],
    'Europe-Africa Internet': [15.36, 16.82, 18.02, 23.93, 28.68],
    'Asia-Pacific Wholesale': [9.86, 10.17, 10.65, 16.26, 14.3],
    'Asia-Pacific Internet': [16.8, 19.48, 21.14, 28.47, 27.98],
    'Latin America Wholesale': [9.18, 10.22, 10.34, 15.65, 13.09],
    'Latin America Internet': [14.76, 18.05, 20.5, 26.96, 25.38]
}

# Plotting the line graph
plt.figure(figsize=(12, 6))
for region in regions:
    plt.plot(years, marketing_data[region], marker='o', label=region)

plt.xlabel('Years')
plt.ylabel('Marketing Cost per Shoe')
plt.title('Marketing Cost per Shoe by Region Over Time')
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.grid(True)
plt.tight_layout()
plt.show()