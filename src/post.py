# TODO: add more copyright info
# Licensed under the MIT License 

class Post:
    def __init__(self, title, post, date):
        self.properties = {
            "title": title,
            "post" : post,
            "date" : date,
        }

    def addTags(self, tags):
        self.tags = tags
 
    def compile(self):
        return ""

class Property:
    def compile(self): abstract

class Title(Property):
    pass

class Post(Property):
    pass

class Date(Property):
    pass

  
    
