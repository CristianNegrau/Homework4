# Scrieti un program in python care aduna toate numerele pe care le da user-ul prin terminal

import sys

the_sum = sum(int(i) for i in sys.argv[1:])

print(the_sum)