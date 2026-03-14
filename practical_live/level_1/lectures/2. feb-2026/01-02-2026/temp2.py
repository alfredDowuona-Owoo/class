import os

print("Exception handling started here")
try :
    folder_name = "temp"
    file_name = "temp_3.txt"
    file_path = os.path.join(folder_name, file_name)
    num = 0
    with open (file_path) as f:
        content = f.read()
        print(content)
    cal = 100 / num
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
    print("No error found, executed successfully")
print("try except block ended here")