"""
Getting random variable names
so this code will replace the name of variable into an random String
count by how much level that you input
"""

import random
import string


#declare level of variable name that contains a level
low = 32       #less memory and storage usage
mid = 64       #normal memory and storage usage for big-scale code
high = 128     #very high usage on memory and storage

def ran(length):
    # wil generate the string for repalce the variable
    char_ran = []
    for let in range(length):
        char_ran.append(random.choice(string.ascii_letters))
    return "".join(char_ran)

def get_level(level):
    # this function will make sure what level you choose and return the "ran()" function
    if level == 'low':
        return ran(32)
    elif level == 'mid':
        return ran(64)
    elif level == 'high':
        return ran(128)
    else:
        print('No level included')
