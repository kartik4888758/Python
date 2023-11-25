#file=open("new.txt","x")
#file1=open("new.txt","w")
#file1.write("water is essential for body.")
#file2=open("new.txt","r")
# reader=file2.read()
# print(reader)

file=open("new.txt","a")
adder="about 3 l of water is recommended for daily drinking."
file.write(adder)
file.close()
file2=open("new.txt","r")
readerere=file2.read()
print(readerere)


