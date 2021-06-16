from pymongo import MongoClient
import time
import json

print("-------------establishing connection with MongoDB---------------------")
client = MongoClient()
db = client.fake_news  # use a database called "fake_news"
collection = db.news   # and inside that DB, a collection called "news"
time.sleep(1)
print("-------------Done-----------")
print("--------------Inserting data into MongoDB--------------")
file_content = []
with open("FakeNews.txt" , encoding="utf8") as f:
    for line in f:
        lineContent =line.split(';')
        file_content.append({"text": lineContent[0],"label": lineContent[1].rstrip("\n")})

buffer = json.loads(json.dumps(file_content))
collection.insert_many(buffer)