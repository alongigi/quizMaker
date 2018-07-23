from CreateQuestions import CreateQuestions
from ReadFile import ReadFile
from View import View

v = View()
v.start()
readfile = ReadFile()
createQuestions = CreateQuestions()
file = open("./text.txt", 'r')
file_text = file.read()
file.close()
file_text = readfile.parse(file_text)
questions = createQuestions.create_questions(file_text)
for q in questions:
    print(q)
    for answer in questions.get(q):
        print(answer)
