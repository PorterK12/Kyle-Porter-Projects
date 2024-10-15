# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:25:38 2024

@author: porte
"""

"""
Created on Tue Apr 16 22:46:34 2024

@author: porte
"""

import numpy as np
import matplotlib.pyplot as plt

# Data for Marketing per shoe
regions = ['North America Wholesale', 'Europe-Africa Wholesale',
           'Asia-Pacific Wholesale',  'Latin America Wholesale',
           'Market Average']

years = ['Y15', 'Y16', 'Y17', 'Y18', 'Y19', 'Y20']

marketing_data = {
    'North America Wholesale': [9.47, 9.87, 10.4, 13.58, 14.4, 13.62],
    'Europe-Africa Wholesale': [9.57, 10.86, 11.26, 14.66, 16.09, 15.42],
    'Asia-Pacific Wholesale': [9.86, 10.17, 10.65, 16.26, 14.3, 13.36],
    'Latin America Wholesale': [9.18, 10.22, 10.34, 15.65, 13.09, 12.43],
    'Market Average':[14.98, 16.57, 16.26, 17.23, 17.22, 17.130]
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