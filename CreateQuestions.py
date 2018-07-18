import re


class CreateQuestions:
    def __init__(self):
        self.contain_number = re.compile(".*\d.*")
