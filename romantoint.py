x = list(input(""))
count = 0
for i in range(len(x)):
    
    if x[i] == "I":
        if i == len(x)-1:
            count += 1
            pass
        elif x[i+1] == "V" or x[i+1] == "X":
            count -= 1
        else:
            count += 1
    
    if x[i] == "V":
        count += 5
    
    if x[i] == "X":
        if i == len(x)-1:
            count += 10
            pass
        elif x[i+1] == "L" or x[i+1] =="C":
            count -= 10
        else:
            count += 10
    
    if x[i] == "L":
        count += 50
    
    if x[i] == "C":
        if i == len(x)-1:
            count += 100
            pass
        elif x[i+1] == "D" or x[i+1] == "M":
            count -= 100
        else:
            count += 100
        
    if x[i] == "D":
        count += 500
        
    if x[i] == "M":
        count += 1000
        
print(count)