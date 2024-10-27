from fastapi import APIRouter, HTTPException, status
from config.database import collection_name
from models.todos import Todo
from schema.schemas import list_serializers, individual_serializers
from bson import ObjectId

todo_router = APIRouter()

@todo_router.post("/todo", status_code=status.HTTP_201_CREATED)
async def add_todo(todo: Todo):
    collection_name.insert_one(dict(todo))
    return todo


@todo_router.get("/todos", response_model=list[Todo])
async def get_todos():
    todos = list_serializers(collection_name.find())
    return todos


@todo_router.get("/todo/{id}", response_model=Todo)
async def get_todo(id: str):
    todo = collection_name.find_one({"_id": ObjectId(id)})
    if todo:
        return individual_serializers(todo)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {id} not found")


@todo_router.put("/todo/{id}", response_model=Todo)
async def update_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    return individual_serializers(collection_name.find_one({"_id": ObjectId(id)}))



@todo_router.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return Response(status_code=status.HTTP_204_NO_CONTENT)



