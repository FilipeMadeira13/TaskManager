from src.tasks import (
    add_task,
    create_task,
    filter_tasks,
    get_titles,
    make_tag_filter,
    mark_done,
    remove_task,
    sort_by_priority,
)


def test_create_and_add():
    tasks = []
    t1 = create_task(1, "Comprar leite", ["compras"], 2)
    tasks = add_task(tasks, t1)
    assert len(tasks) == 1
    assert tasks[0].title == "Comprar leite"


def test_remove_and_mark_done():
    t1 = create_task(1, "A", [], 1)
    t2 = create_task(2, "B", [], 2)
    tasks = [t1, t2]
    tasks = remove_task(tasks, 1)
    assert len(tasks) == 1 and tasks[0].id == 2

    # mark done
    tasks = [t1, t2]
    tasks2 = mark_done(tasks, 2)
    assert any(t.done for t in tasks2 if t.id == 2)


def test_filter_and_sort():
    t1 = create_task(1, "A", ["x"], 3)
    t2 = create_task(2, "B", ["y"], 1)
    t3 = create_task(3, "C", ["x"], 2)
    tasks = [t1, t2, t3]
    tag_x = make_tag_filter("x")
    filtered = filter_tasks(tasks, tag_x)
    assert len(filtered) == 2
    sorted_tasks = sort_by_priority(filtered)
    assert [t.id for t in sorted_tasks] == [3, 1]


def test_get_titles():
    t1 = create_task(1, "AAA", [], 1)
    assert get_titles([t1]) == ["AAA"]
