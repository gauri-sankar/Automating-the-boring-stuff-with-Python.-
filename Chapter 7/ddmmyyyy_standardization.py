#! python3
#ddmmyyyy_standardization.py: A program to convert dates in mmddyyy and yyyymmdd formats into ddmmyyyy
  
import re,pyperclip
#Regex for mmddyyyy

def standardiseDateFormat():
    mmddyyyyregex = re.compile(r'''(

    # \b([1-9]|[0-2][1-9]|3[0-1])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)(\d{4})\b| 
    \b([1-9]|0[1-9]|1[0-2])(\.|-|/)([1-9]|[0-2][1-9]|3[0-1])(\.|-|/)(\d{4})\b
    # \b(\d{4})(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([0-9]|[0-2][1-9]|3[0-1])\b

    )''',re.VERBOSE)

    #Regex for yyyymmdd
    yyyymmddregex = re.compile(r'''(\b(\d{4})(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([0-9]|[0-2][1-9]|3[0-1])\b)''',re.VERBOSE)

    matches = []

    # find all dates in ddmmyyyy

    copiedText = str(pyperclip.paste())

    for groups in mmddyyyyregex.findall(copiedText):
        flag = True
        copiedText = re.sub(groups[0],str(groups[3]+'-'+groups[1]+'-'+groups[5]),copiedText)

    # find all dates in yyyymmdd

    for groups in yyyymmddregex.findall(copiedText):
        copiedText = re.sub(groups[0],str(groups[5]+'-'+groups[3]+'-'+groups[1]),copiedText)

    if flag: 
        print('All possible dates standardised to the required format.')
        print('Copied to clipboard:')
        print(copiedText)
    else:
        print('No possible dates to be standardised.')
    return 

standardiseDateFormat()
