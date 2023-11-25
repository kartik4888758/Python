# file=open("test.txt","x")

#reading from file
file1=open("test.txt","r")
read=file1.read()
print(read)

#closing file
file1.close()

#writing into file
file2=open("test2.txt","w")
file2.write('Fruits are good sources of antioxidants.')
file2=open("test2.txt","r")
reader=file2.read()
print(reader)

#appending into existing file
file2=open("test2.txt","w")
text_append="Fruits are good for immunity building."
file2.write(text_append)
file2=open("test2.txt","r")
reader1=file2.read()
print(reader1)
#closing after operations
file1.close()
file2.close()

    
    