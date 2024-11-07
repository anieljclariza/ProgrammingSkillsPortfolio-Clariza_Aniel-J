#Here I defined the main() function wherein I saved the input of the user in the "number" variable. Then I passed  "number" into the checker() function to check if "number" is even or odd.
def main():
    number = int(input("Input a number: "))
    checker(number)

#Here I defined the checker() function that accepts "number" as arugument and checks if it is "even" or "odd" and prints the result.
def checker(number):
    if number % 2 == 0:
        return(number, "is Even.")
    else:
        return(number, "is Odd.")

#Here I call the main() function to execute the program.
main()