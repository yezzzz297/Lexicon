
def merge_settings(defaults, **overrides):
    merged = dict(defaults)
    merged.update(overrides)
    return merged


defaults = {"theme": "light", "language": "en", "notifications": True}
settings = merge_settings(defaults, theme="dark", notifications=False)
print(defaults)
print(settings)
