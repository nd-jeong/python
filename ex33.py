# i = 0
# numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")


# print("The numbers: ")

# for num in numbers:
#     print(num)

numbers = []

def loop_function(x, y):
    i = 0

    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + y
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

num = int(input("> "))
num2 = int(input("> "))
loop_function(num, num2)
print("The numbers: ")

for num in numbers:
    print(num)