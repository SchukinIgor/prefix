import csv

with open('/home/user/Загрузки/students.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter=','))[1:]

id_project = input()
while id_project != 'СТОП':
    for el in reader:
        if el[-3] == id_project:
            surname, name, partonumic = el[1].split()
            print(f'Проект № {id_project} делал: {name[0]}. {surname} он(а) получил(а) оценку - {el[-1]}')
            break
    else:
        print('Ничего не найдено')
    id_project = input()

