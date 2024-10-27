def individual_serializers(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "complete": todo["complete"]
    }


def list_serializers(todos) -> list:
    return [individual_serializers(todo) for todo in todos] 





