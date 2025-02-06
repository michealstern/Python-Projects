# 1. Using String Functions...!

email = input("Enter your Email: ")
k, j, d = 0, 0, 0

if len(email) >= 6:  #1
    if email[0].isalpha():  #2
        if ("@" in email) and (email.count('@') == 1):  #3
            if (email[-4] == ".") ^ (email[-3] == "."):  #4
                for i in email:  #5
                    if i.isspace():  # Fixed here, we need to check if (i) is a space
                        k = 1
                    elif i.isalpha():  # Check if the character is a letter
                        if i == i.upper():  # Check if the letter is uppercase
                            j = 1
                    elif i.isdigit():  # Digits are allowed
                        continue
                    elif i == "_" or i == "." or i == "@":  # Allow these special characters
                        continue
                    else:  # If any other character is found
                        d = 1

                if k == 1 or j == 1 or d == 1:  # If there is a space, uppercase letter, or invalid character
                    print("Wrong Email 5")
                else:
                    print("Valid Email")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")


# Using RegEx...!
# (Condition)
# a-z should be lowercase.
# 0-9 Int number.
# . _ one time before @
# @ one time
# . should be 2nd or 3rd position at the end

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_input=input("Enter your Email: ")
if re.search(email_condition,user_input):
    print("Valid Email.")
else:
    print("Wrong Email.")