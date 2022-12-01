#Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] ->  элементы 3 и 9, ответ: 12
print('enter numbers separated by spaces: ')
array = [int(value) for value in input(). split()]

s = []   # для вывода как в примере
sum_odd = 0
for j in range(len(array)):
    if j % 2 != 0:
        sum_odd += array[j]
        s += list(str(array[j]))
    
    else:
        j +=1

# для вывода как в примере, работает только на однозначных ?
print(f'{array} -> элементы {" и ".join(s)} ответ {sum_odd}')