age = input("write yourage:- ")
name =str(input("yur name:-"))

def activity(name ,age:int):
    if age < 0:
        raise ValueError("it should be not zero")
    if type(name) == str and type(age) ==int:
          print("hi",name)
          print("your",age,"old")
    else:
        raise TypeError("invalide type it must be string and integer")

    return activity()