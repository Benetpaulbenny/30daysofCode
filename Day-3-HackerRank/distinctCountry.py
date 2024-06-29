#Pr 1: set.add()
no = int(input())
thisSet = set()
for x in range(no):
    thisSet.add(input())
print(len(thisSet))

#Pr 2: hashing
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))

#Pr 3: Substring count
def count_substring(string, sub_string):
    left = 0
    right = len(sub_string)
    count_var = 0
    while right < len(string)+1:
        if string[left:right] == sub_string:
            count_var = count_var + 1
        left = left + 1
        right = right + 1
    return count_var
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

#Pr 4: itertools.product
from itertools import product

a = map(int, input().split())
b = map(int, input().split())
c = list(product(a,b))
for i in range(len(c)):
    print(c[i], end=' ')