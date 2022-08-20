# Build an alarm clock
# build an alarm clock for yourself , you can set multiple alarms ,
# the alarm should show desktop notification

from plyer import notification
import datetime


def alarm(times_re):
    alarm_ = []
    for i in range(times_re):
        in_alarm = list(map(lambda a : int(a),input(f"Set alarm:{i+1} time being notified ....\n>>").split(":")))
        alarm_.append(in_alarm)

    while True:
        for i in alarm_:
            if i == list(map(lambda a : int(a),datetime.datetime.now().strftime('%X').split(":"))):
                alarm_.remove(i)
                notifier()
                break
            elif  i <= list(map(lambda a : int(a),datetime.datetime.now().strftime('%X').split(":"))):
                notifier()
                alarm_.remove(i)   
        if len(alarm_) == 0 :
            break


def notifier():
    title = "Alarm Clock"
    message = "It's time to being notified "
    notification.notify(title = title ,message = message,
                                app_icon ="clock.Ico",timeout = 10 )


now_ = datetime.datetime.now().strftime('%X')
print(f"Welcome to my clock, Set alarm... \nCurrent Time {now_}")
times_repete = int(input("How many alarms you want to add \n>>"))
alarm(times_repete)
print("thanks")

