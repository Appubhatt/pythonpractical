# Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
from collections import Counter

a = [1, 5, 10, 5, 7, 5, 10, 13, 5]
b = (1, 5, 6, 5, 3, 1, 1)
c = {1: 10, 2: 2, 3: 7, 4: 2, 5: 6}
for common in (a, b):
    occurence_count = Counter(common).most_common(1)[0][0]
    print(f"{occurence_count} repeated {common.count(occurence_count)} times")

value, count = Counter(c.values()).most_common(1)[0]

print(f"{value} repeated {count} times")
print('''Created by: Apurva Bhatt
Id:D21ce173''')
