fruits = ('tomato' , 'kiwi' , 'orange' , 'tomato')

print( fruits.count('tomato')  )

count = 0
for fruit in fruits:
 if fruit == 'tomato':
  for letter in fruit:
   if letter == 'o':
    count = count + 1

print("The o in tomato are:" , count )
