#!/usr/bin/env python
import sys

def calorieCalculator(gender, weight, height, age, activity):
	#Constant dictionary for transforming BMR into daily calories
	activityMultiplier = [1.2,1,375,1.55,1.725,1.9]
	
	#Calculate the BMR
	if gender == 'male' :
		bmr = 66 + (13.7 * float(weight)) + ( 5 * float(height)) - (6.8 * float(age))
	if gender == 'female':
		bmr = 666 + (9.6 * float(weight)) + ( 1.8 * float(height)) - (4.7 * float(age))

	#Calculate rmr from bmr and activity
	rmr = bmr*activityMultiplier[int(float(activity))]
	
	dailyProteins = 1.5*2.2*int(float(weight))
	remainingCalories = rmr - dailyProteins*4
	dailyCarbs = remainingCalories/2/4
	dailyFats  = remainingCalories/2/9

	





	return rmr, dailyProteins, dailyCarbs, dailyFats


user_gender = sys.argv[1]
user_weight = sys.argv[2]
user_height = sys.argv[3]
user_age = sys.argv[4]
user_activity = sys.argv[5]

print calorieCalculator(user_gender,user_weight,user_height,user_age,user_activity)
