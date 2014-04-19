#!/usr/bin/env python
import sys

def calorieCalculator(gender, weight, height, age, activity, goal):
	#Constant dictionary for transforming BMR into daily calories
	activityArray = [1.2,1.375,1.55,1.725,1.9]
	goalArray = [-500,0,500]

	#Calculate the BMR
	if gender == 'male' :
		bmr = 66 + (13.7 * float(weight)) + ( 5 * float(height)) - (6.8 * float(age))
	if gender == 'female':
		bmr = 666 + (9.6 * float(weight)) + ( 1.8 * float(height)) - (4.7 * float(age))

	#Calculate rmr from bmr and activity
	rmr = bmr*activityArray[int(float(activity))]+goalArray[int(float(goal))]
	
	#Calculate daily macronutrients
	dailyProteins = 1.5*2.2*int(float(weight))
	remainingCalories = rmr - dailyProteins*4
	dailyCarbs = remainingCalories/2/4
	dailyFats  = remainingCalories/2/9

	#Calculate meal macronutrients
	mealCarbs = dailyCarbs/5
	mealProteins = dailyProteins/5
	mealFats = dailyFats/5

	return int(rmr), int(mealCarbs), int(mealProteins), int(mealFats)


user_gender = sys.argv[1]
user_weight = sys.argv[2]
user_height = sys.argv[3]
user_age = sys.argv[4]
user_activity = sys.argv[5]
goal = sys.argv[6]

print calorieCalculator(user_gender,user_weight,user_height,user_age,user_activity,goal)
