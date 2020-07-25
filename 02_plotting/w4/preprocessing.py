# -*- coding: utf-8 -*-
import pandas as pd

filepath = '../data/Original/calidad_aire_2011_2018.csv'

# %% Getting the cols index to be imported
cols_import_names = ['Fecha', 'Código del departamento', 'Departamento', 'Variable',
                     'Unidades', 'Concentración']
cols_original = list(pd.read_csv(filepath, nrows=1).
                     columns.values)
cols_import = [cols_original.index(i) for i in cols_import_names]
cols_names = ['date', 'region_id', 'region', 'variable', 'units', 'concentration']
del(cols_import_names, cols_original)

# %%
date = []
region_id = []
region = []
variable = []
units = []
concentration = []

chunksize = 50000
for chunk in pd.read_csv(filepath, usecols=cols_import, names=cols_names,header=0, chunksize=chunksize):
    chunk = chunk[(chunk['variable'] == 'PM10')]
    date.extend(list(chunk['date'].values))
    region_id.extend(list(chunk['region_id'].values))
    region.extend(list(chunk['region'].values))
    variable.extend(list(chunk['variable'].values))
    units.extend(list(chunk['units'].values))
    concentration.extend(list(chunk['concentration'].values))
del(chunk, chunksize)
# %% 
    
air_quality = pd.DataFrame(list(zip(date, region_id, region, variable, units, concentration)), 
               columns=cols_names)
del(date, region_id, region, variable, units, concentration)
# %%
air_quality['date'] = pd.to_datetime(air_quality['date'])
air_quality['year'] = air_quality['date'].dt.year
air_quality = air_quality[air_quality['year'] < 2017]

# %%
air_quality.to_csv('../data/Generated/air_quality.csv', index=False)