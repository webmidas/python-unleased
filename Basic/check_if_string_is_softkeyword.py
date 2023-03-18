#how to check if a string is a soft keyword or not
import keyword

s = 'match'

if keyword.issoftkeyword(s):
    print(s,' is a soft keyword')
else:
    print(s,' is a not a soft keyword')