#Personality test program - Task One (Day 2)

#Book Club Points Serendipity Booksellers has a book club that awards points to its customers based on the number of books purchased each month. The points are awarded as follows:
# • If a customer purchases 0 books, he or she earns 0 points. 
#• If a customer purchases 1 book, he or she earns 6 points. 
#• If a customer purchases 2 books, he or she earns 16 points.
# • If a customer purchases 3 books, he or she earns 32 points. 
#• If a customer purchases 4 or more books, he or she earns 60 points. 
#Write a program that asks the user to enter the number of books that he or she has purchased this month and displays the number of points awarded

greetings = "Welcome to Serendipity book sellers, win points for any book you buy."
print(greetings)


books = int(input("Enter the number of books you have bought this month:"))
if books == 0:
    print("You have been awarded 0 points")
elif books == 1:
    print("You have been awarded 6 points")

elif books == 2:
    print("You have been awarded 16 points")

elif books == 3:
    print("You have been awarded 32 points")

elif books >=4:
    print("You have been awarded 60 points")

else:
    print("Invalid Input, input must be an integer")





