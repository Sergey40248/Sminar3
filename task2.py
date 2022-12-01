#Напишите программу, которая найдёт произведение пар чисел 
# списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
#Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

print('enter numbers cherez spaces: ')
array = [int(value) for value in input(). split()]

sum = []
x = -1
a = 0
sr = (len(array) / 2) % 1
if sr != 0:
    for i in range(len(array)):
        sum.append(array[i] * array[x])
        x -=1
        
        if i > len(array) / 2 - 1:
            break
elif sr == 0:
    for i in range(len(array)):
        sum.append(array[i] * array[x])
        x -=1
        
        if i > len(array) / 2 - 2:
            break

print(sum)        
    




  

