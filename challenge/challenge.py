#!/usr/bin/python3

# using a mix of dictionary and lists
dream_cars = {"car_1": "bugatti", "car_2": "ferarri"}
boats = ["Pinta", "Nina", "Santa-Maria"]

#print("The " + dream_cars['car_1'] + " was on the " + boats[2] + ", and the " + dream_cars['car_2'] + " was on the " + boats[0] + ".")
print("The " + dream_cars['car_1'].capitalize() + " was on the " + boats[2] + ", and the " + dream_cars['car_2'].capitalize() + " was on the " + boats[0] + ".")

# use the .format function
print("the {} was on the {}, and the {} was on the {}.".format(dream_cars['car_1'], boats[2], dream_cars['car_2'], boats[0]))
