#! python3
#passwordValidator.py - Create a program to validate passwords.
import re

def strongPasswordCheck(password):
    # regex for all password conditions
    alphabetDigitRegex = re.compile(r'''(^
                                    (?=.*[a-z])                     #At least 1 lowercase alphabet
                                    (?=.*[A-Z])                     #At least 1 uppercase alphabet
                                    (?=.*\d)                        #At least 1 digit
                                    [\w\d!@#$%&*]{8,}               #At least 8 characters
                                    $)''',re.VERBOSE)

    if alphabetDigitRegex.match(password):
        return 'valid'
    else:
        return 'invalid'


password = input('Enter password to check:')
print(strongPasswordCheck(password))

