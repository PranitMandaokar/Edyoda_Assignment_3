# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def upperCount(sample):
    m = 0
    for i in range(len(sample)):
        if (sample[i].isupper()) == True:
            m += 1
    return m   

def lowerCount(sample):
    m = 0
    for i in range(len(sample)):    
        if (sample[i].islower()) == True:
           m += 1   
    return m   

string_1 = input("Enter the string : ")

print(f'No. of Upper case characters : {upperCount(string_1)}')
print(f'No. of Lower case Characters : {lowerCount(string_1)}')




