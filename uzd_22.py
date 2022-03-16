picture = [1,2,3,4,5,6,7,8,9,10,11]
for i in picture:
    if i == 1 or i == 6 or i == 11:
        a=" "
        b="*"
        j=12
        c=""
        while j>=0:
            if j>1 and j<11:
               c=c+b
            else:
                c=c+a
            j=j-1
        print(c)
    if i == 2 or i == 5 or i == 7 or i == 10:
        a=" "
        b="*"
        j=12
        c=""
        while j>=0:
            if j>0 and j<12:
               c=c+b
            else:
                c=c+a
            j=j-1
        print(c) 
    if i == 3 or i == 4 or i == 8 or i == 9:
        a=" "
        b="*"
        j=12
        c=""
        while j>=0:
            if j<4 or j>8:
               c=c+b
            else:
                c=c+a
            j=j-1
        print(c) 