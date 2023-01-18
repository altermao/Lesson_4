# Модуль 1

# функция separator Функция создает разделитель из любых символов любого количества
#     :param simbol: символ разделителя
#     :param count: количество повторений
#     :return: строка разделитель примеры использования ниже

def separator(simbol, count):
    return simbol*count

print(separator('-', 10) == '----------')  # True
print(separator('#', 5) == '#####')  # True


# функция long_separator
def long_separator(count):
    return separator('*', count)

print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True

# функция simple_separator
def simple_separator():
    return long_separator(10)

print(simple_separator() == '**********')  # True


# Функция печатает приветствие в красивом формате
#     **********
#     Hello {who}!
#     ##########
#     :param who: кого мы приветствуем, по умолчанию World
#     :return: None
#     """

def hello_who(who='World'):
    print(separator('*', 10))
    print()
    print(f'Hello {who}!')
    print()
    print(separator('#',  10))


print (hello_who())

#"
    # Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    # :param power: степень
    # :param args: любое количество цифр
    # :return: результат вычисления # True -> (1 + 2)**1
    # """

def hello_world():
    print (hello_who())
print (hello_who ('{who}'))
print (hello_who('Kate'))
print (hello_who('Max'))

def pow_many(power, *args):
    sum=0
    for n in args:
        sum+=n
    return (sum**power)
print(pow_many(1,1,2)==3)
print(pow_many(1,2,3)==5)
print(pow_many(2,1,1)==4)
print(pow_many(3,2)==8)
print(pow_many(2,1,2,3,4)==100)

    # """
    # Функция выводит переданные параметры в фиде key --> value
    # key - имя параметра
    # value - значение параметра
    # :param kwargs: любое количество именованных параметров
    # :return: None
    # """
def print_key_val(**kwargs):
    for key, value in kwargs.items():
        print("{} --> {}".format(key,value))

# """
# name --> Max
# age --> 21
# """
print_key_val(name='Max', age=21)
# """
# animal --> Cat
# is_animal --> True
# """
print_key_val(animal='Cat', is_animal=True)

def my_filter(iterable, function):
    result =[]
    for items in iterable:
        if function (items):
            result.append(items)
    return result
   # """
    # (Усложненое задание со *)
    # Функция фильтрует последовательность iterable и возвращает новую
    # Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
    # (примеры ниже)
    # :param iterable: входаня последовательности
    # :param function: функция фильтрации
    # :return: новая отфильтрованная последовательность
    # """
#     return list (filter (function, iterable)




print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True