import pandas as pd
import os 
from sqlalchemy import create_engine
import logging
import time
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a" #this is appending the files
)

engine = create_engine('sqlite:///inventory.db')
#making a function for ingestion
#This is done to ensure scripting and not just a plain notebook as that doesnt dictate a real world office like scenario
#the script will have to be scheduled
def ingest_db(df, table_name, engine):
    '''This function will ingest the dataframe into the database table'''
    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)
    
def load_raw_data():
    '''this function will load the CSVs as dataframe and ingest into db'''
    start = time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df = pd.read_csv('data/'+file)
        logging.info(f'Ingesting {file} in db')
        ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end - start)/60
    
    logging.info('-----------Ingestion complete-----------')
    logging.info(f'\n Total time taken: {Total_time} minutes')
    
if __name__ == '__main__':
    load_raw_data()