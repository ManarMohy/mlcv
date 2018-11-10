import os

for file in os.listdir("."):
    if(file[0:3] == "dog"):
        os.rename(file, "dog." + file[3:])
    else:
        os.rename(file, "dog." + file)
