# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
#a = int(input("число а"))
#b = int(input("число b"))

# list1=input("list1").split()
# list2=input("list2").split()
list3=[]
def dict(l1, l2):
    if len(l1)<2 or len(l2)<2:
        if len(l1)<2  and l2.count(l1[0])>0:
            list3.append(l1[0])
            return list3
        elif len(l2)<2  and l1.count(l2[0])>0:
            list3.append(l2[0])
            return list3
    else:
        # print(l2+l1)
        for i in range(len(l1)):
            if l2.count(l1[i]):
                list3.append(l1[i])
        return list3

def sort(list_):
    if len(list_)<2:
        return list_
    else:
        pivot=list_[0]
        left=[i for i in list_[1:] if list_[i]<=pivot]
        right=[i for i in list_[1:] if list_[i]>pivot]
        return sort(left)+[pivot]+sort(right)
print(sort(dict([3,2,1],[2,1])))