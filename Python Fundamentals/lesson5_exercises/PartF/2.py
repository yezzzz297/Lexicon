
def create_report(title, *sections, **metadata):
    report = {
        "title": title,
        "sections": list(sections),
    }
    report.update(metadata)
    return report


report = create_report(
    "School Week",
    "python",
    "Java",
    teacher="Aladin",
    class_name="Python Fundamental",
)
print(report)
