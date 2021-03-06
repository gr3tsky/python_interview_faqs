#1. Какие стандартные типы данных вы использовали в Python?
# "Логический" - может принимать одно из двух значений True (истина) или False (Ложь).
is_true = True

#Числа - "integer", могут быть целыми (1 и 2).
int_number = 1

#С плавающей точкой (1.1 и 1.2)
float_num = 1.0
print(1.0 / 3.0) #0.333333333

#Для операций с повышенной точностью используется decimal (Десятичные).
from decimal import Decimal
dec_number = Decimal(1) / Decimal(3)
print(dec_number) #0.33333333333333333333

#Строки - string. Последовательность символов Юникода, например, HTML документ.
var_string = "This is GitHub"

#Списки - list. Упорядоченные последовательности значений.
this_is_list = [1, 2, 3, 4]

#Кортежи - tuple. Упорядоченные неизменяемые последовательности значений.
this_is_tuple = (1,)

#Множества - set. Неупорядоченные наборы значений. Коллекция данных,
#которая хранит неупорядоченные уникальные значения.
this_is_set = ([1, 1, 4, 5, 6])
print(this_is_set) #set([1, 4, 5, 6])

#######################################################################
#2. Сырые строки. Что это?
print(r'Спец символы не \nработают!') # Спец символы не \nработают!
print('Спец символы \nработают!')
#Спец символы
#работают!

#######################################################################
#3. В чем разница между tuple и list?
#Кортежи неизменяемы, а списки да. В этом основная разница. Кортежи быстрее 
#чем списки, поэтому их стоит использовать там, где есть набор элементов, 
#который не требует изменений.
tpl = (1, 2, 3)
tpl[0] = 5
print(tpl) #TypeError: 'tuple' object does not support item assignment

#######################################################################
#4. Что такое set?
#Множество - это "мешок", который содержит неупорядоченные уникальные значения
#Одно множество может содержать значения любых типов. Если у вас есть два множества
#вы можете совершать над ним любые стандартные операции, например, объединение,
#пересечение и разность.
this_is_set = set([1, 2, 3, 3, 3])
print(this_is_set) #set((1, 2, 3))

#######################################################################
#5. Стандартные библиотеки Python (sys, date, string, regex, os.path)
#Модуль json позволяет кодировать и декодировать данные в удобном формате
#Модуль datetime предоставляет классы для обработки даты и времени разными способами
#Модуль os предоставляет множество функций для работы с операционной системой, причем
#их поведение как правило не зависит от ОС, поэтому программы остаются переносимыми.
#Модуль unittest предоставляет богатый набор инструментов для написания и запуска тестов

#######################################################################
#6. Что такое PEP8?
#Свод правил разработанных на основе рекомендаций Гуидо ван Россума о том как лучше следует 
#писать код чтобы сделать его максимально понятным для других программистов. Исходя из практики
#код намного чаще читается, чем пишется, поэтому так важно писать все в едином стиле.
#pep8 диктует этот стиль для всех однозначно

#######################################################################
#7. Сделать swap двух переменных
a = 1
b = 3
a, b = b, a
print(a, b) 
#(3, 1)

#######################################################################
#8. range и xrange в чем разница?
# range в третьей версии возвращает генератор, во второй возвращает list,  
#значения которого записываются в оперативную память (5М элементов, могут "съесть" всю память)
# xrange возвращает генератор, он поодиночно отдает элементы, перезаписывая их, чтобы оперативная 
#память не заполнялась. В третьей версии функции xrange нет.
#Эта разница существует в версии Python 2. В Python 3 этой разницы не существует,
#а range стал вести себя как xrange.

#######################################################################
#9. min or max value in list (задача)
simple_list = [4, 2, 9, 0, 1]
print(max(simple_list)) 
# 9
print(min(simple_list))
# 0

#######################################################################
#10. Удалить повторяющиеся элементы в списке
simple_list = [0, 1, 1, 2, 3, 4, 5, 5]
list = set(simple_list)
# [0, 1, 2, 3, 4, 5]

