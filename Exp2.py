# Create a Zip file

import shutil
folder_to_zip = "Files"       # The folder you want to zip
output_filename = "archive"

# Create zip file
shutil.make_archive(output_filename, 'zip', folder_to_zip)