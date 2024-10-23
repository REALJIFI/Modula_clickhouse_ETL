from helpers import get_client, get_postgres_engine 
from Extract import fetch_data
from load import load_csv_to_postgres
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
query = '''
        select pickup_date,vendor_id, passenger_count,trip_distance,fare_amount,payment_type, tip_amount  
        from tripdata
        where year(pickup_date) = 2015 and month(pickup_date) = 1 and  dayofmonth(pickup_date) = 2
        '''

client = get_client()
engine = get_postgres_engine()


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

    print('pipeline executed successfully')

if __name__ == '__main__':
    main()