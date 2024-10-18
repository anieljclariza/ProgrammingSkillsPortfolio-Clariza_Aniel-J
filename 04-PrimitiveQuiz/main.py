# Made a dictionary called "answers" to place the capitals as keys and countries as values.
answers = {"Paris": "France", 
           "Lisbon": "Portugal",
           "Amsterdam": "Netherlands",
           "Stockholm": "Sweden",
           "Athens": "Greece",
           "Vienna": "Austria",
           "Copenhagen": "Denmark",
           "Berlin": "Germany",
           "Rome": "Italy",
           "London": "England"}

# Here a for-loop is used to go through the key-value pairs in the dictionary above.

#The loop will continue to run until the last key-value pair in the dictionary above is displayed.
for capital, country in answers.items():
    
    # A variable named "user_input" is used to store the inputs of the user. 

    # The "country" variable is used to display the values in the dictionary above to make the code more efficient instead of doing if-else loops.
    user_input = input("What is the capital of " + country + "?: ")

    #This is the conditional wherein the programs executes this part of code if the user is correct regardless of the capitalization.
    if user_input.upper() == capital.upper():
        print("✅Correct!")

    # This part of code is executed if the user is wrong.
    else:
        print("❌Whoops, the correct answer was " + capital)