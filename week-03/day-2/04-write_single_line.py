# Open a file called "my-file.txt"
# Write your name in it as a single line
# If the program is unable to write the file,
# then it should print an error message like: "Unable to write file: my-file.txt"

file_name = input("Enter a filename: ")

try:
    my_file = open(file_name, "w")
    my_file.write("Hello")
    my_file.close()
except Exception:
    print("Unable to write file: ", file_name)

my_file = open(file_name)
sample = my_file.read()
my_file.close()
print(sample)