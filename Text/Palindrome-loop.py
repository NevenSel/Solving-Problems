print "Hello, this will tell you if your input is a palindrome or not. Give it a try!"

some_string = str(raw_input("Please enter a string in all lowercase "))

print "Your string was: ", some_string
print "Reversed, it is: ", some_string[::-1]

while some_string != some_string[::-1]:
    print some_string, " is not a palindrome, please try again."
    some_string = str(raw_input("Please enter a string in all lowercase "))

print some_string, " is a palindrome!"
