# Creating a coffee program that a user will
# be able to interact with.
# Matthew Horsford
# 25 Sept 2026

# Version 2

# TODO: record an input
#       check for valid answer
#       Ask questions and respond
    #Version 1
'''# Ask the user whether they like coffee or not
like_coffee = input("Do you like coffee? ")
# print(like_coffee) # checking the input is stored
print(f"Your answer was {like_coffee}'.")

# Check the input and respond
if like_coffee == "Yes" or "yes":
    print("That is great! I like coffee too.")
else:
    print("You are missing out! Why not give it a try")'''
    
# Version 2
# While loop to test the program
keep_going = ""
while keep_going == "":
    like_coffee = input("Do you like coffee? ")
    # print(like_coffee) # checking the input is stored
    print(f"Your answer was {like_coffee}'.")

    # Check the input and respond (To be fixed next time)
    if like_coffee == "Yes" or like_coffee == "yes" or like_coffee == "Y" or like_coffee == "y":
        print("That is great! I like coffee too.")
        keep_going = "Finish"
    elif like_coffee == "No" or like_coffee == "no" or like_coffee == "N" or like_coffee == "n:":
        print("You are missing out! Why not give it a try")
        keep_going = input("Press <Enter> to try again or any other key to exit")
    else:
        print("I don't understnad. Please try again.")