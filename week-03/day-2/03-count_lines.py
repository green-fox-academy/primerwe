# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

file_name = input("Enter a filename: ")

def count_lines(file_name):
    try:
        with open(file_name) as myfile:
            count = sum(1 for line in myfile if line.rstrip('\n'))
            # line.rstrip()) for filter empty lines!
        return(count)
    except FileNotFoundError:
        return("0")

print(count_lines(file_name))