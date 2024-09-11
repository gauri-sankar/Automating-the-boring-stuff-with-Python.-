#! python3
#hideCreditCard.py - Program to hide the credit card numbers.
import re,pyperclip
#Regex for mmddyyyy

def hideCreditCard():
    # Regex for card numbers
    creditCardRegex = re.compile(r'''(\b
                                 (\d{4})
                                 (\s*)
                                 (\d{4,6})
                                 (\s*)
                                 (\d{4,5})
                                 (\s*)
                                 (\d{2,4})?
                                 \b)''',re.VERBOSE)
    print(creditCardRegex.search('3056 9309 0259 04').group())
    
    #Hide card numbers
    copiedText = pyperclip.paste()
    copiedText = creditCardRegex.sub(r'**** **** **** **** ****',copiedText)

    pyperclip.copy()
    print('Copied to clipboard:',copiedText)
hideCreditCard()
