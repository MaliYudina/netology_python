import xml.etree.ElementTree as ET
from collections import Counter


words_raw = []

tree = ET.parse('assets/newsafr.xml')
for element in tree.findall('channel/item'):
    description = element.find('description')
    words_raw.extend(description.text.split(' '))

words_list = []

for i in words_raw:
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