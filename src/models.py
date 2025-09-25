from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    id: int
    title: str
    tags: tuple
    priority: int
    done: bool = False
