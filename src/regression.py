import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from year_dict import year_dict

def clean_data(df):
        df.iloc[:,[39,40,41]].fillna('None or Unspecified', inplace=True)
        y = df['SalePrice']
        # Create binary indicator features for missing values
        df['Missing_YearMade'] = df['YearMade'] == 1000
        df['Missing_MHCM'] = df['MachineHoursCurrentMeter'].isna()


        df['UsageBand'].fillna('None or Unspecified', inplace=True)
        df['fiModel'] = df['fiModelDesc'] + '-' +\
                        df['fiBaseModel'] + '-' + \
                        df['fiSecondaryDesc'].fillna('_') + '-' + \
                        df['fiModelSeries'].fillna('_').astype(str) + '-' + \
                        df['fiModelDescriptor'].fillna('_')

        




































