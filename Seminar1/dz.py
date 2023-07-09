k = 'ноутбук'

# Введите ваше решение ниже
list1=['AEIOULNSTR','DG','BCMP','FHVWY','K','JX','QZ']
value=[1,2,3,4,5,8,10]
list2=['D', 'G']
list3=['B', 'C', 'M', 'P']
list4=['F', 'H', 'V', 'W', 'Y']
list8=['J', 'X']
list10=['Q', 'Z']
dictEn = dict(zip(list1,value))

listRu1=['АВЕИНОРСТ','ДКЛМПУ','БГЁЬЯ','ЙЫ','ЖЗХЦЧ','ЖЗХЦЧ','ШЭЮ','ФЩЪ']

listRu2=['ДКЛМПУ' ]
listRu3=['БГЁЬЯ']
listRu4=['Й', 'Ы']
listRu5=['Ж', 'З', 'Х', 'Ц', 'Ч']
listRu8=['Ш', 'Э', 'Ю']
listRu10=['Ф', 'Щ', 'Ъ']
dictRu = dict(zip(listRu1,value))

#dictRu = {listRu1: 1, listRu2: 2, listRu3: 3, listRu4: 4, listRu5:5,listRu8: 8, listRu10: 10}

sum=0
k=k.upper()
check=0
#print(dictRu)
#if k in dictEn:
    #print('k- английская буква')
for i in k:
    for item in range(len(list1)):
        if i in list1[item]:
            sum+=list(dictEn.values())[item]
    if sum==0 or check==1:
        for item in range(len(listRu1)):
            if i in listRu1[item]:
                sum+=list(dictRu.values())[item]
                check=1
   
#else:
 #   for i in k:
  #      sum += dictRu[i]
print(sum)