from ReadFile import ReadFile

readfile = ReadFile()
file = open("./machinelearning.txt", 'r')
file_text = file.read()
file.close()
file_text = readfile.parse(file_text)
print(file_text)