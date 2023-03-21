
#!/bin/python3

import math
import os
import random
import re
import sys

def print_status(N):
    if N % 2 != 0:
        print('Weird')
    else:
        if N >= 2 and N <=5:
            print('Not Weird')
        elif N >=6 and N <= 20:
            print('Weird')
        else:
            print('Not Weird')

if __name__ == '__main__':
    N = int(input().strip())
    print_status(N)
