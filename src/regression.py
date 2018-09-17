import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from year_dict import year_dict

def clean_data(df):
        df.iloc[:,[39,40,41]].fillna('None or Unspecified', inplace=True)
        y = df['SalePrice']
        df.drop(columns=['SaleID', 'SalePrice', 'datasource', 'auctioneerID'],
                inplace=True)
        df['Missing_MHCM'] == df['MachineHoursCurrentMeter'].isna()
        df['MachineHoursCurrentMeter'].fillna(0, inplace=True)
        df['UsageBand'].fillna('None or Unspecified', inplace=True)
        df['fiModel'] = df['fiModelDesc'] + '-' +\
                        df['fiBaseModel'] + '-' + \
                        df['fiSecondaryDesc'].fillna('_') + '-' + \
                        df['fiModelSeries'].fillna('').astype(str) + '-' + \
                        df['fiModelDescriptor'].fillna('')
        df.drop(columns=['fiModelDesc',
                        'fiBaseModel',
                        'fiSecondaryDesc',
                        'fiModelSeries',
                        'fiModelDescriptor'])


        for model in s:
                mask = (df.loc[:,'ModelID']==model)&(df.loc[:,'YearMade']==1000)
                df.loc[mask, 'YearMade'] = 1000
        




































