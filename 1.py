name=input("Имя студента")
surname=input("Фамилия студена")
birth=int(input("Год рождения"))
name, surname= surname, name
birth+=60
print(name,surname,birth, sep="_")
