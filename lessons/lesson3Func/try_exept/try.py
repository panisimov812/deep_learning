title = ' Python in Easy Steps'
try:
    print(title1)
except (NameError, IndexError) as msg:
    print(msg)