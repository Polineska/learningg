n=int(input("размер массива A"))
masA=[0]*n #создание массива
print ("Введите", n, "элементов массива A:")
for i in range(n): # перебор индексов
    masA[i] = int(input()) # ввод числа с клавиатуры и собственно сам массив A
masA.sort()
print(masA)
n=int(input("размер массива B"))
masB=[0]*n #создание массива
print ("Введите", n, "элементов массива B:")
for i in range(n): # перебор индексов
    masB[i] = int(input()) # ввод числа с клавиатуры и собственно и сам массив B
masB.sort()
print(masB)
nmas=[] #создаем пустой массив для одинаковых элементов
for i in range(len(masA)):
    for j in range(len(masB)):
        if masA[i]==masB[j]: # если элементы равны
            nmas.append(masA[i]) #добовляем в новый массив
print(', '.join(map(str,nmas))) # убираем квадратные скобки у массива
               

