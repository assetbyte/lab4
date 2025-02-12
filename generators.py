#1

def square(n):
    for i in range(n + 1):
        yield i ** 2  # остановка чтоб не хранить данные в памяти
n = int(input())
for i in square(n):
    print(i)
"""
gen = square(n)
print(next(gen))  
print(next(gen))  
print(next(gen))
"""

#2
def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i
a = int(input()) 
even = even_numbers(a)
print(", ".join(str(i) for i in even))

#3

def divisible(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

b = int(input())
divide = divisible(b)
for i in divide:
    print(i)
    
#4

def kvadrati(c,d):
    for i in range(c,d+1):
        yield i**2
c = int(input())
d = int(input())
kvadratik = kvadrati(c,d)
for i in kvadratik:
    print(i)
    
    
#5

def down(n):
    while n>=0:
        yield n 
        n-=1
e = int(input())
for i in down(e):
    print(i)