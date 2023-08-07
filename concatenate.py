# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 10:41:28 2022

@author: janle
"""

# Imports:
import pandas as pd
import matplotlib.pyplot as plt

# Dane:
biz_owners = pd.read_pickle("business_owners.p")
biz_owners = biz_owners.sort_values('last_name')

biz1 = biz_owners[biz_owners['title'] == 'PRESIDENT']
biz2 = biz_owners[biz_owners['title'] == 'SECRETARY']
biz3 = biz_owners[biz_owners['title'] == 'OTHER']

biz3 = pd.concat([biz1, biz2, biz3], keys=['pre', 'sec', 'oth'], verify_integrity=True)
# 'verify_integrity raises error if e.g. double values are present
# error exception handling should be of use here.
biz3.groupby(level=0).agg({'title': 'count'}).plot(kind='bar')

plt.show()
