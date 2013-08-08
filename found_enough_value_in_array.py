#!/usr/bin/python
import random
# condition
N = 10
source_array = list(range(0, N+1))
random.shuffle(source_array)
source_array.pop()
print source_array


# solution
current_sum = 0
full_sum = 0
inc_value = 1
for x in source_array:
    current_sum += x
    full_sum += inc_value
    inc_value += 1
found_value = full_sum - current_sum

print "Found value "+str(found_value)
