import json
from datetime import datetime as dt
from collections import Counter


class Context:

    def __init__(self, upload_file):
        self.file = upload_file
        self.open = open(upload_file, 'r', encoding='UTF8')

    def __enter__(self):
        if self.file.endswith('.json'):
            duration = json.load(self.open)
            print(duration)
        else:
            raise ValueError

        end = dt.now()
        start = dt.now()

        print(f"Время запуска программы - {start:%d.%m.%Y %H:%M:%S:%f}")
        print(f'Время окончания программы - {end:%d.%m.%Y %H:%M:%S:%f}')
        print(f'Время выполнения программы: {start - end}')

    def __exit__(self, *args):
        print('The program is succesfully finished')
        self.open.close()


with open('newsafr.json', encoding='utf-8') as datafile:
    json_data = json.load(datafile)
    for data in json_data.values():
        news_dict = (data['channel'])

for items in news_dict.items():
    news_list = (news_dict['items'])

news_l = []

for news in news_list:
    news_l.extend((news['description'].split(' ')))

words_list = []

for i in news_l[:]:
    if len(i) > 6:
        words_list.append(i)

words_counter = Counter(words_list)
words_list = list(words_counter.items())
words_list.sort(key=lambda x: x[1])
top_list = words_list[:-11:-1]
top_words = []
for tuple in top_list:
    top_words.append(tuple[0])
print('10 самых часто встречающихся слов (длиннее 6 букв): ', '\n', top_words)

with Context('newsafr.json') as cont:
    cont
