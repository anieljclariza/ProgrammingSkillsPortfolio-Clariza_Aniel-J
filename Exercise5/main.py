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

user_input = input("Input month number: ")
if user_input == "2":
    user_input2 = input("Leap year?(Y or N): ")
    if user_input2.upper() == "Y":
        print("29")
    else:
        print(months.get(user_input))
    
else:
    print(months.get(user_input))