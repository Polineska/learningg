katet1=int(input("катет 1 = "))
katet2=int(input("катет 2 = "))
gipotenuza=int(input("гипотенуза = "))
pirimetr=katet1+katet2+gipotenuza
ploshad=0.5*(katet1*katet2)
if katet1**2+katet2**2==gipotenuza**2:
    print("площадь треугольника = ",ploshad, "перииметр равен = " , pirimetr)
else:
    print("Введенные данные не подходят под существования прямоугольного треугольника \
исправьте данные под условие katet1**2+katet2**2==gipotenuza**2 ")
          
          
