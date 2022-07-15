import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine
import csv

engine = create_engine('sqlite:///database.db', echo=True)

meta = MetaData()

data = Table(
   'data', meta,
   Column('id', Integer, primary_key=True),
   Column('station', String),
   Column('date', String),
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

with open("data.csv", 'r') as file:
    reader_obj = csv.reader(file)
    for row in reader_obj:
        ins = data.insert().values(id=row[0], 
                                   station=row[1], 
                                   date=row[2], 
                                   precip=row[3], 
                                   tobs=row[4], 
                                   latitude=row[5], 
                                   longitude=row[6], 
                                   elevation=row[7], 
                                   name=row[8], 
                                   country=row[9], 
                                   state=row[10]
                                   )
        conn = engine.connect()
        result = conn.execute(ins)
