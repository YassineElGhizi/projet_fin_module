from mongoengine import Document
from mongoengine.fields import StringField

class News(Document):
    meta : {'collection' : 'news'}
    text = StringField()
    label = StringField()