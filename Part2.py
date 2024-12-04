list1 = []
list2 = []

total = 0
with open('input.txt', 'r') as file:
    for line in file:
        row = line.split('   ')
        list1.append(int(row[0]))
        list2.append(int(row[1]))

for num in list1:
    total = total + (num * list2.count(num))

print(total)