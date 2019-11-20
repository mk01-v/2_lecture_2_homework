
#s = [10, 40, 20, 30]
#print(s)
#for element in range(len(s)):
#    s[element] = s[element] + 2
#print(s)


#l1 = [[['Andrey'],['Petrov']],[['Atrem'],['Sidorov']], [['Maksim'], ['Kukushkin']]]
#print(l1[0][0])
#print(l1[0][1])
#rint(l1[1][0])
#print(l1[1][1])
#print(l1[2][0])
#print(l1[2][1])
#l2 = [['Andrey','Petrov'],['Atrem','Sidorov'], ['Maksim', 'Kukushkin']]
#print(l2[0][0])
#print(l2[0][1])
#print(l2[1][0])
#print(l2[1][1])
#print(l2[2][0])
#print(l2[2][1])

s1 = 'test\ntest'
#print(s1)
s2 = '''test
test'''
#print(s2)
print(s1[1])
print(s1[-1])
#вырезка
print(s1[0:2])
s3 = 'test'
#часть текста начинается с 'te'. возвращает True.
print(s3.startswith("te"))
print(s3.endswith("te"))
# индекс расположения буквы. Начинается отсчет с 0.
print(s3.index('s'))

#поиск, возращает индекс символа или нескольких символов. При неудаче - "-1".
print(s3.find('e'))
print(s3.find('set'))

#соединяет в 1 список.
s4 = ('testwett\nesttex')
#kkk = s4.split('\n')
#print(kkk)

#соединяет в 1 элемент, разделяя пробелами.
print(' '.join(s1))

