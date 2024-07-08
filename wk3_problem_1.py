def find_max(lst):
    if not lst:
        return None
    max_value = lst [0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print (find_max(numbers))
#first one I tried^ also works for  other numbers that I tried
#I learned that  I at first incorrectly indented the "return" statement 
#which would give me 2 as the output but I figured it out