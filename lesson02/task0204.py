# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

my_list = input('Введите несколько слов, разделённых пробелами: ').split(' ')
for ind, word in enumerate(my_list, 1):
    if len(word) > 11:
        word = word[:10]
    print(ind, word)
