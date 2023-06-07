"""
Simple string parser that takes in a string
as an input and separates it into a list of
strings based on if the input contains a mixture
of numbers and characters of the standard english
alphabet

ex. input: alpha12be43z0
    output: ['alpha', '12', 'be', '43', 'z', '0']
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

def parse(string):
    returnList = []
    walker = ""
    for i in string:
        if i in alphabet and (walker == "" or walker[0] in alphabet):
            # checks if i in alphabet or if walker is empty or the
            # first char in string is in alphabet
            walker += i
        elif i in numbers and (walker == "" or walker[0] in numbers):
            # checks if i in number or if walker is empty or the
            # first char in string is in numbers
            walker += i
        elif i in alphabet and walker[0] in numbers:
            # checks if i in alphabet
            # and if walker is in number
            # appends walker
            # then resets
            returnList.append(walker)
            walker = ""
            walker += i
            if i == string[-1]:
                # if the last char in string
                # is in alphabet
                returnList.append(walker)
        elif i in numbers and walker[0] in alphabet:
            # checks if i in numbers
            # and if walker is in alphabet
            # appends walker
            # then resets
            returnList.append(walker)
            walker = ""
            walker += i
            if i == string[-1]:
                # if last cahr in string
                # is in numbers
                returnList.append(walker)

    return returnList

arg = "alpha12be43z0"
print(parse(arg))
        
