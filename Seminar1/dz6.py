# # Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и 
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

a = input("Введите номер проездного билетика:" )
if int(a)%100000>=0:
    sum13=0
    sum36=0
    y=int(a)/2
    for i in a [:3]:
        sum13 +=int(i)
        # print(sum13)
    for i in a [3::]:
        sum36 +=int(i)
        # print(sum36)
    if sum13==sum36:
        print("Счатливый билетик!!")
    else:
        print("Билет не счастливый(")

else:
    print ("У билетика 6 цифр")