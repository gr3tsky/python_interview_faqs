#1 Какие стандартные типы данных вы использовали в Python?
# "Логический" - может принимать одно из двух значений True (истина) или False (Ложь)
is_true = True
#Числа - "integer", могут быть целыми (1 и 2)
int_number = 1
#С плавающей точкой (1.1 и 1.2)
float_num = 1.0
#Для операций с повышенной точностью используется decimal (Десятичные)
from decimal import Decimal
dec_number = Decimal(1) / Decimal(3)
print(dec_number)
