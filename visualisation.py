import psycopg2
import matplotlib.pyplot as plt

username = 'nedilko'
password = 'pass'
database = 'DB_lab2'
host = 'localhost'
port = '5432'


query_1 = '''
SELECT count(anime.type_id) as num_of_records, types.type_name
FROM anime
INNER JOIN types
ON anime.type_id=types.type_id
group by types.type_name;
'''

query_2 = '''
SELECT episodes.members, anime.anime_name
FROM anime
INNER JOIN episodes
ON anime.anime_id = episodes.anime_id
ORDER BY members;
'''


# У мене не достатньо підходящі дані для такого
query_3 = '''
SELECT AVG(rate_value), types.type_name, types.type_id
FROM anime
INNER JOIN ratings
USING(anime_id)
INNER JOIN types
ON types.type_id = anime.type_id
GROUP BY types.type_name, types.type_id ;
'''


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    cur.execute(query_1)
    types = []
    num = []

    for row in cur:
        types.append(row[1])
        num.append(row[0])

    x_range = range(len(types))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(x_range, num, label='Type')
    bar_ax.set_title('Кількість записів\n для кожного типу \nу базі даних')
    bar_ax.set_xlabel('тип')
    bar_ax.set_ylabel('кільість записів')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(types)


    cur.execute(query_2)
    episodes = []
    names = []

    for row in cur:
        episodes.append(row[0])
        names.append(row[1])
    pie_ax.pie(episodes, labels=names, autopct='%1.1f%%')
    pie_ax.set_title('Кількість серій\n для топ 10 аніме \nза кількістю персонажів')


    cur.execute(query_3)
    avg = []
    types = []
    tn = []

    for row in cur:
        avg.append(row[0])
        types.append(row[1])
        tn.append(row[2])

    graph_ax.plot(types, avg, marker='o')

    graph_ax.set_xlabel('Тип аніме')
    graph_ax.set_ylabel('Середній рейтинг')
    graph_ax.set_title('Графік залежності \nрейтингу аніме\n від його типу')


    for t, a in zip(tn, avg):
        graph_ax.annotate(a, xy=(t, a), xytext=(7, 2), textcoords='offset points')

mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()