# Sets cars value as 100
cars = 100
# Sets space_in_a_car's value as 4.0
space_in_a_car = 4.0
# Sets drivers value as 30
drivers = 30
# Sets passengers value as 90
passengers = 90
# Sets cars_not_driven as 100 - 30
cars_not_driven = cars - drivers
# Sets cars_driven value equal to drivers variable
cars_driven = drivers
# Sets carpool_capacity as cars_driven multiplied by space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# Sets average_Passengers_per_car as passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")