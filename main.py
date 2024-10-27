

from fastapi import FastAPI
from typing import Optional
# from pymongo.mongo_client import MongoClient

from routes.route import todo_router



app = FastAPI()

app.include_router(todo_router)








# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}









# uri = "mongodb+srv://nasru:jasoos74.@appeul-cluster.p8rcu.mongodb.net/?retryWrites=true&w=majority&appName=appeul-cluster"

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)