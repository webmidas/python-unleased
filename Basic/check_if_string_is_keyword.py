#how to check if a string is a reserved keyword or not
import keyword

s = 'while'

if keyword.iskeyword(s):
    print(s,' is a reserved keyword')
else:
    print(s,' is a not a reserved keyword')