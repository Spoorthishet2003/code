// A recursive implementation to calculate terms in the Fibonacci sequence. 
   
def fn(n):
    if n <= 2:
        return n - 1
    else:
        return fn(n-1) + fn(n-2)

try:
    num = int(input("Enter a number : "))
    if num > 0:
        print(f' fn({num}) = {fn(num)}')
    else:
        print("Input should be greater than 0")
except ValueError:
    print("Try with numeric value")
