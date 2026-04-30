# while loop

i = 0

while (i <= 9):
    i += 1
    print("The value of i is :", i)
print("The loop is end.")    


# Reverse

count = 10

while(count >= 1):
    count -= 1
    print(count)

# Multiplication table of n numbers

n = int(input("enter the number:"))

i = 0

while(i < 10) :
    print( n * (i+1))
    i += 1
    
# break

i = 1

while(i <= 10) :
    if(i % 6 == 0) :
        break
    print(i)
    i += 1
print("outside loop now....")

# continue

i = 1
while(i <= 10) :
    if (i % 3 == 0) :
        i += 1
        continue
    print(i)
    i += 1

print("outside loop...")

i = 0

while(i < 10) :
    i += 1
    if(i % 2 == 0) :
        continue
    print(i)


# for loop

string = "Hello"

# in => membership operator

for var in string:
    print(var)

for i in range(5):
    print(i) 


# count the number of i

word = "Artificial intelligence"

count = 0

for ch in word :
    if(ch == 'i'):
        count += 1
print("Count of i =", count)        


# Count vowels

word = "Data Analytics"
count = 0

for ch in word:
    if(ch == 'a'or ch =='i'or ch== 'o'or ch ==  'e'or ch == 'u'):
        count += 1
print("The vowel count is :", count)  


# Print sum of n natural number

n = int(input("enter the number :"))

sum = 0

for i in range(1, n + 1) :
    sum += i
print("Sum = ", sum)    