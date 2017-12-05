# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"

file_name = input("Enter a filename: ")

try:
    my_file = open(file_name, "r")
    for x in my_file:
        print(x, end=' ')
except FileNotFoundError:
    print("Unable to read file: ", file_name)