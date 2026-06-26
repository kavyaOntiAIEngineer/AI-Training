'''
# Generator function
def numbers():
    yield 1
    yield 2
    yield 3

gen=numbers()
print(next(gen))
print(next(gen))
print(next(gen))
'''

def squares():
    for i in range(1,6):
        yield i*i
for value in squares():
    print(value)

