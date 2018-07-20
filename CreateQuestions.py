import re


class CreateQuestions:
    def create_questions(self, text):
        questions = {}
        self.when_questions(text, questions)
        self.how_much_questions(text, questions)
        self.where_questions(text, questions)
        return questions

    def when_questions(self, text, questions):
        for i, x in enumerate(text):
            if x.isdigit() and len(x) == 4:
                j = i - 1
                t = "?"
                while j >= 0 and text[j] != "." and text[j] != ",":
                    t = text[j] + " " + t
                    j = j-1
                t = "When does " + t
                if len(t.split()) > 5:
                    questions[t] = text[i]
                else:
                    j = i + 1
                    t = "When does"
                    while j <= len(text) and text[j] != "." and text[j] != ",":
                        t = t + " " + text[j]
                        j = j + 1
                    t = t + " ?"
                    if len(t.split()) > 5:
                        questions[t] = text[i]

    def how_much_questions(self, text, questions):
        for i, x in enumerate(text):
            if x.isdigit() and len(x) != 4:
                j = i - 1
                t = "?"
                while j >= 0 and text[j] != "." and text[j] != ",":
                    t = text[j] + " " + t
                    j = j-1
                t = "How much does " + t
                if len(t.split()) > 5:
                    questions[t] = text[i]
                else:
                    j = i + 1
                    t = "How much does"
                    while j <= len(text) and text[j] != "." and text[j] != ",":
                        t = t + " " + text[j]
                        j = j + 1
                    t = t + " ?"
                    if len(t.split()) > 5:
                        questions[t] = text[i]

    def where_questions(self, text, questions):
        for i, x in enumerate(text):
            if x == "in" and text[i+1].isupper():
                j = i - 1
                t = "?"
                while j >= 0 and text[j] != "." and text[j] != ",":
                    t = text[j] + " " + t
                    j = j-1
                t = "Where does " + t
                if len(t.split()) > 5:
                    questions[t] = text[i+1]
                else:
                    j = i + 1
                    t = "Where does"
                    while j <= len(text) and text[j] != "." and text[j] != ",":
                        t = t + " " + text[j]
                        j = j + 1
                    t = t + " ?"
                    if len(t.split()) > 5:
                        questions[t] = text[i+1]

