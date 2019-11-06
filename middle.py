#1. Итераторы и генераторы yield. Как его создать? Чем отличается iterator от iterable?
# Итератор - это объект, который осуществляет доступ к элементам последовательности.
# Итерация - это процесс  (цикл) обработки элементов последовательности.Один шаг в цикле тоже называется итерацией.
# На каждой итерации итератор (с помощью своего метода __next__) указывает на следующий и возвращает текущий
# элемент (и удаляет его из очереди).
# Итерируемый объект включает в себя (помимо последовательности) итератор (для цикличесой обработки).
# Итераторы - это специальные объекты, предоставляющие последовательный доступ к данным из контейнера.