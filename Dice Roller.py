import random
import sys


List = [1,2,3,4,5,6]





while True:


    r = input('Roll[y/n]')

    if r == 'y':

        print(random.choice(List))
    elif r == 'n':

        sys.exit()

    
        
 
