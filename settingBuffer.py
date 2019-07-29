import os
import shutil

dir_path = "./server"
client_path = "./client"

script_list = os.listdir('proto')
script_list = sorted(script_list)

if os.path.exists(dir_path + "/WebApplication/Document/Protocol"):
    shutil.rmtree(dir_path + "/WebApplication/Document/Protocol")

if os.path.exists(client_path + "/WebApplication/Document/Protocol"):
    shutil.rmtree(client_path + "/WebApplication/Document/Protocol")

for filename in script_list:
    print(filename)
    os.system('"flatc.exe -p -o "' + dir_path + " ./proto/" + filename)
    os.system('"flatc.exe -p -o "' + client_path + " ./proto/" + filename)

Python_script_list = os.listdir(dir_path + "/WebApplication/Document/Protocol/Definition")
header_text = ""

for filename in Python_script_list:
    if "__init__.py" in filename:
        continue

    if "__pycache__" in filename:
        continue

    header_text += "from WebApplication.Document.Protocol.Definition." + filename.replace(".py", "") +" import *\n"

with open(dir_path + "/WebApplication/Document/Protocol/protocol.py", "w") as f:
    f.write(header_text)

with open(client_path + "/WebApplication/Document/Protocol/protocol.py", "w") as f:
    f.write(header_text)

