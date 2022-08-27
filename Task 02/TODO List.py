# Build todo list
# that reminds with with tasks in certain times , show the tasks as
# desktop notification

from plyer import notification
import datetime


def timer_checker(times_re):  
    tasks_times = {}
    for i in range(times_re):
        in_time = tuple(map(lambda a : int(a),input(f"Enter task:{i+1} time ?....\n>>").split(":"))) 
        tasks_times[in_time] = input(f"Write Your Task:{i+1} Message...\n>>")
        
    while True:
        for k,v in tasks_times.items():
            if k == tuple(map(lambda a : int(a),datetime.datetime.now().strftime('%X').split(":"))):
                notifier(v)
                tasks_times.pop(k)
                break
            elif k <= tuple(map(lambda a : int(a),datetime.datetime.now().strftime('%X').split(":"))):
                notifier(v)
                tasks_times.pop(k)
                break
        if len(tasks_times) == 0:
            return
    
                       
                       
def notifier(message):
    title = "TODO Tasks"
    notification.notify(title = title ,message = message,
                             app_icon ="clock.Ico",timeout = 10)


print("Welcom to my tasks alarmer ")
print(f"Current time >> {datetime.datetime.now().strftime('%X')} \nWe support only this time formate")
repetes = int(input("How many task you need to alarm \n>>"))
timer_checker(repetes)
print("thanks")
