#exception handling is used to handle or watch out for errors

try:
    number=int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input")



try:
    #value=10/0
    number=int(raw_input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as error:
    print(error)
    



