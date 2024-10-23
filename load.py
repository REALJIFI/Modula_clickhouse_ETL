import pandas as pd

def load_csv_to_postgres(csv_file_path, table_name, engine, schema):
    ''''
    load data from a csv file to postgres DB table

    parameters:
    - csv_file_path (str): path to csv file
    - table_name (str): a pandas db table
    -engine (sqlalchemy.engine): an SQL alchemy engine object
    -schema (str): a postgres DB schema 
    '''

    # read csv file to pandas and sql
    df = pd.read_csv(csv_file_path)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False, schema=schema)

    print(f'{len(df)} rows loaded to staging successfully')