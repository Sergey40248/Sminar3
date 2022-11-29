#Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] ->  элементы 3 и 9, ответ: 12

quantity = int(input('input quantity elements:  '))
array = []
for i in range(quantity):
    array.append(int(input('enter of numbers:  ')))
sum_odd = 0
for j in range(len(array)):
    if j % 2 != 0:
        sum_odd += array[j]
    else:
        j +=1
print(array)
print(sum_odd)