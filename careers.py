#Challenge - Task Two (Day 2)
#2. Write a python program that takes user inputs and determines what career the user should learn.
#Requirements:
#Store career options in a list or in variables.
#Store career advices in a list.
#Store career questions in a list.
#Use conditional statements that determines the user selected choice.
#When a wrong input is entered the program should print out an error message.
#When all the questions are done the program should determine which career the user should venture in and program should terminate.




careers = [

    "Medicine",
    "Engineering",
    "Government policy",
    "Human resources",
    "Mechanical Engineering",
    "Law",
    "Accounting",
    "Marketing",
    "Performing Arts",
    "Creative Arts",
    "International Relations",
    "Philosophy",
    "Nursing",
    "Environmental Conservation",
    "Teaching",
    "Software Engineering",
    "Pure Arts",
    "Creative Arts"
]

career_advices = [
    "You will definitely succeed in this career because of your interest in Humanities, your focus on people and your good grades",
    "You will definitely succeed in this career because of your interest in Humanities, your focus in thematic processes and your good grades",
    "You will definitely succeed in this career because of your interest in Sciences, your focus on people and your good grades",
    "You will definitely succeed in this career because of your interest in Sciences, your focus in thematic processes and your good grades",
    "You will definitely succeed in this career because of your interest in Arts, your focus on people and your good grades",
    "You will definitely succeed in this career because of your interest in Arts, your focus in thematic processes and your good grades",
]




career_questions = [

    "Which career field are you interested in? \n (a) Humanities \n (b) Sciences \n (c) Arts \n \n Enter a, b or c:_",
    "\n In your career of choice, in which focus area would you perform best? \n (a) People \n (b) Process \n Enter a, or b:_",
    "\n Select the range of your Highschool average score \n (a) 100-80 \n (b) 79-60 \n (c) 59-0 \n Enter a, b or c:_ "
]   

career_field = input (career_questions[0])
focus_area = input (career_questions[1])
score = input(career_questions[2])



if career_field == "a" and focus_area == "a" and score == "a":
    print ("You should pursue a career in", careers[5])
elif career_field == "a" and focus_area == "a" and score == "b":
    print ("You should pursue a career in", careers[7])
elif career_field == "a" and focus_area == "a" and score == "c":
    print ("You should pursue a career in", careers[3])
elif career_field == "a" and focus_area == "b" and score == "a":
    print ("You should pursue a career in", careers[2])
elif career_field == "a" and focus_area == "b" and score == "b":
    print ("You should pursue a career in", careers[10])
elif career_field == "a" and focus_area == "b" and score == "c":
    print ("You should pursue a career in", careers[11])
elif career_field == "b" and focus_area == "a" and score == "a":
    print ("You should pursue a career in", careers[0])
elif career_field == "b" and focus_area == "a" and score == "b":
    print ("You should pursue a career in", careers[12])
elif career_field == "b" and focus_area == "a" and score == "c":
    print ("You should pursue a career in", careers[14])
elif career_field == "b" and focus_area == "b" and score == "a":
    print ("You should pursue a career in", careers[1])
elif career_field == "b" and focus_area == "b" and score == "b":
    print ("You should pursue a career in", careers[15])
elif career_field == "b" and focus_area == "b" and score == "c":
    print ("You should pursue a career in", careers[13])
elif career_field == "c" and focus_area == "a" and score == "a":
    print ("You should pursue a career in", careers[8])
elif career_field == "c" and focus_area == "a" and score == "b":
    print ("You should pursue a career in", careers[14])
elif career_field == "c" and focus_area == "a" and score == "c":
    print ("You should pursue a career in", careers[16])
elif career_field == "c" and focus_area == "b" and score == "a":
    print ("You should pursue a career in", careers[17])
elif career_field == "c" and focus_area == "b" and score == "b":
    print ("You should pursue a career in", careers[17])
elif career_field == "c" and focus_area == "b" and score == "c":
    print ("You should pursue a career in", careers[17])
else :
    print ("Invalid input, check that you have entered your answers correctly")


if career_field == "a" and focus_area == "a":
    print (career_advices[0])
elif career_field == "a" and focus_area == "b":
    print (career_advices[1])
elif career_field == "b" and focus_area == "a":
    print (career_advices[2])
elif career_field == "b" and focus_area == "b":
    print (career_advices[3])
elif career_field == "c" and focus_area == "a":
    print (career_advices[4])
elif career_field == "c" and focus_area == "b":
    print (career_advices[5])