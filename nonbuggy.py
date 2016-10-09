# Implemenation of a bubble sort.
# This code is syntactically correct, however there are a couple of
# problems that prevent it from producing the desired output.
# Find these errors and correct them, writing a comment explaining
# what the error was.

def swap_values(i1, i2, _list):
    _list[i1], _list[i2] = _list[i2], _list[i1] # Replaced an i2 with another i1
    return _list

def sort(values):
    for pass_num in range(1, len(values)):
        pass_size = len(values) - pass_num
        for i in range(pass_size): # Intentionally incorrect + 1
            if values[i] > values[i + 1]:
                values = swap_values(i, i + 1, values) # +1 removed in buggy version
    return values

print sort([3, 45, 212, 31, 53, 4])

