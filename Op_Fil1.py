file = open("notes_cleaner.txt","r")
preview = int(input("How many characters to preview: "))
name = file.read(preview)
print(name)

file = open("notes_cleaner.txt","r")
line = file.readlines()
for i in line:
    print(i.strip())
subject = input("Which subject should we skip: ")

file = open("notes_cleaner.txt","r")

for line,number in enumerate(file,start=1):
    if subject.lower() in number.lower():
        print("line skipped ",line)
    else:
        print("keep ",line)
