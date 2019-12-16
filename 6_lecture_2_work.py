---текст
При работе с файлами и директориями. Настройка.
1. Импорт пакетов в cmd.
import os
import os.path
2. Проверка текущего пути.
os.getcwd
os.getcwd()
3. Смена пути
os.chdir("C:\\Python")
Проверяем, произошла ли смена.
os.getcwd()
4. Получить список файлов текущего пути.
os.listdir("C:\\Python")
os.listdir(".") - получить список файлов текущего пути.
os.listdir("Scripts") - получить список файлов текущей директории.
5. Проверка файл/директория.
os.path.isfile("Scripts")
>>>False
os.path.isdir("Scripts")
>>>True
6. Фильтр на файлы, без директорий и фармируем в список.
list(filter(lambda f: os.path.isfile(f), os.listdir(".")))
>>>Список
7. Создание директории

os.mkdir("test") - создает 1 директорию.
os.makedirs("test1\\test2\\test3") - создает вложенные директории.
8. Удаление директории.
os.rmdir("test") - не работает, если есть другие подкаталоги.
9. Для удаления нескольких каталогов.
import shutil
shutil.rmtree("test1")
10. Копирование файлов.
shutil.copy("c:\\Python\\README.txt", "c:\\testpy")
11. Удаление файла
os.remove("C:\\testpy\\README.txt")
----






















