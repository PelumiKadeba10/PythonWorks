# the file must be in the same directory
# myfile = open('sample.txt')
# r --> open in read mode: default mode
# w --> open in write mode, to rewrite the contents
# a --> open in append mode, to add content to the file
# b --> opens in binary mode, used for non-text files
# write mode
# open("sample.txt", "w")

# read mode
# open("sample.txt", "r")
# open("sample.txt")

# binary write mode
# open("sample.txt", "wb")

# To read only a certain amount of a file, you can provide the number of bytes to read to the read function.
# Each ASCII character is 1 byte
file = open('sample.txt')
print(file.read())
file.close()

# readlines method converts the text to a list that you can then manipulate
file = open('sample.txt')
x = file.readlines()
print(x[0])
file.close()

# to write into a file, use the write method
# The write method returns the number of bytes written to a file, if successful.
file = open('newfile.txt', 'w')
file.write('This ia a new file and this text is written into it')
msg = 'This ia a new file and this new text is written into it'
amount = file.write(msg)
print(amount)
file.close()

# with statement --> to close files easily, files will be closed at the end of the with statement
with open("sample.txt") as f:
  print(f.read())

# this code checks each line and prints the number of words there
with open('Sample2.txt') as f:
    x = f.readlines()
    for i in range(0, len(x)):
        a = x[i].split()
        no = len(a)
        print(f'Line {i+1}: {no} words')
