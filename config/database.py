from pymongo import MongoClient

uri = "mongodb+srv://nasru:jasoos74.@appeul-cluster.p8rcu.mongodb.net/?retryWrites=true&w=majority&appName=appeul-cluster"

client = MongoClient(uri)

db = client.todo_db

collection_name = db.todo_collection




