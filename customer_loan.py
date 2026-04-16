
'''

Program: Cunstomer Loan Program

Programmer: Kaweny Ezidio

Date: 12/03/2022

Description: This program calculates how long it will take to pay off a loan.
It asks the user to enter the amount of money they want to borrow, the interest
rate, the monthly payment amount and calculates how long it would take to
pay off that loan, the final payment amount and how much interest would be paid.

'''

# display welcome message
print("** Welcome to the Consumer Loan Calculator **")
# create variables
amount_to_borrow = float(input("How much do you want to borrow? $")) # ask user for amount to be borrowed
interest_total = 0
paid_off_time = 0
final_payment = 0


# check if amount to be borrowed is not positive
if(amount_to_borrow <= 0):
    while(amount_to_borrow <= 0): # create a loop to ask for number again until user enters a positive number
        print("You must enter a positive number!") # display message when number is not positive
        amount_to_borrow = float(input("How much do you want to borrow? $"))

 # aks user for anual interest rate
anual_interest = float(input("What is the annual interest rate expressed as a percent? "))

# check if rate is not positive
if(anual_interest <= 0): # create a loop to ask for number again until user enters a positive number
    while(anual_interest <= 0): # display message when number is not positive
        print("You must enter a positive number!")
        anual_interest = float(input("What is the annual interest rate expressed as a percent? "))

 # aks user monthly payment amount
monthly_payment = float(input("What is the monthly payment amount? $"))
if(monthly_payment <= 0): # check if number is not positive
    while(monthly_payment <= 0): # create a loop to ask for number again until user enters a positive number
        print("You must enter a positive number!") # display message when number is not positive
        monthly_payment = float(input("What is the monthly payment amount? $"))

# calculate interest rate per month
monthly_interest = (anual_interest / 12) * 0.01
# calculate first interest amount which is amount to be borrowed multiplied by monthly interest
interest = amount_to_borrow * monthly_interest
# calculate minimum payment
minimum_payment = interest + 1
# check if monthly payment is grater than zero and lesser than interest
if(monthly_payment > 0 and monthly_payment <= interest):
    # display a message that monthly payment inserted is not enough (program will end if it gets to this point)
    print("You must make payments of at least $"+"{:.2f}".format(minimum_payment),"\nBecause your monthly interest is $"+"{:.2f}".format(interest))

# store amount to be borrowed for later use
check = amount_to_borrow

# create a loop to calculte the results when all inputs are acceptable
while(amount_to_borrow >= 0 and amount_to_borrow > (interest + 1)):
    # check and stop the program when amount is zero or negative
    if(amount_to_borrow <= 0):
        break
    # continue looping when amount is acceptable
    else:
        # create variable to calcule balance
        new_balance = float((amount_to_borrow + interest) - monthly_payment)
        paid_off_time += 1  # count iterations 
        interest_total += interest # store/add interest of every interation
        amount_to_borrow = new_balance # reassign amount to be borrowed with new balance
        interest = amount_to_borrow * monthly_interest # reassign interest
        if amount_to_borrow <= 0: # check if amount has non positive
            # create a variable that adds monthly payment
            final_payment = float(format((monthly_payment + amount_to_borrow),',.2f'))
            break 
# check if amount to be borrowed was deducted and if monthly payment is greater than
# minumum payment to display results
if(check != amount_to_borrow and monthly_payment > minimum_payment):
    print("Your debt will be paid off after",paid_off_time,"months, with a final payment of just $"+str(final_payment))                  
    print("The total amount of interest you will pay during that time is $"+"{:.2f}".format(interest_total)) 

# display message at the end of program
print("** Don't get overwhelmed with debt! **")

'''
SAMPLE RUN

** Welcome to the Consumer Loan Calculator **
How much do you want to borrow? $1000
What is the annual interest rate expressed as a percent? 18
What is the monthly payment amount? $50
Your debt will be paid off after 24 months, with a final payment of just $47.83
The total amount of interest you will pay during that time is $197.83
** Don't get overwhelmed with debt! **


SAMPLE RUN

** Welcome to the Consumer Loan Calculator **
How much do you want to borrow? $15000
What is the annual interest rate expressed as a percent? 10
What is the monthly payment amount? $100
You must make payments of at least $126.00 
Because your monthly interest is $125.00
** Don't get overwhelmed with debt! **** Welcome to the Consumer Loan Calculator **
How much do you want to borrow? $15000
What is the annual interest rate expressed as a percent? 10
What is the monthly payment amount? $100
You must make payments of at least $126.00 
Because your monthly interest is $125.00
** Don't get overwhelmed with debt! **


SAMPLE RUN

** Welcome to the Consumer Loan Calculator **
How much do you want to borrow? $-50
You must enter a positive number!
How much do you want to borrow? $-200
You must enter a positive number!
How much do you want to borrow? $-2.5
You must enter a positive number!
How much do you want to borrow? $0
You must enter a positive number!
How much do you want to borrow? $5
What is the annual interest rate expressed as a percent? 0
You must enter a positive number!
What is the annual interest rate expressed as a percent? -2
You must enter a positive number!
What is the annual interest rate expressed as a percent? 200
What is the monthly payment amount? $200
Your debt will be paid off after 1 months, with a final payment of just $5.83
The total amount of interest you will pay during that time is $0.83
** Don't get overwhelmed with debt! **


SAMPLE RUN

** Welcome to the Consumer Loan Calculator **
How much do you want to borrow? $20000
What is the annual interest rate expressed as a percent? 5
What is the monthly payment amount? $200
Your debt will be paid off after 130 months, with a final payment of just $125.79
The total amount of interest you will pay during that time is $5925.79
** Don't get overwhelmed with debt! **** Welcome to the Consumer Loan Calculator **
How much do you want to borrow? $20000
What is the annual interest rate expressed as a percent? 5
What is the monthly payment amount? $200
Your debt will be paid off after 130 months, with a final payment of just $125.79
The total amount of interest you will pay during that time is $5925.79
** Don't get overwhelmed with debt! **

SAMPLE RUN

** Welcome to the Consumer Loan Calculator **
How much do you want to borrow? $100
What is the annual interest rate expressed as a percent? 12
What is the monthly payment amount? $50
Your debt will be paid off after 3 months, with a final payment of just $1.53
The total amount of interest you will pay during that time is $1.53
** Don't get overwhelmed with debt! **
** Welcome to the Consumer Loan Calculator **
How much do you want to borrow? $100
What is the annual interest rate expressed as a percent? 12
What is the monthly payment amount? $50
Your debt will be paid off after 3 months, with a final payment of just $1.53
The total amount of interest you will pay during that time is $1.53
** Don't get overwhelmed with debt! **


'''










