import os
print("Installed Libraries:")
var = os.popen("conda list -n image-super-resolution").read()
print(var)