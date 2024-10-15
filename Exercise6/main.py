#First I have defined a variable to place the input of the user.
user_input = input("Enter password: ")

#Then I have made an input_count variable to monitor how many attemps the user has done.
input_count = 0

#Next I used a while loop wherein as long as the input the user has typed is incorrect, the loop will continue, the input_count will be increased by 1 every loop, and if the input_count reached 5(When the user inputted incorrectly 5 times)
while user_input != "12345":
    input_count += 1

    #This is just a part of code that I made in order to make correct grammar. If the user has 1 attempt left, I write the print statement as "attempt" instead of "attempts".
    if input_count == 4:
        print("Access denied. " + str(5 - input_count) + " attempt remaining.")
    else:
        print("Access denied. " + str(5 - input_count) + " attempts remaining.")

    #If the input_count is 5, the user is denied to enter the password again.    
    if input_count == 5:
        print("You have entered the password incorrectly 5 times. The authorities have been informed of this activity.")
        break

    #Continues running the loop while input_count is less than 5.
    else:
        user_input = input("Enter password: ")
else:
    print("Access granted.")