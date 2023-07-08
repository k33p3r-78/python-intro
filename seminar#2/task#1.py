# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

seq = ''
while set(seq) != {'0', '1'}:
    seq = input("Введите последовательность: ")
    if len(set(seq)) == 1 and set(seq) < {'0', '1'}:
        print("Все монеты лежат одной стороной.")
        exit()

headCount = seq.count('1')
tailCount = seq.count('0')

if headCount >= tailCount:
    print(f"Большинство монет лежат решкой, вам осталось развернуть {tailCount} орлов.")
else:
    print(f"Большинство монет лежат орлом, вам осталось развернуть {headCount} решек.")    