'''Lapindrome is defined as a string which when split in the middle, gives two
halves having the same characters and same frequency of each character. If there
1,2 are odd number of characters in the string, we ignore the middle character and
check for lapindrome. For example gaga is a lapindrome, since the two halves ga
and ga have the same characters with same frequency. Also, abccab, rotor and
xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome.
The two halves contain the same characters but their frequencies do not match.
Your task is simple. Given a string, you need to tell if it is a lapindrome.'''
num = int(input())
s1 = ""
s2 = ""
for i in range(num):
    s =input()
    l = len(s)
    mid = int(l / 2)
    if(l%2==0):
        s1 = s[:mid]
        s2 = s[mid:]
    else:
        s1 = s[:mid]
        s2 = s[mid+1:]
    l1 = list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()

    if(l1==l2):
        print("YES")
    else:
        print("NO")