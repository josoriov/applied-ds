# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
conc_path = 'concentration.csv'
gdp_path = 'gdp.csv'
reg_path = 'regions.csv'

concentration = pd.read_csv(conc_path)
gdp = pd.read_csv(gdp_path)
regions = pd.read_csv(reg_path)

del(conc_path, gdp_path, reg_path)

# %%
concentration = concentration.merge(regions, how='left', left_on=['region_id'], right_on=['region_id'])