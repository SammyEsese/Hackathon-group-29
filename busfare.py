import datetime

#Write a program that does the following:
#1. Gets today&#39;s date and stores it in a variable &#39;date&#39;
#2. Uses today&#39;s date to get the name on the day of the week written in short form with the
#first letter capitalized eg. &#39;Fri&#39; if today were Friday and assigns it a variable &#39;day&#39;
#3. Uses if statements to determine the today&#39;s fare following these bus fare schedule:
# Monday - Friday --&gt; 100
# Saturday --&gt; 60
# Sunday --&gt; 80
#4. Prints the results in this format
#Date: 2022-07-05
#Day: Tue
#Fare: 100



date = datetime.datetime.now().strftime("%Y-%m-%d" )
day = datetime.date.today().strftime("%a")
fare = [100, 60, 80]
if day == "Mon":
    charges = fare[0]
elif day == "Tue":
    charges = fare[0]
elif day == "Wed":
    charges = fare[0]
elif day == "Thu":
    charges = fare[0]
elif day == "Fri":
    charges = fare[0]
elif day == "Sat":
    charges = fare[1]
else:
    charges = fare[2]

print("Date: ", date)
print("Day: ", day)
print("Fare: ", charges)
