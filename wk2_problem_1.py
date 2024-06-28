arr_1 = [1,1,2,3,5,8,13,21,34,55,89]
arr_2 =[1,2,3,4,5,6,7,8,9,10,11,12]
arr_3 = []

for element in arr_1:
    if element in arr_2 and element not in arr_3:
        arr_3.append(element)
print (arr_3)
