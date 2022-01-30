# Today's date?
# December 7th, 2020
# Breakfast calories?
# 250
# Lunch calories?
# 300
# Dinner calories?
# 500
# Snack calories?
# 150
# Calorie content for December 7th, 2020: 1200

print("Today's date?")
date = input()

print("Breakfast calories?")
breakfast = int(input())

print("Lunch calories?")
lunch = int(input())

print("Dinner calories?")
dinner = int(input())

print("Snack calories?")
snack = int(input())

daily_calories = breakfast + lunch + dinner + snack

print("Calorie content for " + date + ": " + str(daily_calories))


