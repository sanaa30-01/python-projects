import random

def maths(a, b):
    return a + b

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths(new_item, item)
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

#debugging with the debugger:
#breakpoint --> place a breakpoint in the code --> pauses the code at that line
#step over --> move line by line and execute the code
#step into --> go into the function and execute the code --> shows how that function works 