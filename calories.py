#Day 3: Challenge Task Two (Day 3)
#2. Calories from Fat and Carbohydrates A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation, she asks members for the number of fat grams and carbohydrate grams that they consumed in a day. Then, she calculates the number of calories that result from the fat, using the following formula: 
#Calories from fats fat grams * 9 
#Next, she calculates the number of calories that result from the carbohydrates, using the following formula: 
#Calories from carbs carb grams * 4 
#The nutritionist asks you to write a program that will make these calculations.


#variable declaration

fat_grams = int(input("Enter fats consumed: "))
carb_grams = int(input("Enter cabohydrates consumed:  "))

#Calculating the total number of calories from the user input using the given formula

#formula for calculating calories from fat input

calories_from_fat  =  fat_grams *  9

#formula for calculating calories from carbohydrate input

calories_from_carb = carb_grams * 4

#output from the calculation
print("Calories from fat: " , calories_from_fat)
print("Calories from cabohydrates: " , calories_from_carb)


