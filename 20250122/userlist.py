# initial set values for summation and counting

# totalValue = 0
# count = 0

# while True:
#  userInput =  input("Enter a value") 
#  if userInput == 'exit' : break

#  totalValue = totalValue + int( userInput)
#  count+=1

# print( "Average =", totalValue / count )


list = []

while True:
 userInput =  input("Enter a value") 
 if userInput == 'exit' : break

 list.append(  int(userInput) )
 

print( "Average =", sum(list) / len(list) )
print('----------')
print(list)


