def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def pizza_slices(number_of_pizzas, number_of_sodas):
    print(f"There are {number_of_pizzas} pizzas!")
    print(f"There are also {number_of_sodas} sodas!")
    print("We should have a party!\n")

pizza_slices(10, 20)

num_pizzas = 10
num_sodas = 25

pizza_slices(num_pizzas, num_pizzas * 10)
