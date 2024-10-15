# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:31:09 2024

@author: porte
"""

import matplotlib.pyplot as plt

# Data
regions = ['North America', 'Europe-Africa', 'Asia-Pacific', 'Latin America']
years = ['Y10', 'Y11', 'Y12', 'Y13', 'Y14', 'Y15', 'Y16', 'Y17', 'Y18', 'Y19', 'Y20']

# Internet market share data
internet_market_share = {
    'North America': [16.70, 13.50, 16.00, 16.00, 14.50, 14.00, 12.30, 13.60, 16.40, 23.30, 20.20],
    'Europe-Africa': [16.70, 15.60, 16.90, 18.90, 17.00, 15.60, 12.80, 13.80, 18.30, 25.10, 22.10],
    'Asia-Pacific': [16.70, 18.60, 16.40, 16.30, 17.70, 16.70, 12.00, 12.70, 23.50, 23.60, 22.90],
    'Latin America': [16.70, 20.20, 18.20, 18.70, 20.50, 18.90, 13.00, 14.40, 25.00, 26.10, 23.70]
}

# Plotting
plt.figure(figsize=(10, 6))

for region in regions:
    plt.plot(years, internet_market_share[region], marker='o', label=region)

plt.title('Internet Market Share by Region')
plt.xlabel('Year')
plt.ylabel('Market Share (%)')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)

plt.tight_layout()
plt.show()