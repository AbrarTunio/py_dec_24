status = input("What is your secret identity? ")

if ( status == 'don' ):
    print("Welcome Don!")
    order = input("What would you like to order")

    if (order == 'biryani'):
        print("You are served")
    else: print(f"{order} is not available")


print("All Done")

