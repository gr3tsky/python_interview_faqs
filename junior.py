#1 Какие стандартные типы данных вы использовали в Python?
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
#2 Сырые строки. Что это?
print(r'Спец символы не \nработают!') # Спец символы не \nработают!
print('Спец символы \nработают!')
#Спец символы
#работают!

#######################################################################
#3 В чем разница между tuple и list?
#Кортежи неизменяемы, а списки да. В этом основная разница. Кортежи быстрее 
#чем списки, поэтому их стоит использовать там, где есть набор элементов, 
#который не требует изменений.
tpl = (1, 2, 3)
tpl[0] = 5
print(tpl) #TypeError: 'tuple' object does not support item assignment

#######################################################################
#4 Что такое set?
#Множество - это "мешок", который содержит неупорядоченные уникальные значения
#Одно множество может содержать значения любых типов. Если у вас есть два множества
#вы можете совершать над ним любые стандартные операции, например, объединение,
#пересечение и разность.
this_is_set = set([1, 2, 3, 3, 3])
print(this_is_set) #set((1, 2, 3))

#######################################################################
#5 Стандартные библиотеки Python (sys, date, regex, os.path)
#Модуль json позволяет кодировать и декодировать данные в удобном формате
#Модуль datetime предоставляет классы для обработки даты и времени разными способами
#Модуль os предоставляет множество функций для работы с операционной системой, причем
#их поведение ак правило не зависит от ОС, поэтому программы остаются переносимыми.
#Модуль unittest предоставляет богатый набор инструментов для написания и запуска тестов

#######################################################################
#Что такое PEP8?
#Свод правилраз работанных на основе рекомендаций Гуидо ван Россума о том как лучше следует 
#писать код чтобы сделать его максимально понятным для других программистов. Исходя из практики
#код намного чаще читается, чем пишется, поэтому так важно писать все в едином стиле.
#pep8 диктует этот стиль для всех однозначно

#######################################################################



