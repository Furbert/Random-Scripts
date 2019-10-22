import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="tonytrim",
                                  host="SRVHOURT7780",
                                  port="5432",
                                  database="RADDB")

    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE Oman_bst12
          (epoch bigint NOT NULL ,
          tag_name  varchar NOT NULL,
          value  char  NOT NULL ); '''


    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while creating PostgreSQL table", error)
finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")