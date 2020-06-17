# In this exercise, find absolut frequency from vowels in a text that user type. 

import matplotlib.pyplot as plt


parragraph= input('Ingresa tu texto ' )


parragraph =  parragraph.replace(" ", "")
parragraph = parragraph.casefold()
a=parragraph.count('a')
e=parragraph.count('e')
i=parragraph.count('i')
o=parragraph.count('o')
u=parragraph.count('u')

print(parragraph.count('a'))
print(parragraph.count('e'))
print(parragraph.count('i'))
print(parragraph.count('o'))
print(parragraph.count('u'))




