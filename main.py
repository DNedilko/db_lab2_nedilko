import psycopg2
import psycopg2
import matplotlib.pyplot as plt

username = 'nedilko'
password = 'pass'
database = 'DB_lab2'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT count(information.type) as num_of_records, types.name
FROM information
INNER JOIN types
ON information.type=types.id
group by types.name;
'''

query_2 = '''
SELECT episodes, information.name
FROM information
INNER JOIN episodes
ON information.id = episodes.an_id
ORDER BY members DESC
LIMIT 10;
'''


# У мене не достатньо підходящі дані для такого
query_3 = '''
SELECT AVG(value), types.name
FROM information
INNER JOIN rates
USING(id)
INNER JOIN types
ON types.id = information.type
GROUP BY types.name;
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

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
#
# with conn:
#     cur = conn.cursor()
#
#     cur.execute(query_1)
#     types = []
#     num = []
#
#     for row in cur:
#         types.append(row[1])
#         num.append(row[0])
#
#     x_range = range(len(types))
#
#     figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
#     bar = bar_ax.bar(x_range, num, label='Type')
#     bar_ax.set_title('Кількість записів\n для кожного типу \nу базі даних')
#     bar_ax.set_xlabel('тип')
#     bar_ax.set_ylabel('кільість записів')
#     bar_ax.set_xticks(x_range)
#     bar_ax.set_xticklabels(types)
#
#
#     cur.execute(query_2)
#     episodes = []
#     names = []
#
#     for row in cur:
#         episodes.append(row[0])
#         names.append(row[1])
#     pie_ax.pie(episodes, labels=names, autopct='%1.1f%%')
#     pie_ax.set_title('Кількість серій\n для топ 10 аніме \nза кількістю персонажів')
#
#
#     cur.execute(query_3)
#     avg = []
#     types = []
#
#     for row in cur:
#         avg.append(row[0])
#         types.append(row[1])
#
#     graph_ax.plot(types, avg, marker='o')
#
#     graph_ax.set_xlabel('Тип аніме')
#     graph_ax.set_ylabel('Середній рейтинг')
#     graph_ax.set_title('Графік залежності \nрейтингу аніме\n від його типу')
#
#
#
# mng = plt.get_current_fig_manager()
# mng.resize(1600, 600)
#
# plt.show()