# Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

D1={"Name":"Apurva","Sem":4,"College":"CSPIT"}
D3={"4":6,"5":8,"6":4}
D2={"1":2,"2":3,"3":4}
D4={}
def merge(DS,DD):
    return (DD.update(DS))
merge(D1,D4)
print(D4)
merge(D3,D4)
print(D4)
merge(D2,D4)
print(D4)
print('''Created by: Apurva Bhatt
Id:D21ce173''')
