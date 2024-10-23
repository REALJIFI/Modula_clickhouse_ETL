import sqlalchemy
import clickhouse_connect
from dotenv import load_dotenv
import os

load_dotenv(override=True)

def get_client():
    '''
    connects to a clickhouse database using parameters from a .env file

    paramenters: None

    Returns:
    - clickhouses connect.client: A database client object
    '''
    
    #getting credentials 
    host = os.getenv('G_host')
    port = os.getenv('G_port')
    user = os.getenv('G_user')
    password = os.getenv('G_password')

    # connect to database
    client = clickhouse_connect.get_client(host=host, port=port, user=user, password=password, secure=True)

    return client

def get_postgres_engine():
    '''
    constructs a SQLalchemy engine object for postgres DB from .env file

    parameters: None

    Return:
    - sqlalchemy engine (sqlalchemy.engine.Engine)
    '''
    engine = sqlalchemy.create_engine("postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(
                          user = os.getenv('P_user'),
                          password = os.getenv('P_password'),
                          host = os.getenv('P_host'),
                          port = os.getenv('P_port'),
                          dbname = os.getenv('P_database')
                               )
                        )
    
    return engine