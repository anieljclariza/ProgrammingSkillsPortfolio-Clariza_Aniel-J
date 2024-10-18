# This is the dictionary wherein the name, hometown, and age of the user has been placed after being asked to input their data.
biography = {
    "Name:": input("What is your name?: "), 
    ""
    "Hometown:": input("Where do you live?: "),
    ""
    "Age:": int(input("How old are you?(Input an integer please.): "))
    
}
# This loop is used to go through and print the key-value pairs in the dictionary above. Variables x and y will be used for the key and the value respectively.
for x, y in biography.items():
    print(x, y)


