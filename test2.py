# this snippet checks each line in a file for the number of words present
# you may test it with other file types
with open('Sample2.txt') as f:
    x = f.readlines()
    for i in range(0, len(x)):
        a = x[i].split()
        no = len(a)
        print(f'Line {i+1}: {no} words')



