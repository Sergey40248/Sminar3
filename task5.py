#Задайте число. 
# Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
 
n =  int(input("Номер элемента ряда Фибоначчи: "))
list = [0, 1, 1]
fib1 = 1
fib2 = 1
fib_sum = 0 
i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    list.append(fib2)
    i += 1

fib1,fib2 = 0, 1
i = 0

while i < n:
    list.insert(0, fib2)
    fib_sum = fib1 - fib2
    fib1 = fib2
    fib2 = fib_sum
    i += 1
    
 
print("Значение этого элемента:", list)