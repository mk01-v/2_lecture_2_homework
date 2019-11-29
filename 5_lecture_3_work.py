
import random
# импорт констант содержащих символов
import string

# вывод случайных символов.
#print(random.choice('abcd'))

# вывод всех символов
#print(string.ascii_letters)
#print(string.digits)

# генератор случайной буквы или числа.
#print(random.choice(string.ascii_letters + string.digits))

# генератор с помощью вывернутого цикла фор
# не работает
#print(random.choice(string.ascii_letters + string.digits) for i in range(20))
# работает
#for i in range(20):
#    print(random.choice(string.ascii_letters + string.digits))

# не работает склейка в 1 строку.
x = []
for i in range(5):
    x[i] = x[i] + ''.join(random.choice(string.ascii_letters + string.digits))
print(x)
# как реализовано в командной строке, генерация 20 случайных символов
# [random.choice(string.ascii_letters + string.digits) for i in range(20)]
# ''.join([random.choice(string.ascii_letters + string.digits) for i in range(20)])
# ''.join([random.choice(string.ascii_letters + string.digits) for i in range(random.randrange(20))])
















