'''
#Dictionary comprehension of even numbers and their squares from 1 to 10.
even_squares={i:i*i for i in range(1,11) if i%2==0}
print(even_squares)

'''

'''
#Swapping keys and values in a dictionary
student={
    "A":90,
    "B":80,
    "C":70,
}
swapped={value: key for key, value in student.items()}
print(swapped)

'''
