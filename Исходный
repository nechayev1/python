# http://blog.chapagain.com.np/hash-table-implementation-in-python-data-structures-algorithms/
# импортируем библиотеку времени, для того, чтобы засечь сколько работала программа
import threading
import time

hash_table = [[] for _ in range(10)] 	#Создание хеш-таблицы в виде вложенного списка в 10 элементов (списки внутри списка).

# вставили данные в хэш-таблицу 
def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    cell = hash_table[hash_key]   	 #назовем каждый отдельный список в списке хеш-таблиц как «cell»
    for i, kv in enumerate(cell):
        k, v = kv
        if key == k:                # проверяет равны ли оба операнда
            key_exists = True       # проверка наличия ключа в словаре
            break                   # прирывание цикла
    if key_exists:
        cell[i] = ((key, value))    
    else:
        cell.append((key, value))   # добавляет указанный элемент в конец списка
insert(hash_table, 10, 'Nepal')     
insert(hash_table, 25, 'USA')       # добавляет указанный элемент в список на указанную позицию
insert(hash_table, 20, 'India')

# поиск данных из хэш-таблицы
def search(hash_table, key):                    
    hash_key = hash(key) % len(hash_table)    
    cell = hash_table[hash_key]                         
    for i, kv in enumerate(cell):	# цикл, enumerate() позволяет перебирать коллекцию элементов.
        k, v = kv                   # при поиске любого ключа в хеш-таблице мы должны циклически проходить по каждому отдельному подсписку.
        if key == k:
            return v                
print (search(hash_table, 0))#  Nepal
print (search(hash_table, 20)) #  India
print (search(hash_table, 30)) #  None
