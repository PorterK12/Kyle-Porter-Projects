# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:23:05 2024

@author: porte
"""

"""
Created on Mon Apr 29 20:34:52 2024

@author: porte
"""

import matplotlib.pyplot as plt

# Data
regions = ['North America', 'Europe-Africa', 'Asia-Pacific', 'Latin America']
years = [ 'Y15', 'Y16', 'Y17', 'Y18', 'Y19', 'Y20']

# Wholesale market share data
wholesale_market_share = {
    'North America': [ 14.60, 12.30, 13.00, 14.70, 19.20, 18.60],
    'Europe-Africa': [ 14.10, 12.00, 12.70, 14.90, 18.80, 17.30],
    'Asia-Pacific': [ 14.60, 12.60, 13.90, 20.40, 22.00, 20.70],
    'Latin America': [ 17.50, 12.90, 14.00, 21.20, 26.00, 26.00]
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