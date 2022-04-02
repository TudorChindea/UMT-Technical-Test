import sys

def minimumChanges(password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_char = "!@#$%^&*()-+"
    password_length = len(password)
    hasNumber = 0
    hasLower = 0
    hasUpper = 0
    hasSpecial = 0
    #go through the entire password and check all characters if they are either, a number, lower case letter, uppercase letter or a special character
    for c in password:
        if c in numbers: hasNumber = 1
        elif c in lower_case: hasLower = 1
        elif c in upper_case: hasUpper = 1
        elif c in special_char: hasSpecial = 1
    #we return the maximum number between the:
    #       1: difference between the minimum number of characters and password length
    #       2: difference between the number of conditions that need to be met and the ones that are already met
    return max(6-password_length, 4 - hasNumber - hasSpecial - hasLower - hasUpper)
#read the number of characters in the password and the pa
if __name__ == "__main__":
    password = input().strip()
    answer = minimumChanges(password)
    print(answer)