import os

# Чтение содержимого файлов
with open('1.txt', 'r', encoding='utf-8') as file:
    content_1 = file.readlines()

with open('2.txt', 'r', encoding='utf-8') as file:
    content_2 = file.readlines()

# Добавление строк из файла 1.txt в файл 2.txt
content_2.extend(content_1)

# Запись обновленного содержимого файла 2.txt
with open('2.txt', 'w', encoding='utf-8') as file:
    file.writelines(content_2)

# Удаление файла 1.txt
os.remove('1.txt')

# Переименование файла 2.txt в 1.txt
os.rename('2.txt', '1.txt')

# Сортировка файлов по количеству строк в них
file_contents = {'1.txt': content_1}
sorted_files = sorted(file_contents.items(), key=lambda x: len(x[1]))

# Запись содержимого отсортированных файлов в результирующий файл
with open('result.txt', 'w', encoding='utf-8') as result_file:
    for filename, content in sorted_files:
        result_file.write(f"{filename}\n{len(content)}\n")
        result_file.writelines(content)

