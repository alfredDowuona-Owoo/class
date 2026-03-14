import sys
import os
input_for_user= int(input("press 1 for addition operation: ,  2 for subtraction operation:, 3 for exit:") )


while True:
    input_for_user = int(input("press 1 for addition operation: ,  2 for subtraction operation:, 3 for exit:") )
    if input_for_user ==1:
        print("You have selected addition operation")
    elif input_for_user ==2:
        print("You have selected subtraction operation")
    elif input_for_user ==3:
        print("Exiting the program as per user request")
        break
    else:
        print("Invalid input provided, please try again")
        os.exit(0)
        os._exit(0)