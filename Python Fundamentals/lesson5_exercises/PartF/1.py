
def create_report(title, *sections, **metadata):
    
    report = {
        "title": title,
        "sections": list(sections),
    }
    report.update(metadata)
    return report


print(create_report("Weekly Report", "Math", "Science", author="Alice", term="Spring"))
