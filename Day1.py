# list1 = [3,4,2,1,3,3]
# list2 = [4,3,5,3,9,3]

list1 = []
list2 = []

total = 0
with open('input.txt', 'r') as file:
    for line in file:
        row = line.split('   ')
        list1.append(int(row[0]))
        list2.append(int(row[1]))

list1.sort()
list2.sort()

total = 0

for index, num1 in enumerate(list1):
    total = total + abs(num1 - list2[index])

print(total)