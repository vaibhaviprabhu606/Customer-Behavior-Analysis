import pandas as pd
df=pd.read_csv('analysis_customer.py')
df.head(10)
df.info()
df.describe()
df.describe(include='all')
df.isnull().sum()
from numpy import median
df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
