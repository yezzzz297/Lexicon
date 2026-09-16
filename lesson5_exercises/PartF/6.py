
def create_report(title, *sections, **details):
    report = {
        "title": title,
        "sections": list(sections),
    }

    for key, value in details.items():
        if value is not None:
            report[key] = value

    return report


info_1 = {"name": "Ada", "city": "London"}
info_2 = {"name": "Sara", "school": "Lexicon"}

report_1 = create_report("My Day", "Morning", **info_1)
report_2 = create_report("School Work", "Java", "Python", **info_2)

print(report_1)
print(report_2)

missing_info = {"name": "Zaid"}
print(create_report("Home Task", "Reading", **missing_info))
