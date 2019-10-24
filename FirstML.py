#pip install quandl
#pip install sklearn
#pip install pandas
# regression
import pandas as pd 
import Quandl

Quandl.ApiConfig.api_key = 'oGyp1afZgdPkUpX_bNLA'
df = Quandl.get('FINRA/FORF_TLLTD')

print(df.head())