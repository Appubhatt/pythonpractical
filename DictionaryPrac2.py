#  Write a Python script to merge two Python dictionaries.
D1={"Name":"Apurva","Sem":"4","College":"CSPIT"}
D2={"1":"2","2":"3","3":"4"}
D3={}
print(D1.update(D2))
for d in (D1,D2) :
    D3.update(d)
print(D3)
print('''Created by: Apurva Bhatt
Id:D21ce173''')
