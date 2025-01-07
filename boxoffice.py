import random
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
print(f"Integer 1: {num1}")
print(f"Integer 2: {num2}")
x=int(input("Enter the sum "))
if x==num1+num2:
    print("Congratualtions")
else:
    print("Wrong!!")
    print("Sum=",num1+num2)