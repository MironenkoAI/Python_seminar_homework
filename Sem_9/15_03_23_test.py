# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
df = pd.read_csv("california_housing_test.csv")

df.shape

df.dtypes

df.isnull().sum()

# df[df['median_income'] < 2]['median_house_value']
df.loc[df['median_income'] < 2, 'median_house_value']

df[['longitude', 'latitude']]

df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)]

print(df['median_house_value'].max())
print(df['median_house_value'].min())

# Показать максимальное median_house_value, где
# median_income = 3.1250

print(df.loc[df['median_income']==3.1250, 'median_house_value'].max())

