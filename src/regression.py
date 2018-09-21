import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from year_dict import year_dict

def clean_data(df):
        df.iloc[:,[39,40,41]].fillna('None or Unspecified', inplace=True)
        y = df['SalePrice']
        # Drop columns with potential data leakage
        df.drop(columns=['SaleID', 'SalePrice', 'datasource', 'auctioneerID'],
                inplace=True)
        # Create binary indicator feature if missing MachineHoursCurrentMeter
        df['Missing_MHCM'] == df['MachineHoursCurrentMeter'].isna()

        df['UsageBand'].fillna('None or Unspecified', inplace=True)
        df['fiModel'] = df['fiModelDesc'] + '-' +\
                        df['fiBaseModel'] + '-' + \
                        df['fiSecondaryDesc'].fillna('_') + '-' + \
                        df['fiModelSeries'].fillna('_').astype(str) + '-' + \
                        df['fiModelDescriptor'].fillna('_')

        




































