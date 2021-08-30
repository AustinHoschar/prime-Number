#Didn't start this assignment before I got to school so I didnt do most of this.
num = int(input("Enter a number: "))

flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            
            flag = True
            break

if flag:
    print(num, "is not a prime number")
    print()
else:
    print(num, "is a prime number")
    print("Divisable by 1 and " + num + ".")
