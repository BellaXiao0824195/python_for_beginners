
#1. Change "green" to "yellow". and add "purple" to list
colors = ["red", "green", "blue"]
colors[1] = 'yellow'
colors.append("purple")
print(colors)

#2. remove cat from list 
animals = ["dog", "cat", "rabbit", "hamster"]
animals.pop(2)
print(animals)

#3. get length of the list below
numbers = [1, 2, 3, 4, 5]
len(numbers)
#4. generate a list that has numbers from 1 to 10
list_10 = list(range(1,11))
print(list_10)

#5. return first 5 numbers from the list generated from 4 above
first5num = list_10[:4]
print(first5num)

#6. create a list of the first 10 square numbers using list comprehension.
square_list = [x**2 for x in range(1,11)]
print(square_list)

square_list = []
for x in range(1,11):
    square_list.append(x**2)

print(square_list)
