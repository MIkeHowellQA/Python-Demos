tasks = []

# Add 5 blandly names tasks to the list of tasks
for taskNum in range(1,6):
    tasks.append (f"Task {taskNum}")

print (tasks)    

# Print each task
for task in tasks:
    print (task)

# See the python documentation for an explanation of enumerate.
# It takes each item in a data structure and encompases it in a tuple, the first item in the tuple is an index number
# (starting from a number of your choice) and the second item in the tuple is the current item being enumerated(listed).
for i, task in enumerate(tasks,1):
    print (f"Task # {i} Task: {task}")
           
print (list(enumerate(tasks, 400)))

i=input ("Enter the task number to delete")
completed = tasks.pop(int(i)-1)
# off by one = -1, list is zero based

print (f"The completed task is {completed}")

for i, task in enumerate(tasks,1):
    print (f"Task # {i} Task: {task}")

