
# http://blog.chapagain.com.np/hash-table-implementation-in-python-data-structures-algorithms/

import threading

hash_table = [[] for _ in range(10)] #Создание хеш-таблицы в виде вложенного списка (списки внутри списка).

def insert(hash_table, key, value):	#hash_table -- [[], [], [], [], [], [], [], [], [], []], key -- 10, value -- Nepal
    hash_key = hash(key) % len(hash_table)        # hash(10) % len([[], [], [], [], [], [], [], [], [], []]), т.е hash_key == 0
    key_exists = False
    bucket = hash_table[hash_key]    #назовем каждый отдельный список в списке хеш-таблиц как «bucket», возьмет 0-й элемент, т.е. [] -- пустой список.
    for i, kv in enumerate(bucket):	 # выполнится bucket.append((key, value)), при (20, 'India') Цикл по enumerate выполнится и i == 0, kv == (10, 'Nepal'), k ==  10, v = Nepal
        k, v = kv
        if key == k:
            key_exists = True 
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))	 # append() - добавляет элемент в список
 
 
insert(hash_table, 10, 'Nepal')		
insert(hash_table, 25, 'USA')
insert(hash_table, 20, 'India')

# поиск
# распараллеливать здесь

def search(hash_table, key):                    #При поиске любого ключа в хеш-таблице мы должны циклически проходить по каждому отдельному подсписку.
    hash_key = hash(key) % len(hash_table)    
    bucket = hash_table[hash_key]                         
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v

    for i in range(3):
        t = threading.Thread(target = search, name = i, args=(hash_key, i))
        t.start()
    for t in thread_list:
        t.join()

print (search(hash_table, 10)) # Output: Nepal
print (search(hash_table, 20)) # Output: India
print (search(hash_table, 25)) # Output: None


