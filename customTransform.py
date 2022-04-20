from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.impute import MissingIndicator
import numpy as np
import pandas as pd
from scipy import sparse as sp

class quarterly_agg(TransformerMixin, BaseEstimator):
    """takes in a time-series format and transforms by time
    """

    def __init__(self, *, missing_values=np.nan, add_indicator=False):
        self.missing_values = missing_values
        self.add_indicator = add_indicator

    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y):
        
        recession_vs_yield = pd.DataFrame(X).concat(pd.Series(y), axis = 1)
        recession_vs_yield = recession_vs_yield.set_index(pd.DatetimeIndex(recession_vs_yield.index))


        #Generate the different features
        data_mean = recession_vs_yield.resample('Q-JAN', convention='end').agg('mean')
        data_mean['USREC'] = data_mean['USREC'].apply(lambda x: 1 if x > 0 else 0)
        data_std = recession_vs_yield.resample('Q-JAN', convention='end').agg('std').drop(columns = ['USREC'])
        # data_max = recession_vs_yield.resample('Q-JAN', convention='end').agg('max').drop(columns = ['USREC'])
        # data_min = recession_vs_yield.resample('Q-JAN', convention='end').agg('min').drop(columns = ['USREC'])
        data_spread = recession_vs_yield.resample('Q-JAN', convention='end').agg('max') - recession_vs_yield.resample('Q-JAN', convention='end').agg('min')
        data_spread = data_spread.drop(columns = ['USREC']).add_suffix('_split')

        #Merge them features
        data = pd.merge_asof(data_mean,data_std, left_index = True, right_index = True, suffixes = ('_mean','_std'))
        data = pd.merge_asof(data,data_spread, left_index = True, right_index = True)
        data = data.iloc[1:-1 , :]
        data['USREC'] = data['USREC'].shift(periods = -1)
        data = data.iloc[:-1,:]
        X = data.drop(columns=['USREC'])
        y = data['USREC']

        return X,y