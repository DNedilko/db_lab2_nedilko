import psycopg2
import matplotlib.pyplot as plt

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
GROUP BY anime_general.type, anime_types.type;
'''

query_2 = '''
SELECT COUNT(anime_general.type) as types_num, anime_types.type
FROM anime_general
INNER JOIN 
anime_types
ON anime_general.type = anime_types.id
GROUP BY anime_types.type;
'''


# У мене не достатньо підходящі дані для такого
query_3 = '''
SELECT distinct(rates), episodes
FROM anime_general
WHERE episodes <> 'Unknown'
Order BY episodes desc, rates ASC
limit 10;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    cur.execute(query_1)
    types = []
    avg = []

    for row in cur:
        avg.append(row[0])
        types.append(row[1])

    x_range = range(len(types))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(x_range, avg, label='Total')
    bar_ax.set_title('Середній рейтинг по кожному типу аніме')
    bar_ax.set_xlabel('Аніме')
    bar_ax.set_ylabel('Середній рейтинг')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(types)

    cur.execute(query_2)
    counts = []
    type = []

    for row in cur:
        counts.append(row[0])
        type.append(row[1])

    x_range = range(len(type))

    pie_ax.pie(counts, labels=type, autopct='%1.1f%%')
    pie_ax.set_title('Відсоткове співвідношення кожного типу у базі даних')

    cur.execute(query_3)
    rates = []
    episodes = []

    for row in cur:
        rates.append(row[0])
        episodes.append(row[1])

    graph_ax.plot(episodes, rates, marker='o')

    graph_ax.set_xlabel('Кількість епізодів')
    graph_ax.set_ylabel('Рейтинг')
    graph_ax.set_title('Графік залежності рейтингу від кількості епізодів')

    for ep, rt in zip(episodes, rates):
        graph_ax.annotate(rt, xy=(ep, rt), xytext=(7, 2), textcoords='offset points')

mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()