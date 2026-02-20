# import os
# print(os.getcwd()) 
# Current workig directory
# PS D:\PY\Modules\OS> python -u "d:\PY\Modules\OS\os_module.py"
# D:\PY\Modules\OS

# import os 
# os.chdir("D:/PY")
# print(os.getcwd())
# change directory
# PS D:\PY\Modules\OS> python -u "d:\PY\Modules\OS\os_module.py"
# D:\PY

# import os
# files=os.listdir("D:/PY")
# print(files)
# it returns only name of entries [file and folders]
# PS D:\PY\Modules\OS> python -u "d:\PY\Modules\OS\os_module.py"
# ['.vscode', 'both.py', 'build', 'cv_live.py', 'Deepface.py', 'Dsa', 'Modules', 'Net_Ping', 'QRS', 'r.jpg', 'speech.py', 'Wepons', 'Wepons2']


# import os
# os.mkdir("by")
# creates new folder


# import os
# os.makedirs("HE/BY/KYU")
# creats nested dirs


# import os
# try:
#     os.remove("simple.txt")
#     print("File is deleted")
# except FileNotFoundError:
#     print("File Not Find")
# except OSError as e:
#     print(f"Errot {e}")
# To remove files only

# import os
# try:
#     os.rmdir("by")
#     print("folder is deleted")
# except FileNotFoundError:
#     print("Not Found")
# except OSError as e:
#     print(f"Error {e}")
# To delete Empty Folder

# import os
# try:
#     os.rename("HI","Demo")
#     print("renamed")
# except FileExistsError:
#     print("Alrady Exists")
# except FileNotFoundError:
#     print("Not Found")
# except OSError as e:
#     print(f"Error {e}")
# To rename and move the file


# import os
# os.path.join("Demo","txt")
# it joins the paths

# import os
# os.path.exists("txt8.txt")
# Check the path exist

# import os
# print(os.environ)
# returns environment var list 

# import os 
# r=os.system("ls")
# print(r)
# uses as cmd





