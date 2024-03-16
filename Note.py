import count
from datetime import datetime

class Note:
    def __init__(self, id=str(count.counter()),title="Text",content="Content",
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.content = content
        self.date = date

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_date(self):
        return self.date

    def set_id(self):
        self.id =str(count.counter())

    def set_title(self):
        self.title =self

    def set_content(self):
        self.content = self

    def set_date(self):
        self.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(self):
        return self.id + ';' + self.title + ';' + self.content + ';' + self.date

    def map_note(note):
        return '\nID: ' + note.id + '\n' + 'Название: ' + note.title + '\n' + 'Описание: ' + note.content + '\n' + 'Дата публикации: ' + note.date