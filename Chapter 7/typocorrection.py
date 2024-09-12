#! python3
#typocorrection.py - Program to correct typos such as multiple spaces, repeated words and exclamation marks or question marks.

import re,pyperclip

def typocorrect():
    #create regexes for typos
    spaceRegex = re.compile(r'[^\S\n]{2,10}')
    repeatWordsRegex = re.compile(r'\b(\w+)\b(?:\s+\b\1\b)+')
    repeatSymbolsRegex = re.compile(r'([^\s\w\d])\1{1,}')

    copiedText = pyperclip.paste()
    #find and replace

    copiedText = spaceRegex.sub(' ',copiedText)
    copiedText = repeatWordsRegex.sub(r'\1',copiedText)
    copiedText = repeatSymbolsRegex.sub(r'\1',copiedText)
    pyperclip.copy(copiedText)
    print('All possible typos removed and copied to clipboard:')
    print(copiedText)

typocorrect()
