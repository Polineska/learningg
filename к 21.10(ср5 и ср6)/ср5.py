#самостоятельна работа 5
# Процедура перевод в двоичную систему
def f(n): # n - целое число 0...255
    k = 128 # делитель для старшей цифры
    while k > 0: # пока делитель больше 0
        d = n // k # очередная цифра
        print(d , end="") # вывод очередной цифры
        n = n % k # заменяем число на остаток
        k = k // 2 # делитель для следующей цифры
# Основная программа
x = int(input("Введите число 0...255: "))
f (x) # вызов процедур
    
