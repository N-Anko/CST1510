i = 1
while i <=10:
    print(i, end=" ")
    i += 1
print()
for j in range(1, 11):
    print(j, end=" ")
print()
def greeting(name):
    print("Hi" , name)
# name = input("Enter your name: ")
greeting("Neel")
greeting("Hameed")
x = "ali"
greeting(x)
def total(a,b,c):
    sum = a+b+c
    print(f"Total is: {sum}")
total(20,30,10)
def greater(a,b):
    if a>=b:
        return a
    else:
        return b
n1 = 10
n2 = 15
gr = greater(n1,n2)
print(f"The greater number is: {gr}")