
def show_event(event_type, **details):

    result = {"event_type": event_type}
    result.update(details)
    return result


print(show_event("login", user="Sam", successful=True))
print(show_event("purchase", amount=50, item="book"))
