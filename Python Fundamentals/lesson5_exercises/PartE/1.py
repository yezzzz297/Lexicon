
def log_event(event_type, *messages, **metadata):
    result = {
        "event_type": event_type,
        "messages": list(messages),
        "metadata": metadata,
    }
    return result


print(log_event("login", "user signed in", "welcome back", user="Sam", role="admin"))
