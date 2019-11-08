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
