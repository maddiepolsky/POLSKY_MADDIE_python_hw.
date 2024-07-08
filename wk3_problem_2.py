#Write a function remove duplicates(lst) that returns a list with duplicates removed.

def remove_duplicates(lst):
    old = set()
    new = []
    for item in lst:
        if item not in old:
            old.add(item)
            new.append(item)
    return new
numbers = (1, 1, 5, 4, 4, 6, 8, 8, 9)
print(remove_duplicates(numbers))

#works for other lists too