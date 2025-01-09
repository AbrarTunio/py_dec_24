handle = open( "email.txt" , "r" )

for email in handle:
    pos = email.find("@")
    print(email[:pos])