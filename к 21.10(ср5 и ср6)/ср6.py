#функция нахождения индекса максимального элемента
def f(mass):
    maxx=0
    maxind=0
    for i in range(len(mass)):
        if mass[i]>maxx:
            maxx=mass[i]#максимальный элемент
            maxind=i # ищем индекс максимального элемента
#       return maxx
    return maxind #возвращаем индекс максимального элемента


n=int(input("размер массива"))
mas=[0]*n #создание массива
from random import uniform #подключение функции uniform (gkfdf.ofz njxrf)
for l in range(n):  #заполнение массива
    mas[l]=uniform(0,30) #случайными числами от 0 до 30
print("Изначальный массив",mas)#выводим массив

#print("Индекс максимального элемента",f(mas))

for k in range(n): # пробегаемся по размеру  массива (по индексам)
    if f(mas)<k: #сравниваем индексы( если  индекс максимального элемента меньше индекса след элемента)
        mas[k]=0# все элементы после макс зануляем
print("Измененный массив ",mas)
