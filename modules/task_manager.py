from datetime import datetime
def add_task(tasks, name, description, deadline, priority):
    """
    ПУНКТ 1: Добавить задачу (название, описание, дедлайн, приоритет)
    Параметры:
    - tasks: список всех задач
    - name: название задачи
    - description: описание задачи
    - deadline: дата дедлайна в формате ГГГГ-ММ-ДД
    - priority: приоритет (high/medium/low)
    
    Возвращает: обновлённый список задач
    """
    if priority not in ['high', 'medium', 'low']:
        print("Ошибка: приоритет должен быть high/medium/low")
        return tasks
    new_task = [name, description, deadline, priority, 'not_done']
    tasks.append(new_task)
    print(f"Задача '{name}' добавлена! Дедлайн: {deadline}, Приоритет: {priority}")
    return tasks

def view_tasks(tasks, filter_priority=None, filter_status=None):
    """
    ПУНКТ 2: Просмотр задач с фильтрацией по приоритету и/или статусу
    Параметры:
    - tasks: список всех задач
    - filter_priority: "high", "medium", "low" или None (без фильтра)
    - filter_status: "done", "not_done" или None (без фильтра)
    Возвращает: отфильтрованный список задач
    """
    filtered = tasks.copy()
    if filter_priority is not None:
        filtered = [task for task in filtered if task[3] == filter_priority]
    if filter_status is not None:
        filtered = [task for task in filtered if task[4] == filter_status]
    return filtered

def display_tasks(tasks):
    """
    Красиво выводит список задач в консоль
    """
    if not tasks:
        print("\n Нет задач для отображения")
        return 
    print('\n' + '=' * 65)
    for i, task in enumerate(task, 1):
        name, description, deadline, priority, status = task
        if status == 'done':
            status_text = "ВЫПОЛНЕНО"
        else:
            status_text = 'В РАБОТЕ'

        if priority == "high":
            priority_icon = "ВЫСОКИЙ ПРИОРИТЕТ"
        elif priority == "medium":
            priority_icon = "СРЕДНИЙ ПРИОРИТЕТ"
        else:
            priority_icon = "НИЗКИЙ ПРИОРИТЕТ"
        
        is_hot = False
        try:
            deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
            days_left = (deadline_date - datetime.now()).days
            if 0 <= days_left <= 2 and status == "not_done":
                is_hot = True
        except:
            pass
        hot_marker = "ГОРЯЩАЯ!" if is_hot else ""
        
        print(f"\n [{i}] {name} {hot_marker}")
        print(f"   {description}")
        print(f"   Дедлайн: {deadline} | Приоритет: {priority_icon}")
        print(f"   Статус: {status_text}")
        print("-" * 65)
    
    print(f"\nИТОГО: {len(tasks)} задач(и)")


def get_all_tasks(tasks):
    """
    Возвращает все задачи (без фильтров)
    """
    return tasks