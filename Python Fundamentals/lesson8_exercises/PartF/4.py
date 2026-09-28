# Call send on each type of notification

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
