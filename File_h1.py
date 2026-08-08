#A Python program that creates a bucket-list.txt file and works with it in five steps:
#  write three items to the file using 'w' mode, read the full content back using read(),
#  count the items using readlines() and len(), append two more items using 'a' mode,
#  and read the final updated file to confirm everything is saved.

file = open("bucket-list.txt","w")

file.write("Visit paris\n")
file.write("Visit Lyon\n")
file.write("Go bald\n")

with open("bucket-list.txt","r") as file:
    content = file.read()

print(content)

with open("bucket-list.txt","r") as file:
    item = file.readlines()
print(len(item))

with open("bucket-list.txt","a") as file:
    file.write("Put shoes on a table\n")
    file.write("Go to mars\n")

with open("bucket-list.txt","r") as file:
    final_content = file.read()
print(final_content)