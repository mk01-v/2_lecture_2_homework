import json


# если файл не существует или не читается добавляется with
# и finally не надо, т.к. блок with закроет его сам.

with open("C:/Python/config.json") as f:
    try:
        res = json.load(f)
    except json.decoder.JSONDecodeError as ex:
        # pass
        # вывод описания ошибки и пустого словаря.
        print(ex)
        res = {}

print(res)