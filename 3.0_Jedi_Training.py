# 3.0 Jedi Training (20pts)  Name: Logan Knisley


# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name. (1pt)
name = input("Enter your name: ")
print("Bonjour " + name)

# 2. Write a program where a user enters a base and height and you print the area of a triangle. (1pt)
base = int(input("What is the triangle's base? "))
height = int(input("What is the triangle's height? "))
area = base * (height / 2)
print("The area is", area)

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference. (1pt)
radius = int(input("What's the radius of a circle"))
cir = 2 * 3.141592 * radius
print("The circumference is", cir)

# 4. Ask a user for an integer and then print the square root. (1pt)
un_sqrt = int(input("Enter your integer: "))
print(un_sqrt ** 0.5)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next. (1pt)
mass = float(input("Enter your mass: "))
acc = float(input("Enter your acceleration: "))
force = mass * acc
print(force)
print("Do you get it?")

'''
6. TEMPERATURE PROGRAM (5pts)
-------------------
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.

Test your program with the following data:

In: 32  Out: 0
In: 212  Out: 100
In: 52  Out: 11.1
In: 25  Out: -3.9
In: -40  Out: -40

'''
witty_lines = ["Have fun biotic thermometer",
               "Big fan of temperature?",
               "How can checking the heat be enjoyable to you",
               "Thank America for keeping this useless application alive",
               "Do you really need to type commands into this to know how hot it is? Hot tells you how hot it is!",
               "Here comes the sun is stuck in my head and I don't know how to deal with it"]
increment = 0
while True:
    try:
        burger_unit = int(input("Enter your temperature: "))
        change = 5/9 * (burger_unit - 32)
        print(change)
        try:
            if int(input("Do you want to leave? 0 = Stay, 1 = Exit: ")) == 1:
                break
            else:
                print(witty_lines[increment])
                if change > 0:
                    increment += 1
                else:
                    increment += 2
                if increment > 5:
                    increment = 0
        except ValueError:
            print("I guess you want to stay")
    except ValueError:
        print("Use arabic numerals not your silly letters")

'''
7. TRAPEZOID PROGRAM (5pts)
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
'''

first_base = int(input("Enter your top base"))
second_base = int(input("Enter your bottom base"))
height = int(input("Enter your height"))
print("The area is", ((first_base * second_base) / 2 ) * height)

'''
8. GRADING PROGRAM (5pts)
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''

sem = int(input("Enter your semester grade: "))
final = int(input("Enter your final grade: "))
final_int = int(input("How much is that final exam worth?: "))
final_value = final_int * (10 ** -2)
overall = (final * final_value) + (sem * (1 - final_value))
print("Your final grade:", overall)




