# Here I defined the "names" list.
names = ["Jake",
         "Zac",
         "Ian",
         "Ron",
         "Sam",
         "Dave"]

# Here I defined "user_input" variable to store the user input.
user_input = input("Name?: ")

# Here I print first the input of the user(name), then the index of the name inputed by the user.
print(user_input, "is at Index", names.index(user_input))