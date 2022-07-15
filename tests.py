import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///database.db', echo=True)

meta = MetaData()

data = Table(
   'data', meta,
   Column('id', Integer, primary_key=True),
   Column('station', String),
   Column('precip', String),
   Column('tobs', String),
   Column('latitude', String),
   Column('longitude', String),
   Column('elevation', String),
   Column('name', String),
   Column('country', String),
   Column('state', String)      
)

meta.create_all(engine)
print(engine.table_names())

with open("data.csv", 'r') as file:
    data_df = pd.read_csv(file)
data_df.to_sql('data', con=engine, index=True, index_label='id', if_exists='replace')