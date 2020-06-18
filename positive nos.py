# Python program to print positive Numbers in a range 
#Using forloop
  
# list of numbers 
list1 = [12,-7,5,64,-14] 
  
# iterating each number in list 
for num in list1: 
      
    # checking condition 
    if num >= 0: 
       print(num, end = " ") 
        
        
        
# list of numbers 
list2 = [12,14,-95,3] 
  
# iteration
for num in list2: 
      
    # checking condition 
    if num >= 0: 
       print(num, end = " ") 

        
#using while loop
# Python program to print positive Numbers in a range
  
# list of numbers 
list1 = [12,-7,5,64,-14] 
num = 0
    
while(num < len(list1)): 
      
    # checking condition 
    if list1[num] >= 0: 
        print(list1[num], end = " ") 
      
    # increment 
    num += 1
    
    
    list2 = [12,14,-95,3] 
num = 0
    
while(num < len(list1)): 
      
    # checking condition 
    if list2[num] >= 0: 
        print(list2[num], end = " ") 
      
    # increment 
    num += 1
