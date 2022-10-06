kolvoexponatov=int(input(" количество экспонатов ="))
kolvolet=int(input("количество лет ="))
a=8*60/5 #кол-во человек могут посетить музей за день
if kolvoexponatov < 0:
    print("значение экспонатов неверно")
elif kolvolet < 0:
    print("введено неверное значение времени")
else:
    print("введены неверные значение")
if kolvolet>0 and kolvoexponatov>=0 :
    print("будет просмотрено экспонатов для заданного кол-во времни = ", kolvolet*365*a)
if kolvoexponatov>0 and kolvolet>=0:
    print("будет затрачено времни(в минутах) на просмотр экспонатов =",((kolvoexponatov/a)*60*8))

    

             
                   
