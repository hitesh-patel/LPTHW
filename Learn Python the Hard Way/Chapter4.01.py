cars = 100
space_in_a_car = 4.0
drivers = 30
passegers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car

print "There are", cars, " cars available."
print "There are only", drivers, "drivers avaiolable."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."

