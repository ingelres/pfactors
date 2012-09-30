#!/usr/bin/env python
#
# Author: Francois Ingelrest

from math import sqrt
from sys  import argv, exit

if len(argv) == 1 :
    print 'Usage : ', argv[0], ' value'
    exit()

value      = int(argv[1])
maxDivider = int(sqrt(value))
output     = ''
divider    = 2

while divider <= maxDivider :

    # Find how many times 'value' may be divided by 'divider'
    count = 0
    while value % divider == 0 :
        value /= divider
        count += 1

    # Format the result
    if count != 0 :
        output += ' * ' + str(divider)
        if count > 1 :
            output += '^' + str(count)
        # Stop if the value can't be divided any more
        if value == 1 :
            break

    # Next divider
    # '2' is the sole even divider we use
    if divider == 2 : divider = 3
    else :            divider += 2

else :
    output += ' * ' + str(value)

# Display the result, removing the leading ' * ' characters
print 'x =', output[3:]
