import re


class CreateQuestions:
    def create_questions(self, text):
        q1 = self.when_questions(text)
        return q1

    def when_questions(self, text):
        qa = {}
        for i, x in enumerate(text):
            if x.isdigit() and len(x) == 4:
                j = i - 1
                t = "?"
                while j >= 0 and text[j] != "." and text[j] != ",":
                    t = text[j] + " " + t
                    j = j-1
                t = "When does " + t
                if len(t.split()) > 7:
                    qa[t] = text[i]
                else:
                    j = i + 1
                    t = "When does"
                    while text[j] != "." and text[j] != ",":
                        t = t + " " + text[j]
                        j = j + 1
                    t = t + " ?"
                    if len(t.split()) > 7:
                        qa[t] = text[i]
        return qa
