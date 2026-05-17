from datetime import datetime

# Сортировка по дедлайну
def sort_by_deadline(tasks, reverse=False):
    return sorted(tasks, key=lambda t: t[2], reverse=reverse)

# Статистика 
def show_statistics(tasks):
    if not tasks:
        print("Отчет: задач пока нет.")
        return
    
    total = len(tasks)
    done = sum(1 for t in tasks if t[4] == "done")
    today = datetime.now().date().strftime("%Y-%m-%d")
    overdue = sum(1 for t in tasks if t[4] == "not_done" and t[2] < today)
    
    print("\n" + "=" * 40)
    print("СТАТИСТИКА ЗАДАЧ")
    print("=" * 40)
    print(f"Всего задач: {total}")
    print(f"Выполнено: {done}")
    print(f"Не выполнено: {total - done}")
    print(f"Просрочено: {overdue}")
    print(f"Процент выполнения: {round(done / total * 100, 1)}%")
