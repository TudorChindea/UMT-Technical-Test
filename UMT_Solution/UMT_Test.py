import sys

def minimumChanges(password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_char = "!@#$%^&*()-+"
    password_length = len(password)
    hasNumber = 1
    hasLower = 1
    hasUpper = 1
    hasSpecial = 1
    maxRepeatingChars = 0
    currentRepeatingChar = 0
    lastChr = 'a'
    #go through the entire password and check all characters if they are either, a number, lower case letter, uppercase letter or a special character
    for c in range(password_length-1):
        if c == 0: 
            lastChr = password[c]
            currentRepeatingChar +=1
        elif password[c] == lastChr:
            currentRepeatingChar +=1
        else:
            if currentRepeatingChar>= 3:
                maxRepeatingChars +=1
            currentRepeatingChar = 0
            lastChr = password[c]
        if password[c] in numbers: hasNumber = 0
        elif password[c] in lower_case: hasLower = 0
        elif password[c] in upper_case: hasUpper = 0
        elif password[c] in special_char: hasSpecial = 0
    #we return the maximum number between the:
    #       1: difference between the minimum password length and the number of characters 
    #       2: difference between the number of conditions that need to be met and the ones that are already met
    #       3: the number of times more than 3 characters appear together
    max1 = max(6-password_length,password_length-20)
    return max(max1, hasNumber + hasSpecial + hasLower + hasUpper + maxRepeatingChars)
#read the number of characters in the password and the pa
if __name__ == "__main__":
    password = input().strip()
    answer = minimumChanges(password)
    print(answer)