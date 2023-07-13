import math

# the following code will ask the user to input their specific details to run their specific required calculator.
# the program will print the correct information based on the users input.

print ("investment - to calculate the amount of interest you'll earn on your investment.")
print ("bond - to calculate the amount you'll have to pay on a home loan.")

# this line asks the user to input either investment or bond so it selects the correct category of questions.
finance_choice = str(input("Enter either 'investment' or 'bond' from the menu above to proceed:\t").lower())


# the following code of questions will print and request the users input when 'investment' is inputed as the answer to line 10.
if finance_choice == "investment":  
    
    deposit = float(input("how much would you like to deposit?:\t"))

    interest_rate = float(input("how much is the interest ?:\t")) / (100)
    
    years_of_investing = int(input("for how many years do you plan to invest?:\t"))

    interest = str(input("would you like 'simple' or 'compound' interest?:\t").lower()) # 

    print("") # this prints a space to keep the program tidy and spaced out to ensure clarity and readability.
    
    if interest == "simple":      # the user has a set of questions within the previous question.
        total_simple_interest = deposit*(1+ interest_rate * years_of_investing) # calculates the total 'simple interest' . 
        print(f" your total simple interest is £{total_simple_interest:.2f}") # this prints the calculated total 'investment' - 'simple interest' information. 


    elif interest == "compound":
        total_compound_interest = deposit * math.pow((1 + interest_rate), years_of_investing) # calculates the total 'compound interest' .
        print(f" your total compound interest is £{total_compound_interest:.2f}") # this prints the calculated total 'investment' - 'compound interest' information.

    else:
        print("you have not entered your choice of interest type, please enter again.") # if the user does not input a valid answer from line 22 this will print.



elif finance_choice == "bond":  # else if user inputs 'bond' from the question on line 10 then the following questions & inputs will print.
    
    house_value = float(input("what is the current value of the house?:\t"))

    monthly_interest_rate = float(input("how much is the interest ?:\t")) / (100) / (12)

    months_of_repayment = int(input("how many months do you plan to take to repay the bond?:\t"))

    repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** (-months_of_repayment)) # calculates the total monthly 'bond' repayments.

    print("")

    print(f"your monthly repayment for the bond is £{repayment:.2f}") # this prints the calculated total monthly 'bond' repayments.

else: 
    print("sorry, you must only enter 'investment' or 'bond'. please try again.") # if user does not input a valid answer to line 10, this line prints.













   







