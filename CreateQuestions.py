import random
import re
import string


class CreateQuestions:
    def create_questions(self, text):
        questions = {}
        self.when_questions(text, questions)
        self.how_much_questions(text, questions)
        self.where_questions(text, questions)
        self.who_quesions(text, questions)
        for key, value in questions.items():
            random.shuffle(value)

        return questions

    def when_questions(self, text, questions):
        for index, word in enumerate(text):
            if word.isdigit() and len(word) == 4:
                pre_index = index - 1
                question = "?"
                while pre_index >= 0 and text[pre_index] != "." and text[pre_index] != ",":
                    question = text[pre_index] + " " + question
                    pre_index = pre_index - 1
                question = "When does " + question
                if len(question.split()) > 5:
                    answer = int(text[index])
                    questions[question] = [answer, answer + random.randrange(-10, 10),
                                           answer + random.randrange(-10, 10),
                                           answer + random.randrange(-10, 10)]
                else:
                    pre_index = index + 1
                    question = "When does"
                    while pre_index <= len(text) and text[pre_index] != "." and text[pre_index] != ",":
                        question = question + " " + text[pre_index]
                        pre_index = pre_index + 1
                    question = question + " ?"
                    if len(question.split()) > 5:
                        answer = int(text[index])
                        questions[question] = [answer, answer + random.randrange(-10, 10),
                                               answer + random.randrange(-10, 10),
                                               answer + random.randrange(-10, 10)]

    def how_much_questions(self, text, questions):
        for i, x in enumerate(text):
            if x.isdigit() and len(x) != 4:
                j = i - 1
                t = "?"
                while j >= 0 and text[j] != "." and text[j] != ",":
                    t = text[j] + " " + t
                    j = j - 1
                t = "How much does " + t
                if len(t.split()) > 5:
                    answer = int(text[i])
                    questions[t] = [answer, answer + random.randrange(-10, 10),
                                    answer + random.randrange(-10, 10),
                                    answer + random.randrange(-10, 10)]
                else:
                    j = i + 1
                    t = "How much does"
                    while j <= len(text) and text[j] != "." and text[j] != ",":
                        t = t + " " + text[j]
                        j = j + 1
                    t = t + " ?"
                    if len(t.split()) > 5:
                        answer = int(text[i])
                        questions[t] = [answer, ''.join(random.choices(string.ascii_uppercase)) + ''.join(
                            random.choices(string.ascii_lowercase, k=len(answer) - 1)),
                                        ''.join(random.choices(string.ascii_uppercase)) + ''.join(
                                            random.choices(string.ascii_lowercase, k=len(answer) - 1)),
                                        ''.join(random.choices(string.ascii_uppercase)) + ''.join(
                                            random.choices(string.ascii_lowercase, k=len(answer) - 1))]

    def where_questions(self, text, questions):
        for i, x in enumerate(text):
            if x == "in" and text[i + 1].istitle():
                j = i - 1
                t = "?"
                while j >= 0 and text[j] != "." and text[j] != ",":
                    t = text[j] + " " + t
                    j = j - 1
                t = "Where does " + t
                answer = text[i + 1]
                if len(t.split()) > 5:
                    questions[t] = [answer, ''.join(random.choices(string.ascii_uppercase)) + ''.join(
                        random.choices(string.ascii_lowercase, k=len(answer) - 1)),
                                    ''.join(random.choices(string.ascii_uppercase)) + ''.join(
                                        random.choices(string.ascii_lowercase, k=len(answer) - 1)),
                                    ''.join(random.choices(string.ascii_uppercase)) + ''.join(
                                        random.choices(string.ascii_lowercase, k=len(answer) - 1))]
                else:
                    j = i + 1
                    t = "Where does"
                    while j <= len(text) and text[j] != "." and text[j] != ",":
                        t = t + " " + text[j]
                        j = j + 1
                    t = t + " ?"
                    answer = text[i + 1]
                    if len(t.split()) > 5:
                        questions[t] = [answer, ''.join(random.choices(string.ascii_uppercase)) + ''.join(
                            random.choices(string.ascii_lowercase, k=len(answer) - 1)),
                                        ''.join(random.choices(string.ascii_uppercase)) + ''.join(
                                            random.choices(string.ascii_lowercase, k=len(answer) - 1)),
                                        ''.join(random.choices(string.ascii_uppercase)) + ''.join(
                                            random.choices(string.ascii_lowercase, k=len(answer) - 1))]

    def who_quesions(self, text, questions):
        for i, x in enumerate(text):
            if x == "by" and text[i + 1].istitle():
                j = i - 1
                t = "?"
                while j >= 0 and text[j] != "." and text[j] != ",":
                    t = text[j] + " " + t
                    j = j - 1
                t = "Who does " + t
                answer = ""
                x = i
                while text[x + 1].istitle():
                    answer = answer + text[x + 1] + " "
                    x = x + 1
                if len(t.split()) > 5:
                    questions[t] = [answer, ''.join(random.choices(string.ascii_uppercase)) + ''.join(
                        random.choices(string.ascii_lowercase, k=len(answer) - 1)),
                                    ''.join(random.choices(string.ascii_uppercase)) + ''.join(
                                        random.choices(string.ascii_lowercase, k=len(answer) - 1)),
                                    ''.join(random.choices(string.ascii_uppercase)) + ''.join(
                                        random.choices(string.ascii_lowercase, k=len(answer) - 1))]
                else:
                    j = i + 1
                    t = "Who does"
                    while j <= len(text) and text[j] != "." and text[j] != ",":
                        t = t + " " + text[j]
                        j = j + 1
                    t = t + " ?"
                    answer = ""
                    x = i
                    while text[x + 1].istitle():
                        answer = answer + text[x + 1] + " "
                        x = x + 1
                    if len(t.split()) > 5:
                        questions[t] = [answer, ''.join(random.choices(string.ascii_uppercase)) + ''.join(
                            random.choices(string.ascii_lowercase, k=len(answer) - 1)),
                                        ''.join(random.choices(string.ascii_uppercase)) + ''.join(
                                            random.choices(string.ascii_lowercase, k=len(answer) - 1)),
                                        ''.join(random.choices(string.ascii_uppercase)) + ''.join(
                                            random.choices(string.ascii_lowercase, k=len(answer) - 1))]
