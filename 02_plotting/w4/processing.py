# -*- coding: utf-8 -*-
import pandas as pd

filepath = 'air_quality.csv'

# %%
air_quality = pd.read_csv(filepath)
air_quality['region_id'] = air_quality['region_id'].astype(int) 
# %% Creating a regions dataframe
regions = air_quality['region']+';'+air_quality['region_id'].astype(str)
regions = regions.unique()
regions = pd.DataFrame(regions, columns=['comb'])
regions['region'] = regions.apply(lambda row: row['comb'].split(sep=';')[0], axis=1)
regions['region_id'] = regions.apply(lambda row: int(float(row['comb'].split(sep=';')[1])), axis=1)
regions.drop(labels=['comb'], inplace=True, axis=1)
regions.set_index(['region_id'], inplace=True)
regions.sort_index(inplace=True)

# %%
concentration = (air_quality.groupby(['region_id', 'year', 'variable'])['concentration'].mean())
concentration.to_csv('concentration.csv')

# %%
conc_path = 'concentration.csv'
gdp_path = '../data/PIB_2010_2016.csv'
reg_path = 'regions.csv'

concentration = pd.read_csv(conc_path)
regions = pd.read_csv(reg_path)
gdp = pd.read_csv(gdp_path, nrows=34)

# %%
to_drop = [str(i) for i in range(2000,2011)]
col_names = ['region'] + [str(i) for i in range(2011, 2017)]
gdp.drop(labels=[0], inplace=True, axis=0)
gdp.drop(labels=to_drop, inplace=True, axis=1)
gdp.columns = col_names
gdp['region'] = gdp.apply(lambda row: row['region'].upper(), axis=1)
gdp = (gdp.replace(to_replace='NORTE SANTANDER', value='NORTE DE SANTANDER').
       replace(to_replace='VALLE', value='VALLE DEL CAUCA'))
del(to_drop, col_names, conc_path, gdp_path, reg_path)

# %%

gdp = regions.merge(gdp, how='left', left_on=['region'], right_on=['region'])
gdp.to_csv('gdp.csv', index=False)