import os

print("Exception handling started here")
try :
    folder_name = "temp"
    file_name = "temp_2.txt"
    file_path = os.path.join(folder_name, file_name)
    num = 0
    with open (file_path, "r+") as f:
        content = f.read()
        print(content)

    if num == 0:
        raise Exception(" Our own exception: num should not be zero for division operation")
    cal = 1501 / num
    print("calculation result is:", cal)
except FileNotFoundError:
    print("File not found, please check correct file name or path.")
    print("current location is:", os.getcwd())
    print("files present in the directory are:", os.listdir(os.path.join(os.getcwd(), folder_name)))
    print("file name selected is:", file_path)

except TypeError:
    print("issue with multiply type operation")

except Exception as e:
    print("error caught:", e)
else:
    print("No error occurred, try block executed successfully")
finally:
    try:
        f.close()
        print("file is closed successfully in finally block")
    except:
        print("File was not opened or already closed.")
print("try except block ended here")