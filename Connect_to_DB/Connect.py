
import psycopg2


def connect():

    try:
        connection = psycopg2.connect(user="postgres",
                                      password="tonytrim",
                                      host="SRVHOURT7780",
                                      port="5432",
                                      database="postgres")
        cursor = connection.cursor()
        print(connection.get_dsn_parameters(), "\n")
        print('Trying my brother, be patient...')

        cursor.execute('SELECT version();')
        db_version = cursor.fetchone()
        print('Database Version:{}'.format(db_version))

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL",error)
    finally:
        if (connection):
             cursor.close()
             connection.close()
             print('Hope you done, because connection is closed')


connect()

