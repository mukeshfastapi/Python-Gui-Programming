# 1) loop over the list
#
# (2) print out the filename of each item without
# the extension using slicing and with the first letter capitalized.

filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

for filename in filenames:
    print(filename[:-4].capitalize())