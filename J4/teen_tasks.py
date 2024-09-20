restrictions = [(1, 7), (1, 4), (2, 1), (3, 4), (3, 5)]

while True:
    x = int(input())
    y = int(input())
    if x == 0 and y == 0:
        break
    restriction = (x, y)
    restrictions.append(restriction)

task_list = []
possible_tasks = []
tasks = [1, 2, 3, 4, 5, 6, 7]

while True:
    # check task eligibility
    for task in tasks:
        possible = True
        for restriction in restrictions:
            if task == restriction[1]:
                possible = False
        if possible:
            possible_tasks.append(task)

    # check if task list is done or impossible
    if len(possible_tasks) == 0 and len(tasks) != 0:
        print("Cannot complete these tasks. Going to bed.")
        break
    elif len(possible_tasks) == 0 and len(tasks) == 0:
        for task in task_list:
            print(task, end=' ')
        break

    # perform a task
    possible_tasks.sort()
    selected_task = possible_tasks[0]
    task_list.append(selected_task)
    tasks.remove(selected_task)

    # remove restrictions involving selected task
    removed_restrictions = []
    for restriction in restrictions:
        if selected_task in restriction:
            removed_restrictions.append(restriction)
    
    for removed_restriction in removed_restrictions:
        restrictions.remove(removed_restriction)
    
    possible_tasks = []