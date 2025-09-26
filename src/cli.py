from typing import List

from .models import Task
from .tasks import (
    add_task,
    create_task,
    filter_tasks,
    get_titles,
    make_tag_filter,
    mark_done,
    remove_task,
    sort_by_priority,
)


def print_tasks(tasks: List[Task], title: str = "Tarefas"):
    print(f"\n--- {title} (total: {len(tasks)}) ---")
    if not tasks:
        print("  (nenhuma tarefa)")
        return
    for t in tasks:
        status = "✓" if t.done else " "
        tags = ", ".join(t.tags) if t.tags else "-"
        print(
            f"[{status}] id={t.id} | título: {t.title} | prioridade: {t.priority} | tags: {tags}"
        )


def next_id(tasks: List[Task]) -> int:
    return 1 if not tasks else max(t.id for t in tasks) + 1


def input_tags() -> List[str]:
    raw = input("Tags (separadas por vírgula, opcional): ").strip()
    if not raw:
        return []
    return [tag.strip() for tag in raw.split(",") if tag.strip()]


def menu():
    tasks: List[Task] = []

    while True:
        print("\n=== GERENCIADOR DE TAREFAS (MENU) ===")
        print("1) Adicionar tarefa")
        print("2) Listar todas as tarefas")
        print("3) Listar tarefas pendentes")
        print("4) Filtrar por tag")
        print("5) Listar ordenadas por prioridade")
        print("6) Marcar tarefa como concluída")
        print("7) Remover tarefa")
        print("8) Mostrar títulos (exemplo map)")
        print("0) Sair")
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            title = input("Título: ").strip()
            if not title:
                print("Título não pode ser vazio.")
                continue
            tags = input_tags()
            try:
                priority = int(
                    input("Prioridade (inteiro, menor = mais importante): ").strip()
                )
            except ValueError:
                print("Prioridade inválida — usando 1 por padrão.")
                priority = 1
            tid = next_id(tasks)
            t = create_task(tid, title, tags, priority)
            tasks = add_task(tasks, t)
            print(f"Tarefa adicionada com id={tid}.")

        elif choice == "2":
            print_tasks(tasks, "Todas as tarefas")

        elif choice == "3":
            pendentes = [t for t in tasks if not t.done]
            print_tasks(pendentes, "Tarefas pendentes")

        elif choice == "4":
            tag = input("Tag a filtrar: ").strip()
            if not tag:
                print("Tag vazia.")
                continue
            predicate = make_tag_filter(tag)
            filtradas = filter_tasks(tasks, predicate)
            print_tasks(filtradas, f"Tarefas com tag '{tag}'")

        elif choice == "5":
            ordered = sort_by_priority(tasks)
            print_tasks(ordered, "Tarefas ordenadas por prioridade (menor -> maior)")

        elif choice == "6":
            try:
                tid = int(input("ID da tarefa a marcar como concluída: ").strip())
            except ValueError:
                print("ID inválido.")
                continue
            tasks = mark_done(tasks, tid)
            print(f"Se existir, a tarefa id={tid} foi marcada como concluída.")

        elif choice == "7":
            try:
                tid = int(input("ID da tarefa a remover: ").strip())
            except ValueError:
                print("ID inválido.")
                continue
            tasks = remove_task(tasks, tid)
            print(f"Se existir, a tarefa id={tid} foi removida.")

        elif choice == "8":
            titles = get_titles(tasks)
            print("\nTítulos:")
            for idx, tt in enumerate(titles, start=1):
                print(f"  {idx}. {tt}")

        elif choice == "0":
            print("Saindo... até a próxima!")
            break

        else:
            print("Opção inválida. Digite o número da opção desejada.")


if __name__ == "__main__":
    menu()
