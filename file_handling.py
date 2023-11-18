
fp = "ipp.txt"


file = open(fp, 'w')
file.write("Hello, this is a sample file.")
file.close()
print("Content written to",fp, "successfully.")

file = open(fp, 'r')
content = file.read()
file.close()
print("Content read from ",fp,":",content)


file = open(fp, 'a')
file.write("\nThis is an appended line.")
file.close()
print("Content appended to ",fp," successfully.")


file = open(fp, 'r')
updated_content = file.read()
file.close()
print("Updated content read from ",fp," : ",updated_content)
