with open('../../../PycharmProjects/Python7/007_working_with_files/text_files/trimushketera.txt', 'r', encoding='utf-8') as file:
    text = file.read()
text = text.replace('\n', ' ')
text = text.replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace(';', '').replace('"', '')
text = text.lower()
words = text.split()
print('Количество слов в тексте: ',len(words))
# print(type(words))

uniq_words = set(words)
print('Количество уникальных слов в тексте: ', len(uniq_words))

with open('alpf_list.txt', 'w', encoding='utf-8') as wfile:
    alpf_words = list(uniq_words)
    alpf_words.sort()
    for wor in alpf_words:
        wfile.write(wor + "\n")













