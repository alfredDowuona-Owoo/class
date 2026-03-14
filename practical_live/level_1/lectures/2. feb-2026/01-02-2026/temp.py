


###################################
# Exception handling in python  ###

value_1 = input("please provide a value for calculation: ")

def add(val_1, val_2):
    try:
        return val_1 + val_2
    except :
        print("error in calculation handling it using type casting")
    return val_1 + float(val_2)

calc = add(100, value_1)
print("calculation result:", calc)
print("hello world")

## handle error such that other things should work even if there is an error in the above code
### handle error such that it will not break the entire code execution