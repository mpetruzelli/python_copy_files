# Author: Mike Petruzelli
# Email: Mike.petruzelli@capitalone.com
# All rights reserved

# The intent of this file is to move playbook.yml files
# Jinja templating can only occur from folders below the playbook location
# This script assumes you have used ansible-galaxy to install roles
# to a "roles" path.
# The script will walk 1 directory down from "roles" and copy
# any *.yml files it finds, up to the "roles" directory.
# This will allow you to use jinja templating in multiple roles.
# or even call templates from other roles, using relative paths.

import os
import shutil

#src = "path/to/playbook/diectory/roles"
role_folders = os.listdir(src)

for folder_name in role_folders:
    directory_path = os.path.join(src, folder_name)
    if not os.path.isfile(directory_path):
        file_name = os.listdir(directory_path)
        for files in file_name:
            if ".yml" in files:
                shutil.copy(os.path.join(directory_path, files),src)

