# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                      Физика:         30(л)       —    10(лаб)
#                      Физкультура:       —    30(пр)        —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open("task06.txt", "r", encoding='utf-8') as f_obj:
    number_of_lines = len(f_obj.readlines())
    f_obj.seek(0)
    class_hours = {}
    for i in range(number_of_lines):
        line = f_obj.readline().replace('\n', '').split(' ')
        if line[1] == '—':
            line[1] = '0(л)'
        if line[2] == '—':
            line[2] = '0(пр)'
        if line[3] == '—':
            line[3] = '0(лаб)'
        total_num = int(line[1][:-3]) + int(line[2][:-4]) + int(line[3][:-5])
        class_hours.update({line[0]: total_num})
print(class_hours)
