
def create_report(title, *sections, **details):
    report = {
        "title": title,
        "sections": list(sections),
    }

    for key, value in details.items():
        if value is not None:
            report[key] = value

    return report


info_a = {"teacher": "Aladin", "subject": "Python"}
info_b = {"host": "Ada", "place": "Home"}

report_a = create_report("Class Notes", "Lesson 1", "Lesson 2", **info_a)
report_b = create_report("Birthday Plan", "Food", "Games", **info_b)

print(report_a)
print(report_b)
print(create_report("Simple Notes", "Reading"))
