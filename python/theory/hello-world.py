#Fancy Hello World

# The character sets are defined to include spaces, alphabetic characters, special characters, and digits.
char_set_alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
char_set_digit = list("0123456789")
char_set_special = list("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~")
char_set_space = list(" ")

import time 

def hello_world(str, char_set):
    result = []

    # Iterate through each character in the string
    for i in str:
        for j in char_set:       
            if i == j:                  # If the character matches, append it to the result
                result.append(i)
                break

            print("".join(result) + j)  # Print the current result and the character being checked
            time.sleep(0.02)            # Adding a delay to simulate waterfall effect

                
hello_world("Hello, World!", char_set_space + char_set_alpha + char_set_special)
