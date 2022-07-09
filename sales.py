#Sales Tax Challenge
#Sales Tax Challenge – Task Two (Day 1)

 #A painting company has determined that for every 115 square feet of wall space, one gallon of paint and eight hours of labor will be required. The company charges $20.00 per hour for labor. Write a program that asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon. The program should display the following data: 
#• The number of gallons of paint required 
#• The hours of labor required 
#• The cost of the paint 
#• The labor charges 
#• The total cost of the paint job

squre_feet = float(input("\n\nEnter the squre feet of the wall to be painted: "))
price = float(input("\n\nEnter the price of the paint per gallon: "))

#The number of gallons of paint required
gallons = squre_feet  / 115
print("\nThe number of gallons of paint required is: " , gallons)

#The hours of labour required
hours = (squre_feet * 8) / 115
print("\nThe hours of lobour required is: " , hours)

#The cost of the paint
cost = price * gallons
print("\nThe cost of the paint is: " , cost)

#The labour charges
labour = hours * 20
print("\nThe labour charges is: " , labour)

#Total cost of painting job
total_cost = labour + cost
print("\nThe total cost of painting job is : $" , total_cost)