#######################################################################
#11. Разрезать строку по разделителю и склеить обратно с новым разделителем Z
string = "00100001000000101001010000"
new_list = string.split('1') #['00','0000','000000','0','00','0','0000']
new_string = "Z".join(new_list)
print(new_string) #00Z0000Z000000Z0Z00Z0Z0000

#######################################################################
#12. mutable (изменяемые) and immutable (неизменяемые типы данных) types
# MUTABILITY OF COMMON TYPES
# The following are some immutable objects:
# int
a = 5
old_addr = id(a)
a = 6 #выделена новая ячейка памяти
new_addr = id(a)
print(a) #6
print(old_addr) #3770390   <-адрес старой ячейки памяти
print(new_addr) #3770336   <-адрес новой ячейки памяти
#float
#decimal
#bool
#string
#tuple
#range
#bytes

# The following are some mutable objects:
#list
list = [1, 2, 3]
old_addr = id(list)
list[0] = 4 #[4, 2, 3]
new_addr = id(list)
print(old_addr) #139991941772216   <-адрес старой ячейки памяти
print(new_addr) #139991941772216   <-адрес новой ячейки памяти
#dict
#set
#bytearray
#user-defined classes (unless specifically made immutable)

#######################################################################
#13. Как передаются аргументы в функцию? По ссылке или по значению?
#Ни по тому ни по другому, потому как в языке Python числа, списки, строки являются объектами.
a = 5 #call-by-object (передача неизменяемого объекта)
b = [1, 2, 3, 4, 5] #call-by-object-refernce (передача изменяемого объекта по объекту ссылки)
function1(2, a, b, {'a': 1, 'b': 2}, m = (4, 4, 5))
 b[0] = 5 #изменили первый элемент внутри функции
print(b) #[5, 2, 3, 4, 5]

#######################################################################
#14. Есть ли ошибка?
def is_none(arg): #Функция, которая проверяет arg является ли он None
  if arg: 
    return False
  return True
print(is_none(None)) #True
print(is_none([])) #True (пустой список не может быть None)
print(is_none('')) #True (пустая строка не может быть None)

def is_none(arg): #Функция, которая проверяет arg является ли он None
  if arg is not None: #Правильно так!!! в предыдущем случае происходит проверка на существование arg
    return False
  return True
print(is_none(None)) #True
print(is_none([])) #False (пустой список не может быть None)
print(is_none('')) #False (пустая строка не может быть None)

#######################################################################
#15. Для чего нужны декораторы @staticmethod и @classmethod?
#Декораторы - это функции обертки, которые дают возможность изменить поведение функции
#не меняя её код
class A
  value = 4
  def b(self):
    return True

a = A()
print(A, b()) # вернет ошибку, так ка мы вызываем метод b от класса A, а не от экземпляра a
print(a, b())

class A
  value = 4
  @staticmethod
  def b():
    return True

a = A()
print(A, b()) # True
print(a, b()) # True


class A
  value = 4
  @classmethod
  def b(cls):
    return cls.value #Можно получить атрибут класса из метода b, который является методом класса

a = A()
print(A, b()) # 4
print(a, b()) # 4

#######################################################################
#16. Чем отличаются copy.copy(x) и copy.deepcopy(x) ?
x = [1, 2, 3]
y = x #тут к объекту [1, 2, 3] добавился новый алиас y
y[0] = 4
print(x) #[4, 2, 3]

x = [1, 2, 3]
import copy
y = copy.copy(x) #создается новый объект и кладется в другую ячейку памяти
y[0] = 4
print(x) #[1, 2, 3]

#Если в качестве элемента списка является еще один список
x = [1, 2, 3, [1, 2, 3,]]
import copy
y = copy.copy(x) 
y[3][0] = 4
print(x) #[1, 2, 3, [4, 2, 3,]]

#Чтобы такого не было необходимо делать deepcopy
x = [1, 2, 3, [1, 2, 3,]]
import copy
y = copy.deepcopy(x) 
y[3][0] = 4
print(x) #[1, 2, 3, [1, 2, 3,]]

