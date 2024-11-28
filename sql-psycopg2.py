import psycopg2

# connect to"chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# fetch the results (multiple)
results = cursor.fetchall()


# fetch the result (single)
# results = cursor.fetchone()

#close the connection 
connection.close()

#print results
for result in results:
    print(result)
