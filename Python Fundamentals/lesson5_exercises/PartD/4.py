
def keep_valid_settings(**settings):
    result = {}
    for key, value in settings.items():
        if value is not None:
            result[key] = value
    return result


print(keep_valid_settings(theme="dark", font_size=None, language="en"))
