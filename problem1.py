#!!
S=input("Enter String to count Frequency: ")
Count = {} 
#for loop for count 
for i in S: 
#if-else for incrementing count by 1
    if i in Count: 
        Count[i] += 1
    else: 
        Count[i] = 1
  
# printing count
print (" is :\n "  +  str(Count)) 
#!!