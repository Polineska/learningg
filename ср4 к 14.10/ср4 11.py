n=int(input("размер массива"))
mas=[0]*n #создание массива
from random import uniform #подключение функции uniform (gkfdf.ofz njxrf)
for i in range(n):  #заполнение массива
    mas[i]=uniform(0,30) #случайными числами от 0 до 30
print(mas)#выводим массив
#maxel=max(mas) можно максимальный элемент найти так
#print(maxel)
#или находим максимальный элемент след.образом
maxx=0
maxind=0 #переменная для макс индекса
for i in range(len(mas)):
    if mas[i]>maxx: 
        maxx=mas[i] #максимальный элемент
        maxind=i #индекс максимального элемента
print(maxx)
print(maxind)
for i in range(n): # пробегаемся по размеру  массива (по индексам)
        if maxind<i: #сравниваем индексы( если  индекс максимального элемента меньше индекса след элемента)
            mas[i]=0 # все элементы после макс зануляем
print("Измененный массив " mas)
        
