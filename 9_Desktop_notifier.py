from plyer import notification
# import notify2

title = "Hello World"
message = "This is a test message"


def method_1():
    notification.notify(title=title,
                        message=message,
                        # app_name="App Notifier",
                        # ticker = "test",
                        app_icon = None,
                        timeout = 3,
                        toast = False)

# def method_2():
#     notify2.init("Python App")
#     n = notify.Notification(summary="Hello",message="This is a test",icon=None)
#     n.set_timeout(3000)

method_1()
