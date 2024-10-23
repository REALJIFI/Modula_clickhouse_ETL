import pandas as pd

# function to get data
def fetch_data(client, query):
    '''
    fetches query output from a clickhouse database and writes to a csv file

    parameters:
    - client (clickhouse_connect.Client)
    - Query(A SQL select query)

    Return:None 
    '''

    #execute the query
    output = client.query(query)
    rows = output.result_rows
    cols = output.column_names

    #close the client
    client.close()

    #write to pandas df and csv file
    df = pd.DataFrame(rows, columns=cols)
    df.to_csv('tripdata.csv', index=True)

    print(f'{len(df)} successfully Extracted')
