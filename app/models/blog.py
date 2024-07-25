from datetime import datetime

class Blog:
    def __init__(self, title, author, category, content):
        self.title = title
        self.author = author
        self.content = content
        self.category = category
        self.date = datetime.utcnow() # time of creation



    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'category': self.category,
            'content': self.content,
            'date': self.date
        }

    
    