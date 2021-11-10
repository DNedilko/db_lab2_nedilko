import psycopg2


username = 'nedilko'
password = 'pass'
database = 'DB_lab2'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT avg(rates) as avg_per_type, anime_types.type
FROM anime_types
INNER JOIN anime_general
ON anime_general.type = anime_types.id
GROUP BY anime_general.type, anime_types.type
ORDER BY avg_per_type DESC;
'''

query_2 = '''
SELECT COUNT(anime_general.type) as types_num, anime_types.type
FROM anime_general
INNER JOIN 
anime_types
ON anime_general.type = anime_types.id
GROUP BY anime_types.type
ORDER BY types_num;
'''


# У мене не достатньо підходящі дані для такого
query_3 = '''
SELECT distinct(rates), episodes
FROM anime_general
WHERE episodes <> 'Unknown'
Order BY episodes desc
limit 10;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    cur.execute(query_1)
    print("--First query--")
    for row in cur:
        print(row)

    cur.execute(query_2)
    print("--Second query--")
    for row in cur:
        print(row)

    cur.execute(query_3)
    print("--Third query--")
    for row in cur:
        print(row)
