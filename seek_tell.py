#Seek() method is used to change the current file pointer location by desired points by user 

file=open("test2.txt",'r')
file.seek(10)
reader=file.read()
print(reader)


#tell() method is used to locate the current positioning of pointer in file.

file=open("test.txt",'r')
data=file.read(20)
print("data read:",data)
position=file.tell()
print("current location:",position)