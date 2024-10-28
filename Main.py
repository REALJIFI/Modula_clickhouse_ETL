from helpers import get_client, get_postgres_engine 
from Extract import fetch_data
from load import load_csv_to_postgres
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from datetime import datetime, timedelta

client = get_client()
engine = get_postgres_engine()

### modification for getting max_date from staging table
# this code will check the last loaded date before running a new date in the pipeline

session = sessionmaker(bind=engine)
session =session()
result = session.execute(text('select max(pickup_date) from "STG".tripdata'))
max_date = result.fetchone()[0] 
session.close()

## getting the new date
new_date = (datetime.strptime(max_date, '%Y-%m-%d') + timedelta(days=1)).date()

query = f'''
        select pickup_date,vendor_id, passenger_count,trip_distance,fare_amount,payment_type, tip_amount  
        from tripdata
        where pickup_date = toDate('{max_date}') + 1
        '''


def main():
    '''
    main function to run the data pipeline module
    1 Extract data from url  
    2 fetch data from source file
    3 load data from modular function to a secure database

    parameters: None

    Returns: None
    
    '''

    # Extract data
    fetch_data(client=client, query=query)

    #load data 
    load_csv_to_postgres('tripdata.csv', 'tripdata', engine, 'STG')

# this function will only work after setting it up in pgadmin
    # execute stored procedure
    session = sessionmaker(bind=engine)
    session =session()
    session.execute(text('CALL "STG".agg_tripdata()'))
    session.commit()

    print('stored procedure executed')

    print(f'pipeline executed successfully for {new_date}')

if __name__ == '__main__':
    main()