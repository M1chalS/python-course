import os
import shutil

path = "emptyfolder"

try:
    os.remove(path)
    # os.rmdir(path)  # usuwa folder
    # shutil.rmtree(path)  # usuwa rekurencyjnie pliki i foldery
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You dont have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")
