# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10


a = input("Введите количество журавликов: " )
y=int(a)%6
if y!=0:
    print("такое количество журавликов не могло получиться)")
else: 
    part=int(int(a)/6)
    print(str(part) + " "+str(part*4 )+ " "+str(part))