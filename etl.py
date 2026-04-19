import pandas as pd
import requests
from db import get_engine
from config import API_URL

def extract():
    response = requests.get(API_URL)
    return pd.DataFrame(response.json())

def transform(df):
    df = df.dropna()
    df['title_length'] = df['title'].apply(len)
    return df

def load(df):
    engine = get_engine()
    df.to_sql("jobs_data", engine, if_exists="replace", index=False)

def run_etl():
    df = extract()
    df = transform(df)
    load(df)
