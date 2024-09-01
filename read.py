file = open("File Mgt Project/sample.txt", "r")
content = file.read()
file.close()
print(f"Content of Sample file is {content}")