search =[] #Список создаем для вывода строк которые будем сортировать
count = 0 #Переменная счетчик
search_str = input("Напишите строку которая будет использоваться для поиска: ") #Просим ввести строку для поиска
with open("D:\\profiles\\ShatukA_82\\Desktop\\Новая папка\\text.txt", 'r', encoding='utf-8') as file: #Читаем файл text.txt через 'r' 
    for i in file: #Цикл для поиска и добавления строк в список
        if search_str in i: #Доп проверка подстроки
            search.append(i) #Добавляем в список строки
            count += 1 #При найденой строки добавляем счетчику 1 чтобы потом вывести кол-во строк
print(f"Нашлось {count} строк") #Выводим кол-во найденных строк
print(f"Отсортированные строки: {sorted(search)}") #Выводим список с только что отсортированными строками