import os


class Reader:
    def __init__(self, day, filename):
        self.day = day
        self.filename = filename
    
    def read(self) -> str:
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/input/' + self.day + '/' + self.filename
        text_file = open(path, 'r')
        data = text_file.read()
        text_file.close()
        return data

