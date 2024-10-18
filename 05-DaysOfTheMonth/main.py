# Dictionary called "months" is created to store the months as keys and the days of those months as values.
months = {"1":"31",
          "2":"28",
          "3":"31",
          "4":"30",
          "5":"31",
          "6":"30",
          "7":"31",
          "8":"31",
          "9":"30",
          "10":"31",
          "11":"30",
          "12":"31"
          }

# Variable "user_input" is created to store the inputs of the user.
user_input = input("Input month number: ")
# If-else statement that only runs when the user inputs "2" into the terminal. This code asks if February is leap year or not and displays the respective outputs according to the answer of the user.
if user_input == "2":
    user_input2 = input("Leap year?(Y or N): ")
    if user_input2.upper() == "Y":
        print("29")
    else:
        print(months.get(user_input))

# This code is ran to get the number of days of the month number that the user has inputed in the terminal.
else:
    print(months.get(user_input))