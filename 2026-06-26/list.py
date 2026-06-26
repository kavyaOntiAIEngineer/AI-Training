'''
#List of numbers from 1 to 10
numbers=[]
for i in range(1,11):
    numbers.append(i)
print(numbers)

'''

'''
#Even numbers without using list comprehension
even=[]
for i in range(1,11):
    if i%2==0:
        even.append(i)
print(even)

'''

'''
# Uppercase fruits without using list comprehension
fruits=["apple","banana","cherry"]
upper=[]
for fruit in fruits:
    upper.append(fruit.upper())
print(upper)

'''

#Flattening a matrix without using list comprehension
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
flat=[]
for row in matrix:
    for item in row:
        flat.append(item)
print(flat)
