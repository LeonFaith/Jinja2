import os 


# create new directory
dir_name = "config_files"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Directory {dir_name} created.")
else: 
    print(f"Directory {dir_name} already exists.")


# create new file in new directory
file_name = "config.txt"
file_path = os.path.join(dir_name, file_name)

with open(file_path, "w") as file:
    file.write("hostname router1\n")
    print(f"File {file_path} created.")
