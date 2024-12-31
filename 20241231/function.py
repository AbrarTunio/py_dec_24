# Function Defination

# def fry():
#     print("You gave me chicken")
#     print("I gave you fried Chicken")

def speak( animalName ):
    if animalName == "Dog":
        print(f"{animalName} Barks")
    elif animalName == "Cat":
        print(f"{animalName} Meows")
    else:
        print(f"Not in mood")


# Function Using or Calling

# fry()
speak( "Cat")
print("**************")
speak( "Dog")
print("**************")
speak("Lion")