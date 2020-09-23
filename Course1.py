
CHAPTER 2: Expressions

2.2 Write a program that uses input to prompt a user for their name and then
welcomes them. Note that input will pop up a dialog box. Enter Sarah in the
pop-up box when you are prompted so your output will match the desired output.

name = input("Enter your name")
print("Hello", name)

###############################################################################

2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking or bad user data.

hrs = input("Enter Hours:")
rph = input("Enter Rate:")
hrs = float(hrs)
rph = float(rph)
pay = hrs* rph
print("Pay:", pay)

#################################################################################

CHAPTER 3: Conditional Statements

3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking the user input - assume the user types numbers properly.

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
if h <= 40:
    pay = h*r
else:
    pay = (r*1.5)*(h-40) + 40*r
print(pay)

******************************
# Alternative

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h =  float(hrs)
r = float (rate)
if h > 40:
    pay = (h-40)*(r*1.5)+ 40*r
else:
    pay = h*r
print(pay)
    


###################################################################################
3.2: Rewrite your pay program using try and except so that your program handles
non-numeric input gracefully by printing a message and exiting the program.
The following shows two executions of the program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:                   # to avoid traceback
   h = float(hrs)      # line that throws error when non-numeric input is given
   r = float(rate)     # line that throws error when non-numeric input is given
except:
    print("Error, please enter numeric input")

#print(h,r)
      
if h <= 40:
    pay = h*r
else:
    pay = (r*1.5)*(h-40) + 40*r

print(pay)

################################################################################
#Alternative

sh = input("Enter Hours:")
sr = input ("Enter Rate:")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")

#print(fh,fr)
if fh > 40:
    reg = fr*fh
    otp = (fh-40) * (fr*0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay:", xp)
    

################################################################################


3.3. Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit.
For the test, enter a score of 0.85.

inp = input("Enter Score: ")
score = float(inp)
if score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print ('D')
elif score < 0.6:
    print('F')
else:
    print("Out of range")

*******************************************
#Alternative:

try:
   inp = input("Enter Score: ")
   score = float(inp)
   if score >= 0.9:
       print('A')
   elif score >= 0.8:
       print('B')
   elif score >= 0.7:
       print('C')
   elif score >= 0.6:
       print ('D')
   elif score < 0.6:
       print('F')
   else:
       print("Out of range")
except:
       print("please enter a number:")

##############################################################################
CHAPTER 4: Functions

4.6. Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
Do not name your variable sum or use the sum() function.


def computepay(h,r):
    if h > 40:
        p = (h-40)*(r*1.5) + 40*r
    else:
        p = h*r
    return p

hrs = input("Enter Hours:")
rate = input ("Enter Rate:")
h =  float (hrs)
r = float(rate)

p = computepay(h,r)
print("Pay",p)




##############################################################################

CHAPTER 5: Loops and Iterations

5.1. Write a program which repeatedly reads numbers until the user enters "done".
Once "done" is entered, print out the total, count, and average of the numbers.
If the user enters anything other than a number, detect their mistake
using try and except and print an error message and skip to the next number.


num = 0
tot = 0
while True:
    sval = input("Enter a number: ")
    if sval == 'done':
        break
    fval = float (sval)
    #print(fval)
    num = num +1
    tot = tot + fval
#print("ALL DONE")
print(tot, num, tot/num)

*********************************
# adding try and except

num = 0
tot = 0
while True:
    sval = input("Enter a number: ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    #print(fval)
    num = num +1
    tot = tot + fval
#print("ALL DONE")
print(tot, num, tot/num)

#################################################################################


5.2. Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a try/except and put out
an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    try:
        num = int(inp)
    except:
        print ("Invalid input")
        continue
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    if largest is None:
        largest = num
    elif num > largest:
        largest = num

print ("Maximum is", largest)
print ("Minimum is", smallest)

**************************************

#Alternative 1:

largest = 0
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        num1=int(num)
        if num1 > largest:
            largest=num1
        elif smallest is None or num1 < smallest:
             smallest = num1
    except:
        print('Invalid input')
        continue


print("Maximum is", largest)
print("Minimum is",smallest)

***************************************************

#Alternative 2:
    
largest = None
smallest = None

while True:
    inp = raw_input("Enter a number: ")

    if inp == "done":
        break

    try:
        num = int(inp)

        if smallest is None:
            smallest = num
        elif num < smallest:
            smallest = num
        elif num > largest:
           largest = num
    except:
        print ("Invalid input")

    continue

print ("Maximum is", largest)
print ("Minimum is", smallest)


***************************************************
#Alternative 3:

largest = None
smallest = None

while True:
      num = input("Enter a number: ")
      if num == "done":
          break
      try:
         n = int(num)
         if smallest is None or n < smallest:
             smallest = n
         if largest is None or n > largest:
             largest = n
       except ValueError:
       # num cannot be converted to an int
            print ("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)

####################################################################################




