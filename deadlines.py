def dedline_check(tasks):
    for task in tasks:
        if task[2] <= 2:
            task[0] = task[0].upper()
    return tasks

tasks_list = [["cleaning", "to clean", 5, "low"], ["swiping", "to swipe", 2, "high"], ["drinking", "to drink", 5, "high"]]
new = dedline_check(tasks_list)
print(new)