#######################################################################
#17. lambda functions
#Анонимные функции могут содержать лишь одно выражение, но и выполняются они быстрее.
#Анонимные функции создаются с помощью конструкции lambda. В стандартной библиотеке полно функций,
#которые принимают другие функции: map, reduce, filter, sorted, any, all
event_list = [{'a': 1, 'b': 2}, {'a': 4, 'b': 5}, {'a': -6, 'b': 0}]
event_list.sort(key=lambda x: x['b'],) #сортировкка по значению b вложенных словарей
print(event_list)
#[{'a': -6, 'b': 0}, {'a': 1, 'b': 2}, {'a': 4, 'b': 5}]

#######################################################################
#18. Что делает этот метод? id(object)
#Получает адрес в ячейке памяти
b = a = 2 #два имени ссылаются на один объект, адреса ячеек памяти одинаковые
print(id(a) == id(b)) #True
a = a + 1 #имя a ссылается на новый объект, который на новом адресе памяти
print(id(a) == id(b)) #False


#######################################################################
#19. Как в Python определить private атрибут или метод. Можно ли вызватьэтот метод снаружи класса?
class A:
 _a1 = 4
 __a2 = 5
print(A._a1) # 4
#print(A.__dict__) <- эта команда покажет все атрибуты и методы класса
print(A.__a2) # AtributError: class A has no attribute '__a2'
print(A._A__a2) # 5

#######################################################################
#20. Что такое хеш-функции?
# Хэш представляет собой фиксированное целое число, которое идентифицирует конкретное значение. 
# Конфликты хэшей – это когда два разных значения имеют одинаковый хеш.
# 
print(hash("Look at me!")) # 4343814758193556824
print(hash("Look at me!!"))# 6941904779894686356
а = "Look at me!"
print(hash(a)) # 4343814758193556824
#Эти цифры очень полезны, поскольку они позволяют быстро находить значения в большом наборе
#значений. Примеры их использования в set Python и dict . В list , если вы хотите проверить, есть ли
#значение в списке, с if x in values: Python должен пройти весь список и сравнить x с каждым
#значением в values списка. Это может занять много времени для длинного list . В set Python
#отслеживает каждый хеш, и когда вы вводите if x in values: Python получит хэш-значение для x , 
#посмотрит, что во внутренней структуре, а затем сравнивает x со значениями, которые имеют 
#одинаковые хэш как x .
# Если есть хэш, можно получить его значение
 print(unhash(4343814758193556824)) # Look at me!
 
#######################################################################
#21. Что может быть в качестве ключа словаря?
# Словарь, как и список, является изменяемым (mutable) типом данных, хотя и содержит неизменяемые 
# ключи и может неограниченно расти.

#######################################################################
#21. Что такое декораторы и как они создаются на примере?

#######################################################################
#22. Что такое list coprehension, какой синтаксис создания генераторов?

#######################################################################
#23. Что такое классы?

#######################################################################
#24. Что такое магические методы, какие они бывают и для чего используются?

#######################################################################
#25. Что такое миксин?

#######################################################################
#26. Что такое миксин?

#######################################################################
#27. Что такое JSON?

#######################################################################
#28. Какие noSQL решения бывают для хранения данных?
# CSV, TSV, XML

#######################################################################
#29. Базы данных, с какими работали?

#######################################################################
#30. Что такое индексы, как они работают?

#######################################################################
#31. Чем отличается RIGHT, LEFT, INNER JOIN?

#######################################################################
#32. Как работает http, ftp? Что происходит, когда вы вводите в адресной 
# строке браузера URL сайта и нажимаете ввод?

#######################################################################
#33. Как работает http, ftp? Что происходит, когда вы вводите в адресной 
# строке браузера URL сайта и нажимаете ввод?

#######################################################################
#34. Что такое agile?

#######################################################################
#35. Что такое scrum?

#######################################################################
#36. Что такое git, git flow?

#######################################################################
#37. Что такое get, post, cookoies, session?



#Как пройти собеседование Python программисту [GeekBrains] 
#-> https://www.youtube.com/watch?v=EjO8f8sZnBw&list=WL&index=3&t=0s

#Junior Python Developer: полный разбор собеседования и ответы на наиболее частые вопросы интервью 
#-> https://www.youtube.com/watch?v=fgXCN7A8yzg&list=WL&index=6&t=0s





