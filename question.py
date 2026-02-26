# 1️⃣ Question

# Print the sum of the values from 1 to 5 using the print() function.

print("The sum of 1 to 5 is:", 1+2+3+4+5)
# 2️⃣ Question

# Find the sum of odd numbers between 1 and 100 and print the sum.


N = 1
S = 0

while N <= 100:
    S += N
    N += 2

print("Sum of odd numbers from 1 to 100 is:", S)
# 3️⃣ Question

# Write a program that receives a positive integer and tells whether it is odd or even.


num = int(input("Enter a positive integer: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
# 4️⃣ Question

# Print decorative output using * and #.


print('*' * 5)
print('# ' * 5)
# 5️⃣ Question

# Save name and address in variables and print them.


name = "Imran"
address = "Delhi, India"

print("Name:", name)
print("Address:", address)
# 6️⃣ Question

# Take two integers as input and print them from smallest to largest.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    print(a, b)
else:
    print(b, a)
# 7️⃣ Question

# Write a program using compound conditional expression (if statement).


answer = int(input("Enter 0 or 1: "))

if answer == 0:
    print("You entered zero")
elif answer == 1:
    print("You entered one")
else:
    print("Invalid input")
# 8️⃣ Question

# Print prime and composite numbers from 2 to 12 using nested for loop.


for num in range(2, 13):
    for i in range(2, num):
        if num % i == 0:
            print(num, "Composite")
            break
    else:
        print(num, "Prime")
# 9️⃣ Question

# Find all Armstrong numbers between 100 and 999.


for num in range(100, 1000):
    a = num // 100
    b = (num // 10) % 10
    c = num % 10
    
    if num == a**3 + b**3 + c**3:
        print(num)
# 🔟 Question

# Combine two lists using nested loops.


l1 = ["Hello", "Good"]
l2 = ["Morning", "Evening"]

for i in l1:
    for j in l2:
        print(i, j)
# 1️⃣1️⃣ Question

# Add a new item to a dictionary and print it.


person = {"Name": "Imran", "Age": 20}

person["Father"] = "John Doe"

print(person)
# 1️⃣2️⃣ Question

# Move the largest value in the list to the last using swapping (without temp variable).

lst = [3, 8, 2, 10, 5]

for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]

print(lst)
# 1️⃣3️⃣ Question

# Convert 2D array into 1D array.


a = [[1,2],[3,4],[5,6]]
new_list = []

for row in a:
    for item in row:
        new_list.append(item)

print(new_list)
# 1️⃣4️⃣ Question

# Print average score from dictionary using values() and len().

maria = {'korean': 94, 'english': 88, 'math': 90, 'science': 85}

avg = sum(maria.values()) / len(maria)
print("Average:", avg)
# 1️⃣5️⃣ Question

# Use deepcopy() to copy dictionary and check with is operator.

import copy

school = {"class1": {"student": "Imran"}}
school2 = copy.deepcopy(school)

print(school is school2)
# 1️⃣6️⃣ Question

# Extract math scores using zip() and calculate average.


scores = (
    ('Hyun', 88, 95, 90),
    ('Jin', 92, 90, 88),
    ('Min', 85, 88, 91),
    ('Lee', 90, 87, 93)
)

names, eng, math, sci = zip(*scores)

avg_math = sum(math) / len(math)

print("Average Math Score:", avg_math)