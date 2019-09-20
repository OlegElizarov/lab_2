import random
# coding=utf-8

# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field (items, *args):
    assert len(args) > 0
    nn=True
    for k in range(len(args)):
        if args[k]== None:
            print (None)
            print ()
            nn=False
            break

    if nn:
        for i in range(len(items)):
            if (len(args)>1):
                for j in range(len(args)):
                    print (args[j],items[i][args[j]],end=' ')
            else:
                print(items[i][args[0]],end=' ')
        print ( )
    # Необходимо реализовать генератор 


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    pass
    a=[random.randint(begin,end) for i in range(num_count)]
    print (a,end=' ')
    print ()
    return a
    # Необходимо реализовать генератор
