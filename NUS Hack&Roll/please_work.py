import io
import os
list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk('/Users/vivekadrakatti/Documents/'):
    for filename in filenames:
        if filename.endswith('.jpg'):
            list_of_files[filename] = os.sep.join([dirpath, filename])
print(list_of_files)
