def squares(a, b):
    lists=[]
    # Traverse through all numbers
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
print(squares(1, 30))
