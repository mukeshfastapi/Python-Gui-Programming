# In the coding area we have defined a list of filenames. Your task is to:

# (1) loop over the list

# (2) print out the filename of each item without the extension using slicing.\

filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

for filename in filenames:
    print(filename.replace(".txt",""))