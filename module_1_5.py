immutable_var = 1, 2, "kortej", "4", True
print(immutable_var[1])
print(type(immutable_var))
print(immutable_var)
print(len(immutable_var))
#immutable_var[0][0] = 7
#print(immutable_var)

print(" ")

immutable_var_1 = ([1, 2, 3, 4], 3, 4, 5)
print(len(immutable_var_1))
# квадрутную скобу он получается считает как список, т.к. считает её одним элементом
# получается кортеж неизменим, изменимы только элементы в виде списка, которые содержатся в нём (не считая конкотенации и умножения)
print(type(immutable_var_1))
#print(type[1, 2]) - хотел понять считает ли программа этот элемент как список, но в таком контексте кортеж изменяем
print(immutable_var_1)
immutable_var_1[0][0] = 7
print(immutable_var_1)

print(" ")

immutable_var_1[0][1] = '3'
print(immutable_var_1)

print(" ")

#immutable_var_1.append['3'] - в кортеж нельзя добавлять по причине его неизменяемости
#immutable_var_1.append('3')
#immutable_var_1.remove(1)
#print(immutable_var_1)

print(" ")

immutable_var_1 = ([1, 2], 3, 4, 5)
print(type(immutable_var_1))
print(immutable_var_1)
#immutable_var_1[0][2] = '3'
#print(immutable_var_1)

print(" ")

immutable_var_2 = (1, 2, 3, 4, 5)
print(type(immutable_var_2))
print(immutable_var_2)
#immutable_var_2[0][0] = 7 - без элемента с квадратными скобами, который я полагаю квалифицируется как список, нельзя произвести замену
#print(immutable_var_2)

print(" ")

mutable_list = [1, 2, 3, 4, "1", "2", "3", "4", True, False]
print(type(mutable_list))
print(mutable_list)
#print(int(mutable_list))

print(" ")

#mutable_list_1 = [1, 2, 3, 4]
#print(type(mutable_list_1))
#print(int(mutable_list_1))
#print(mutable_list_1)

print(" ")

print(type(mutable_list[5]))
print(mutable_list[5])
print(type(mutable_list[3]))
print(mutable_list[3])
mutable_list.append("slovo")
print(mutable_list)
mutable_list[0] = 999
print(mutable_list)
mutable_list.remove(999)
print(mutable_list)
print(len(mutable_list))