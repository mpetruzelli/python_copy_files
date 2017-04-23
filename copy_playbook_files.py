# Author: Mike Petruzelli
# Email: Mike.petruzelli@capitalone.com
# All rights reserved

import os
import shutil

src = "/Users/Mike/personal_github/jinja_testing/roles"
role_folders = os.listdir(src)

for folder_name in role_folders:
    directory_path = os.path.join(src, folder_name)
    if not os.path.isfile(directory_path):
        file_name = os.listdir(directory_path)
        for files in file_name:
            if ".yml" in files:
                shutil.copy(os.path.join(directory_path, files),src)

