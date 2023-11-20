//Python program to check whether a given number is palindrome or not and also count the number of occurrences of each digit in the input number.

value = input("Enter a value : ")  
if value == value[::-1]:
    print("Palindrome")           
else:
    print("Not Palindrome")
    
counted_dict = Counter(value)
for key in sorted(counted_dict.keys()):
    print(f'{key} appears {counted_dict[key]} times');

"""
##Alternate way to count appearances##
for i in range(10):
    if value.count(str(i)) > 0:
        print(f'{str(i)} appears {value.count(str(i))} times')



