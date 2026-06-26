'''
#Dictionary of even numbers and their squares from 1 to 10.
even={}
for i in range(1,11):
    if i%2==0:
        even[i]=i*i
print(even)

'''

'''
#Swapping keys and values in a dictionary
student={
    "A":90,
    "B":80,
    "C":70,
}

swapped={}
for key, value in student.items():
    swapped[value]=key
print(swapped)

'''