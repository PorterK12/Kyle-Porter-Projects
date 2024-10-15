# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:34:52 2024

@author: porte
"""

import matplotlib.pyplot as plt

# Data
regions = ['North America', 'Europe-Africa', 'Asia-Pacific', 'Latin America']
years = ['Y10', 'Y11', 'Y12', 'Y13', 'Y14', 'Y15', 'Y16', 'Y17', 'Y18', 'Y19', 'Y20']

# Wholesale market share data
wholesale_market_share = {
    'North America': [16.70, 15.60, 16.40, 15.80, 15.80, 14.60, 12.30, 13.00, 14.70, 19.20, 18.60],
    'Europe-Africa': [16.70, 15.70, 14.50, 10.20, 13.80, 14.10, 12.00, 12.70, 14.90, 18.80, 17.30],
    'Asia-Pacific': [16.70, 20.50, 18.80, 18.20, 16.40, 14.60, 12.60, 13.90, 20.40, 22.00, 20.70],
    'Latin America': [16.70, 19.80, 19.00, 17.80, 19.00, 17.50, 12.90, 14.00, 21.20, 26.00, 26.00]
}

# Plotting
plt.figure(figsize=(10, 6))

for region in regions:
    plt.plot(years, wholesale_market_share[region], marker='o', label=region)

plt.title('Wholesale Market Share by Region')
plt.xlabel('Year')
plt.ylabel('Market Share (%)')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)

plt.tight_layout()
plt.show()