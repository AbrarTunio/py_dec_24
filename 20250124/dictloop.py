fruits = {  'mango' : 25 , 'kiwi' : 37, 'oranges' : 19 , 'melon' : 5 }

# myfruitlist = [ 'mango' , 'kiwi' , 'oranges' , 'melon'  ]
# for fruit in myfruitlist:
#  print(fruit)

for name , qty in fruits.items():
 print(name, "==>" , qty)
 print( type(name) )
 print('**********************')


for name  in fruits.items():
 print(name)
 print( type(name) )
 print('**********************')

