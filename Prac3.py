#Find Captain Room Number
K = int(input())
Rooms = list(map(int,input().split()))
a=set()
b=set()
for room in Rooms:
    if room not in a:
        a.add(room)
        b.add(room)
    else:
        b.discard(room)
print(b)
print('''Created by: Apurva Bhatt
Id:D21ce173''')
