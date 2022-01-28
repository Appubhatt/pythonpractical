size=int(input())
list1=[]
for a in range(1,size+1):
    ele=int(input())
    list1.append(ele)
print(list1)
Largest=list1[0]
SecLar=list1[0]
for i in range(1,size):
    if list1[i] > Largest:
        SecLar = Largest
        Largest = list1[i]
    elif list1[i] > SecLar and Largest != list1[i]:
        SecLar = list1[i]
print(SecLar)