# coding=utf-8

# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:
def print_result(func):
    def a(*args):
        print(func.__name__)
        res = func(*args)
        if type(res)== list:
            print (res)
        elif type(res)== dict:
            a=list(res.keys())
            b=list(res.values())
            for i in range(2):
                print (a[i],'=',b[i])
        else:
            print (res)
    return a
