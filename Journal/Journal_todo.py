# Day to  Day task journal

date = input("Enter today date:")
mood = input("How do you rate your mood today:")
journal = input("Let Your daily task:")

with open(f"{date}.txt", "w")as file:
    file.write(mood + "\n")
    file.write(journal)