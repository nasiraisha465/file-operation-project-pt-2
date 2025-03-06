# write in file using with()fuction
with open('Codingal.txt','w') as file:
    file.write("hi! I am aisha and i am 15 yr old.")
file.close()

# split file into words
with open('Codingal.txt','r') as file:
    data = file.readlines()
    print("words in this file are.....")
    for line in data:
        word = line.split()
        print (word)
file.close()
