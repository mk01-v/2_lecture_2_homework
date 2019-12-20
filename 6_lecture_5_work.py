import json



f=open("C:/Python/config.json")
try:
    res = json.load(f)
except json.decoder.JSONDecodeError as ex:
    #pass
    #вывод описания ошибки и пустого словаря.
    print(ex)
    res = {}
# выполнять в любом случае.
finally:
    f.close()

print(res)




#res ['browser']['firefox']
#>>>firefox












