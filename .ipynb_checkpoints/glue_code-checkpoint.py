import sys
import pandas as pd

def create_features(df):
    """
    Create time series features based on time series index.
    """
    df = df.copy()
    df['hour'] = df.index.hour
    df['minute'] = df.index.minute
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['day'] = df.index.month
    df['year'] = df.index.year
    df['season'] = df['month'] % 12 // 3 + 1
    df['dayofyear'] = df.index.dayofyear
    df['dayofmonth'] = df.index.day
    df['weekofyear'] = df.index.isocalendar().week
    return df.astype(float)

source_path = 's3://lambton-power-consumption-project/raw/data.csv'
df = pd.read_csv(source_path)
df.columns = ['_'.join(list(filter(None, col.lower().split(' ')))) for col in df.columns]
df = df.set_index('datetime')
df.index = pd.to_datetime(df.index)
df = create_features(df)
df.to_csv('s3://lambton-power-consumption-project/processed/data.csv')