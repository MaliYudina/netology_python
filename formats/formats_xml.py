import xml.etree.ElementTree as ET
from collections import Counter


words_raw = []

encode = ET.XMLParser(encoding='utf-8')
tree = ET.parse('assets/newsafr.xml', parser=encode)
for element in tree.findall('channel/item'):
    description = element.find('description')
    words_raw.extend(description.text.split(' '))

words_list = []

for i in words_raw:
    if len(i) > 6:
        words_list.append(i)

top_10 = tuple(Counter(words_list).most_common(10))

answer = []
for word in top_10:
    answer.append(word[0])

print('10 самых часто встречающихся слов (длиннее 6 букв): ', '\n', answer)
