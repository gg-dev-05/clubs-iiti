import re

def checkIfMailIsValid(email):
    regex = '(cse|ce|me|ee|mems)(\d{9})(@iiti.ac.in)'
    if(re.search(regex,email)):  
        return True
    else:  
        return False