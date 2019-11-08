#1. Удалить все элементы списка:
simpe_list = [1, 2, 3]
del simple_list[:]
print(simple_list) # []

# Создать копию списка
simpe_list = [4, 5, 6]
new_simpe_list = simpe_list[:] # Идентично функции copy
print(id(simpe_list) is id(new_simpe_list)) # False
print(new_simpe_list) # [4, 5, 6]
print(new_list is simpe_list)# False

#######################################################################
#2. Python 3.5+ поддерживает аннотацию типов:
def my_function(a: int, b: int) -> int: #на входе функция ожидает 2 чила и вернет число
  return a * b
print(function(3,4)) # 12

#######################################################################
#3. Объединить два dictionary в Python 3.5+
dict_one = {'a': 1, 'b': 2}
dict_two = {'b': 3, 'c': 4}
result = {**dict_one, **dict_two} #распаковка, объединение и замена новыми значениями элементов с одинаковыми ключами
print(result) # {'a': 1, 'c': 4, 'b': 3}

#######################################################################
#4. Объединит два dictionary в Python 2
dict_one = {'a': 1, 'b': 2}
dict_two = {'b': 3, 'c': 4}
result = dict(dict_one, **dict_two) #распаковка, объединение и замена новыми значениями элементов с одинаковыми ключами
print(result) # {'a': 1, 'c': 4, 'b': 3}

#######################################################################
#5. Операторы "is" или "=="
# Оператор "is" сравнивает адреса в ячейках памяти, а "==" сравнивает значения
a = [1, 2, 3]
b = a
print(a is b) #True, адрес один и тот же
print(a == b) #True, значения одинаковы
c = list(a) # Создание нового объекта, с новым адресом
print(a == c) #True, значения равны
print(a is c) #False, потому что новый адрес

#######################################################################
#6. Вывести Zen of Python by Tim Peters
import this

#######################################################################
#7. Генераторы списков
values = [expression
         for value in collection
         if condition]
# Эквивалентно этому
values = []
for value in collection:
  if condition:
    values.append(expression)

# Пример:
even_squers = [x * x for x in range(10) if not x % 2]
#возвести в квадрат все числа в диапазоне от 0-10, которые являются четными
print(even_squers) #[0, 4, 16, 36, 64]

#######################################################################
#8. Функции в Python можно передавать как значения в другие функции 
# и возвращать их как значения из других функций
def my_function(a, b):
  return a + b
funcs = [my_function]
print(funcs[0]) #returns Error
print(funcs[0](2,3)) # 5

#######################################################################
#9. Стандартный метод repr у словаря сложночитаем, так как выводит все значения 
# массива данных в одну строку
my_dictionary = {'a': 29, 'b': 72, 'c': 0xc0ffee}
print(my_dictionary) #Без сортировки
# {'a': 29, 'c': 0xc0ffee, 'b': 72}

# Однако мы можем сделать библиотеку читабельнее с помощью json библиотеки
import json
print(json.dumps(my_dictionary, indent=4, sort_keys=True))
#{
#  'a': 29,
#  'b': 72,
#  'c': 0xc0ffee
#}



#Как пройти собеседование Python программисту [GeekBrains] 
#-> https://www.youtube.com/watch?v=EjO8f8sZnBw&list=WL&index=3&t=0s




