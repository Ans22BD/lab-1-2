def square_numbers(n):
    for i in range(n+1):
        yield i ** 2
    
N = 10
for num in square_numbers(N):
        print(num,end = " ")
    