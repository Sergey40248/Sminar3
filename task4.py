#Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
#Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

n = int(input('enter the number to convert to binary:  '))
number = n
bin_num = []

while n > 0:
      bin_num.append(str(n % 2))
      n //= 2

print((f'{number} -> {"".join(bin_num)[::-1]}'))
