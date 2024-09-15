#! python3
#regexStrip.py - Program performing the strip() methods functionality or to remove leading or trailing zeroes from the sentence.

import re

def regexStrip(sentence, toSub = ' ' ):
    return re.sub(rf'^{re.escape(toSub)}*(.*?){re.escape(toSub)}*$',r'\1',sentence)


print(regexStrip('***The string to strip .***','*')) #Example 

