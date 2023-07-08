# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

num = ''
while len(str(num)) != 3:
    num = int(input("Введите число: "))

res = 0
while num // 10:
    res += num % 10
    num //= 10
res += num

print(res)
