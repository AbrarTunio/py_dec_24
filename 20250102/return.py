
def welcome( name , gender ):
    if ( gender == "male" ):
        return f"Welcome Mr. {name}"
    else:
        return f"Welcome Ms. {name}"

result = welcome( "Raafe" , 'male' )
print( result )

result = welcome( "Safia" , 'female' )
print( len(result)  )

result = welcome('Gauri' , 'female') 
print( result )
