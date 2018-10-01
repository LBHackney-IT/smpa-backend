from molten import field, schema
from typing import Optional
from inspect import Parameter

from ..helpers.sqlite import DB


@schema
class Todo:
    id: Optional[int] = field(response_only=True)
    description: str
    status: str = field(choices=["todo", "done"], default="todo")


class TodoManager:
    def __init__(self, db: DB) -> None:
        self.db = db

    def create(self, todo: Todo) -> Todo:
        with self.db.get_cursor() as cursor:
            cursor.execute("insert into todos(description, status) values(?, ?)", [
                todo.description,
                todo.status,
            ])

            todo.id = cursor.lastrowid
            return todo


class TodoManagerComponent:
    is_cacheable = True
    is_singleton = True

    def can_handle_parameter(self, parameter: Parameter) -> bool:
        return parameter.annotation is TodoManager

    def resolve(self, db: DB) -> TodoManager:
        return TodoManager(db)


def create_todo(todo: Todo, todo_manager: TodoManager) -> Todo:
    return todo_manager.create(todo)
