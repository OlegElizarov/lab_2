# coding=utf-8
# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.items = list(items)
        a = list(kwargs.values())
        if a[0] == True:
            self.kwargs = True
        else:
            self.kwargs = False
        unique_list = []
        for x in self.items:
            if self.kwargs == False:
                if x not in unique_list:
                    unique_list.append(x)
            else:
                if str(x).upper() not in unique_list and str(x).lower() not in unique_list:
                    unique_list.append(str(x).lower())
        self.items = unique_list

    pass

    def __next__(self, i):
        if self.__next__() != None:
            return self.__next__()
        else:
            return None

    def __iter__(self):
        return self
