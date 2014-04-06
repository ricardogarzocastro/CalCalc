#!/usr/bin/env python
import sys

def calorieCalculator(gender, weight, height, age, activity, goal):
	#Calculate the BMR
	if gender == 'male' :
		bmr = 66 + (13.7 * weight) + ( 5 * height) - (6.8 * age)
	if gender == 'female':
		bmr = 665 + (9.6 * weight) + ( 1.8 * height) - (4.7 * age)

	return bmr


user_gender = sys.argv[1]
user_weight = sys.argv[2]
user_height = sys.argv[3]
user_age = sys.argv[4]
user_activity = sys.argv[5]
user_goal = sys.argv[6]

print calorieCalculator(user_gender,user_weight,user_height,user_age,user_activity,user_goal)

#print calorieCalculator()