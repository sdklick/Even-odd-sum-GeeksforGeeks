# Even odd sum GeeksforGeeks
Arr=[1,1,1,1,1] #when you solve the code do not write this line
odd=0
even=0
for x in range(1,len(Arr)+1):
    if x%2==0:
       even+=Arr[x-1]
    elif x%2!=0:
        odd+=Arr[x-1] 
print(odd,even)          


