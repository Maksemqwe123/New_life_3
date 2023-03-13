import psycopg2

host = 'localhost'
user = 'postgres'
password = 'Makcemjoi990'
db_name = 'assistants'

connection = psycopg2.connect(
    user=user,
    password=password,
    host=host,
    database=db_name
)
