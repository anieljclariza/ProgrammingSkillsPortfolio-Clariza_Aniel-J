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

for capital, country in answers.items():
    
    user_input = input("What is the capital of " + country + "?: ")
    if user_input.upper() == capital.upper():
        print("✅Correct!")

    else:
        print("❌Whoops, the correct answer was " + capital)