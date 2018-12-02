import json
from collections import Counter


with open('assets/newsafr.json', encoding='utf-8') as datafile:
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