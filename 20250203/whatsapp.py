import pywhatkit as kit


handle = open( 'numbers.txt' , 'r' )

for line in handle.readlines():
 listofLine = line.split(',')
 name = listofLine[0]
 number = listofLine[1]
 
 kit.sendwhatmsg( number, f"Hi {name}, How you doing?", 17, 39)

