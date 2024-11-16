from pymongo import MongoClient

url = 'mongodb+srv://dgtrons:hkC8zcL8GVE1YnI1@cluster0.'\
      'wonss.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(url)

db = client.question

collection_name = db["question_collection"]
