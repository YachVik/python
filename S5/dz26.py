# напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

a = int(input("A = " ))
b = int(input("B = " ))
i=0
def st(a, b):
   
    # if b==0:
    #     return 1
    if b==1:
        return a
    else:
        return a*st(a, b-1)

print(st(a, b))
