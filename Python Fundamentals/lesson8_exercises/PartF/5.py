# Explain which method is called

class Notification:
    def send(self):
        return "Sending a notification."


class EmailNotification(Notification):
    def send(self):
        return "Sending an email."


class SMSNotification(Notification):
    def send(self):
        return "Sending an SMS."


notification = Notification()
email = EmailNotification()
sms = SMSNotification()
print(notification.send())
print(email.send())
print(sms.send())


# notification uses Notification.send().
# email uses EmailNotification.send().
# sms uses SMSNotification.send().
# Each subclass uses its own version of send().
