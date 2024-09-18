#! python3
#multiplicationQuiz.py - Implements a small multiplication quiz program using pyinputplus

import pyinputplus as pyip
import random,time

correctAnswers = 0
noOfQuesions = 10

for Qno in range(noOfQuesions):
    num1 = random.randint(-9,9)
    num2 = random.randint(-9,9)

    try:
        response = pyip.inputStr('%s. %s x %s = '%(Qno+1,num1,num2), allowRegexes = ['^%s$'%(num2*num1)], 
                                 blockRegexes = [('.*','Incorrect.')],limit = 3,timeout = 20)

    except pyip.TimeoutException:
        print('Out of time!!')
    except pyip.RetryLimitException:
        print('Out of tries!!')
    else:
        print('Correct Answer. Math wizard.')
        correctAnswers+=1
    time.sleep(1)
    
    
print('Result = %s/%s'%(correctAnswers,noOfQuesions))
