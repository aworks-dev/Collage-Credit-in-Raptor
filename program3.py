# 2/4/2025
# ---------------------------------------------------------------------
# Variable           Type            Porpose
# ---------------------------------------------------------------------
#credits             int            shows the credit earned

# display output to user
print("*******************************************************************")
print("University of Computer Science and ONLY Computer Science ")
print("*******************************************************************\n")
print("CLASS STANDING EVALUATOR\n")
# declare and initialize variables.
credit = int(input("Enter the number of credits earned: " ))
#evaluating conditions
if credit>=120:
    print("Welcome to the University Alumni Association")   #display output to user if conditions met
elif credit>=90 and credit<120:                          #evaluating conditions
    print("Senior: Almost done!")                        #display output to user if conditions met
elif credit>=60 and credit<90:                           #evaluating conditions
    print("Junior: Getting close. Don’t give up now.")   #display output to user if conditions met
elif credit>=30 and credit<60:                           #evaluating conditions
    print("Sophomore: You’re making progress.")          #display output to user if conditions met
elif credit>=0 and credit<30:                            #evaluating conditions
    print("Freshman: Welcome to University.")               #display output to user if conditions met
elif credit<0:                                           #evaluating conditions
    print("ERROR: Negative Credits Entered.")            #display output to user if conditions met
