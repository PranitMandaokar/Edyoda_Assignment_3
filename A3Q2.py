# Write a Python program to reverse a string using function :

def reverse(sample):
    rev =""
    for i in range(len(sample)):
        rev = sample[i] + rev
    return rev

string_1 = input("Enter the string : ")

string_reverse = reverse(string_1)

print(string_reverse)
