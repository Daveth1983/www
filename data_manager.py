import os
import psycopg2
import psycopg2.extras


def establish_connection(connection_data=None):
 
    if connection_data is None:
        connection_data = get_connection_data()
        # print(connection_data)
    try:
        # connect_str = "dbname={} user={} host={} password={}".format(connection_data['dbname'],
        #                                                              connection_data['user'],
        #                                                              connection_data['host'],
        #                                                              connection_data['password'])
        connect_str = "dbname={} user={} host={} password={}".format('test_nae5', 'postgres1', 'dpg-cllm3rsjtl8s73adabig-a', '3LMINopqPL8y0XALTDnRO2JvvKBbIXQV')
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
    except psycopg2.DatabaseError as e:
        print("Cannot connect to database.")
        print(e)
    else:
        return conn


def get_connection_data():
    pass
    # return {
    #     'dbname': os.environ.get('MY__PSQL_DBNAME'),
    #     'user': os.environ.get('MY__PSQL_USER'),
    #     'host': os.environ.get('MY__PSQL_HOST'),
    #     'password': os.environ.get('MY__PSQL_PASSWORD')
        
    # }


def execute_select(statement, variables=None, fetchall=True):
   
    result_set = []

   
    with establish_connection() as conn:
        # with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(statement, variables)
            result_set = cursor.fetchall() if fetchall else cursor.fetchone()
    return result_set


def execute_insert(statement, variables=None):
    with establish_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(statement, variables)

