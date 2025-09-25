from dataclasses import replace
from typing import Callable, List

from .models import Task


# 1) função pura para criar tarefa
def create_task(id: int, title: str, tags: List[str], priority: int) -> Task:
    return Task(id=id, title=title, tags=tuple(tags), priority=priority, done=False)


# 2) adicionar (retorna nova lista -> imutabilidade funcional)
def add_task(tasks: List[Task], task: Task) -> List[Task]:
    return tasks + [task]


# 3) remover (retorna nova lista)
def remove_task(tasks: List[Task], task_id: int) -> List[Task]:
    return [t for t in tasks if t.id != task_id]


# 4) marcar como done (retorna nova lista)
def mark_done(tasks: List[Task], task_id: int) -> List[Task]:
    def _mark(t: Task) -> Task:
        return replace(t, done=True) if t.id == task_id else t

    return [_mark(t) for t in tasks]


# 5) função de ordem superior: filtrar usando predicate
def filter_tasks(tasks: List[Task], predicate: Callable[[Task], bool]) -> List[Task]:
    return [t for t in tasks if predicate(t)]


# 6) closure: fábrica de predicate por tag
def make_tag_filter(tag: str) -> Callable[[Task], bool]:
    def predicate(task: Task) -> bool:
        return tag in task.tags

    return predicate


# 7) lambda: ordenar por prioridade usando key func padrão (lambda)
def sort_by_priority(
    tasks: List[Task], reverse: bool = False, key_func=lambda t: t.priority
) -> List[Task]:
    return sorted(tasks, key=key_func, reverse=reverse)


# 8) obter apenas títulos (exemplo de map via list comprehension)
def get_titles(tasks: List[Task]) -> List[str]:
    return [t.title for t in tasks]
