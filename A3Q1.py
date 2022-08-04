#  Write a Python function to sum all the numbers in a list.

# logic : 1 with predfined input

def list_sum(sample_list):
    sum = 0
    for element in sample_list:
        sum = sum + element
    return sum
 
list_1 = [8,2,3,0,7]
print(f"List : {list_1}")
print(f"Sum : {sum(list_1)}")   

# logic : 2 with user input

l = []
a = int(input("enter the number of element in the list : "))
i = 0
while i < a:
    num = int(input("Enter the number : "))

    l.append(num)
    i += 1

print(f"list : {l}")
print(f"Sum : {sum(l)}")

