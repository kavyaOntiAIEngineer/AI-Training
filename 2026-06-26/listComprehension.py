'''
# Numbers from 1 to 10 using list comprehension
numbers=[i for i in range(1,11)]
print(numbers)

'''

'''
# Even numbers using list comprehension
even=[i for i in range(1,11) if i%2==0]
print(even)

'''
'''
# Uppercase fruits using list comprehension
fruits=["apple","banana","cherry"]
upper=[fruit.upper() for fruit in fruits]
print(upper)

'''
#Flattening a matrix using list comprehension
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]

]
flat=[item for row in matrix for item in row]
print(flat)
